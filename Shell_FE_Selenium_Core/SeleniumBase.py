import json
import os
import subprocess
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


class SeleniumBase:
    """SeleniumBase class contains functions for reading config file, browser initiation"""
    # region Class Variable Declarations
    __config = None
    __browser = None
    __webdrivermanager = None
    __implicitwait = None
    __opts = None
    __environment = None
    __headless = None
    __incognito = None
    __acceptcerts = None
    __extensions = None
    __notifications = None
    __insecure_content = None
    __disable_popup = None
    __remote_exe = None
    __remote_environment = None
    __docker = None
    __seleniumgrid = None
    __remoteurl = None
    __remote_browser = None
    __browser_port = None
    #__remote_browser_version = None
    __remote_platform = None
    download_directory = None
    download_path = None
    user_profile = None
    user_dir_path = None
    driver = None
    url = None
    diff_app = None
    __run_on_testing_browser = None
    __binary_location = None
    __testing_browser_version = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    browserstack_config = current_working_directory + '/Shell_FE_Behave_Tests/browserstack.json'
    cloud_config = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else '../Shell_FE_Behave_Tests/config/config.json'
    __webdriver_executables = current_working_directory + '/Shell_FE_Behave_Tests/WebDriverExecutables/'
    TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
    caps = {}


    # endregion

    # region Reading data from Configuration files and initializing values to Class variables
    @staticmethod
    def read_config():
        """Reads behave.ini file present in Shell_FE_Behave_Tests folder.

        Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(SeleniumBase.configfile)
        return configuration

    @staticmethod
    def initialize_values():
        """Assigns respective values to class variables from behave.ini file.
        """
        SeleniumBase.__config = SeleniumBase.read_config()
        SeleniumBase.__browser = SeleniumBase.__config['browser']['browser_name']
        SeleniumBase.__webdrivermanager = SeleniumBase.__config.getboolean('browser', 'webdriver_manager')
        SeleniumBase.__implicitwait = SeleniumBase.__config['timeout']['implicit_wait']
        environment = SeleniumBase.__config['application']['environment']
        # region Application url initialization
        if environment == "dev":
            SeleniumBase.url = SeleniumBase.__config['application']['dev_url']
        elif environment == "qa":
            SeleniumBase.url = SeleniumBase.__config['application']['qa_url']
        elif environment == "stage":
            SeleniumBase.url = SeleniumBase.__config['application']['stage_url']
        elif environment == "prod":
            SeleniumBase.url = SeleniumBase.__config['application']['prod_url']
        else:
            print("Invalid environment name provided in INI file. Environment: {0}.".format(environment))
        # endregion
        # region Browser options initialization
        SeleniumBase.__headless = SeleniumBase.__config.getboolean('browser-options', 'headless')
        SeleniumBase.__incognito = SeleniumBase.__config.getboolean('browser-options', 'incognito')
        SeleniumBase.__acceptcerts = SeleniumBase.__config.getboolean('browser-options', 'accept_cert')
        SeleniumBase.__extensions = SeleniumBase.__config.getboolean('browser-options', 'disable_extensions')
        SeleniumBase.__notifications = SeleniumBase.__config.getboolean('browser-options', 'disable_notifications')
        SeleniumBase.__insecure_content = SeleniumBase.__config.getboolean('browser-options', 'allow_insecure_content')
        SeleniumBase.__disable_popup = SeleniumBase.__config.getboolean('browser-options', 'disable_popup')
        SeleniumBase.download_directory = SeleniumBase.__config.getboolean('browser-options', 'download_directory')
        SeleniumBase.user_profile = SeleniumBase.__config.getboolean('browser-options', 'user_profile')
        SeleniumBase.user_dir_path = SeleniumBase.__config['browser-options']['path_to_directory']
        SeleniumBase.__browser_port = SeleniumBase.__config['browser-options']['browser_port']
        # endregion
        SeleniumBase.__remote_exe = SeleniumBase.__config.getboolean('browser', 'remote')
        SeleniumBase.__remote_environment = SeleniumBase.__config['browser']['remote_environment']
        SeleniumBase.__remoteurl = SeleniumBase.__config['remote-options']['remote_url']
        SeleniumBase.__remote_browser = SeleniumBase.__config['remote-options']['remote_browser']
        #SeleniumBase.__remote_browser_version = SeleniumBase.__config['remote-options']['remote_browser_version']
        SeleniumBase.__remote_platform = SeleniumBase.__config['remote-options']['remote_platform']
        SeleniumBase.download_path = SeleniumBase.__config['browser-options']['download_path']

        """
        Reading the configuration data for chrome testing browser
        """
        SeleniumBase.__run_on_testing_browser = SeleniumBase.__config.getboolean('browser-options',
                                                                                 'run_on_testing_browser')
        SeleniumBase.__binary_location = SeleniumBase.__config['browser-options']['binary_location']
        SeleniumBase.__testing_browser_version = SeleniumBase.__config['browser-options']['testing_browser_version']

    # endregion

    # region WebDriver Initialization and dispose methods
    @staticmethod
    def browser_initialization():
        """Initializes browser based on the value passed in behave.ini file and assigns the respective driver to
        the class variable 'driver'.

        Raises:
            An exception if an invalid browser name is provided in behave.ini file

        Returns:
            Class variable 'driver' present in SeleniumBase
        """
        browsername = str(SeleniumBase.__browser).upper()
        if SeleniumBase.__remote_exe is False:
            if browsername == "CHROME":
                SeleniumBase.driver = SeleniumBase.__chrome_initialization()
            elif browsername == "FIREFOX":
                SeleniumBase.driver = SeleniumBase.__firefox_initialization()
            elif browsername == "IE":
                SeleniumBase.driver = SeleniumBase.__ie_initialization()
            elif browsername == "EDGE":
                SeleniumBase.driver = SeleniumBase.__edge_initialization()
            elif browsername == "SAFARI":
                SeleniumBase.driver = SeleniumBase.__safari_initialization()
            else:
                print("Invalid browser!!")
                raise Exception("Invalid Browser name passed. Aborting the UI tests!!")
        elif SeleniumBase.__remote_exe is True:
            remote_environment = str(SeleniumBase.__remote_environment).upper()
            if remote_environment == "BROWSERSTACK":
                SeleniumBase.driver = SeleniumBase.__browserstack_initialization()
            if remote_environment == "LAMBDATEST":
                SeleniumBase.driver = SeleniumBase.__lt_initialization()
            if remote_environment == "GRID":
                grid_browser = str(SeleniumBase.__browser).upper()
                if grid_browser == "CHROME":
                    SeleniumBase.driver = SeleniumBase.__seleniumgrid_chrome_initialization()
            if remote_environment == "DOCKER":
                docker_browser = str(SeleniumBase.__browser).upper()
                if docker_browser == "CHROME":
                    SeleniumBase.driver = SeleniumBase.__docker_chrome_initialization()
                elif docker_browser == "FIREFOX":
                    SeleniumBase.driver = SeleniumBase.__docker_firefox_initialization()
                elif docker_browser == "EDGE":
                    SeleniumBase.driver = SeleniumBase.__docker_edge_initialization()
        SeleniumBase.driver.implicitly_wait(int(SeleniumBase.__implicitwait))

    @staticmethod
    def __chrome_initialization():
        """Initializes driver to ChromeDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

        Returns:
            ChromeDriver instance
        """
        SeleniumBase.__opts = webdriver.ChromeOptions()
        # capability = DesiredCapabilities.CHROME.copy()
        SeleniumBase.set_options(SeleniumBase.__opts)
        if SeleniumBase.__webdrivermanager:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=SeleniumBase.__opts)
            return driver

        elif SeleniumBase.__docker:
            driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
            return driver
        elif SeleniumBase.__run_on_testing_browser:
            SeleniumBase.__opts.binary_location = SeleniumBase.__binary_location
            SeleniumBase.__opts.browser_version = SeleniumBase.__testing_browser_version
            chromedrivername = "chromedriver.exe"
            service = Service(executable_path=SeleniumBase.__webdriver_executables + chromedrivername)
            driver = webdriver.Chrome(options=SeleniumBase.__opts)
            return driver

        else:
            try:
                chromedrivername = "chromedriver.exe"
                service = Service(executable_path=SeleniumBase.__webdriver_executables + chromedrivername)
                # driver = webdriver.Chrome(service=service, options=SeleniumBase.__opts)
                driver = webdriver.Chrome(options=SeleniumBase.__opts)
                return driver
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __firefox_initialization():
        """Initializes driver to FirefoxDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                FirefoxDriver instance
        """
        SeleniumBase.__opts = webdriver.FirefoxOptions()
        SeleniumBase.set_options(SeleniumBase.__opts)

        if SeleniumBase.__webdrivermanager:
            service = Service(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=SeleniumBase.__opts)
            return driver
        elif SeleniumBase.__docker:
            driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
            return driver

        else:
            try:
                geckodrivername = "geckodriver"
                service = Service(executable_path=SeleniumBase.__webdriver_executables + geckodrivername)
                driver = webdriver.Firefox(service=service,
                                           options=SeleniumBase.__opts)
                return driver
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __edge_initialization():
        """Initializes driver to EdgeDriver. Based on value in behave.ini file WebDriver Manager or
        WebDriver binary would be used.

            Returns:
                Edgedriver instance
        """
        SeleniumBase.__opts = webdriver.EdgeOptions()
        SeleniumBase.__opts.use_chromium = True
        SeleniumBase.set_options(SeleniumBase.__opts)

        if SeleniumBase.__webdrivermanager:
            service = Service(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(options=SeleniumBase.__opts)
            return driver

        elif SeleniumBase.__docker:
            driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
            return driver

        else:
            try:
                if 'TF_BUILD' in os.environ or 'GITHUB_ACTIONS' in os.environ:
                    driver = webdriver.Edge(options=SeleniumBase.__opts)
                    return driver
                else:
                    subprocess.call(["powershell", f"msedge.exe --remote-debugging-port={SeleniumBase.__browser_port} --user-data-dir={SeleniumBase.user_dir_path}"], shell=True)
                    SeleniumBase.__opts.add_experimental_option("debuggerAddress", "localhost:9222")
                    driver = webdriver.Edge(options=SeleniumBase.__opts)
                    return driver
               
            
            except Exception as err:
                raise Exception(err)

    @staticmethod
    def __safari_initialization():
        """Initializes driver to Safari driver.
            Returns:
                  Safari driver instance
        """
        driver = webdriver.Safari()
        return driver

    @staticmethod
    def set_options(browser_options):
        opts = browser_options
        opts.headless = SeleniumBase.__headless
        opts.set_capability("acceptInsecureCerts", SeleniumBase.__acceptcerts)
        if SeleniumBase.__incognito:
            if str(SeleniumBase.__browser).upper() == "CHROME":
                opts.add_argument("--incognito")
            if str(SeleniumBase.__browser).upper() == "EDGE":
                opts.add_argument("-inprivate")
            if str(SeleniumBase.__browser).upper() == "FIREFOX":
                opts.add_argument("-private")
        if SeleniumBase.__extensions:
            opts.add_argument("--disable-extensions")
        if SeleniumBase.__notifications:
            opts.add_argument("--disable-notifications")
        if SeleniumBase.__insecure_content:
            opts.add_argument("--allow-running-insecure-content")
            opts.add_argument("--ignore-certificate-errors")
        if SeleniumBase.__disable_popup:
            opts.add_argument("--disable-popup-blocking")
        if SeleniumBase.download_directory:
            prefs = {"download.default_directory": SeleniumBase.download_path,
                     # "download.prompt_for_download": False,
                     # "download.directory_upgrade": True,
                     # "safebrowsing.enabled": True
                     }
            opts.add_experimental_option("prefs", prefs)
        if SeleniumBase.user_profile:
            opts.add_argument("--user-data-dir={0}.".format(SeleniumBase.user_dir_path))

    @staticmethod
    def __browserstack_initialization():
        """Initializes driver to remote webdriver with Browserstack based on the value provided in 'remote_environment'
         in Behave.INI file.

            Returns:
                Remote webdriver instance with Browserstack.
        """
        with open(SeleniumBase.browserstack_config) as config_file:
            config = json.load(config_file)

        username = config['user']
        accesskey = config['key']
        server = config['webServer']

        capabilities = config['webEnvironments'][SeleniumBase.TASK_ID]
        driver = webdriver.Remote(command_executor='https://{0}:{1}@{2}/wd/hub'.format(username, accesskey, server),
                                  desired_capabilities=capabilities)
        return driver

    @staticmethod
    def __lt_initialization():
        """Initializes driver to remote webdriver with lambdatest based on the value provided in 'remote_environment'
         in Behave.INI file.

            Returns:
                Remote webdriver instance with Browserstack.
        """

        with open(SeleniumBase.cloud_config) as lt_config_file:
            lt_config = json.load(lt_config_file)

        username = os.environ['LT_USERNAME'] if 'LT_USERNAME' in os.environ else lt_config['username']
        access_key = os.environ['LT_ACCESS_KEY'] if 'LT_ACCESS_KEY' in os.environ else lt_config['accessKey']
        desired_capabilities = lt_config['environments'][SeleniumBase.TASK_ID]
        if desired_capabilities['LT:Options']['browserName'].upper() == "CHROME":
            SeleniumBase.__opts = webdriver.ChromeOptions()
        elif desired_capabilities['LT:Options']['browserName'].upper() == "MICROSOFTEDGE":
            SeleniumBase.__opts = webdriver.EdgeOptions()
        elif desired_capabilities['LT:Options']['browserName'].upper() == "FIREFOX":
            SeleniumBase.__opts = webdriver.FirefoxOptions()
        elif desired_capabilities['LT:Options']['browserName'].upper() == "SAFARI":
            SeleniumBase.__opts = webdriver.SafariOptions()

        for key in lt_config["capabilities"]:
            if key == "LT:Options":
                desired_capabilities[key].update(lt_config["capabilities"][key])
                SeleniumBase.__opts.set_capability(key, desired_capabilities[key])

        selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        driver = webdriver.Remote(
            options=SeleniumBase.__opts,
            command_executor=selenium_endpoint)
        return driver

    @staticmethod
    def __seleniumgrid_chrome_initialization():
        """Initializes driver to Remote ChromeDriver configured in Selenium Grid. Based on value in behave.ini file.

        Returns:
            Remote ChromeDriver instance
        """
        SeleniumBase.__opts = webdriver.ChromeOptions()
        # capability = DesiredCapabilities.CHROME.copy()
        SeleniumBase.set_options(SeleniumBase.__opts)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", SeleniumBase.__remote_browser)
        chrome_options.set_capability("platformName", SeleniumBase.__remote_platform)
        # chrome_options.set_capability("browserVersion", SeleniumBase.__remote_browser_version)
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(
            command_executor=SeleniumBase.__remoteurl,
            options=chrome_options
        )
        return driver

    @staticmethod
    def __docker_chrome_initialization():
        SeleniumBase.__opts = webdriver.ChromeOptions()
        # capability = DesiredCapabilities.CHROME.copy()
        SeleniumBase.set_options(SeleniumBase.__opts)
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
        return driver

    @staticmethod
    def __docker_firefox_initialization():
        SeleniumBase.__opts = webdriver.FirefoxOptions()
        SeleniumBase.set_options(SeleniumBase.__opts)
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
        return driver

    @staticmethod
    def __docker_edge_initialization():
        SeleniumBase.__opts = webdriver.EdgeOptions()
        SeleniumBase.__opts.use_chromium = True
        SeleniumBase.set_options(SeleniumBase.__opts)
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=SeleniumBase.__opts)
        return driver

    @staticmethod
    def dispose():
        """Terminates all instances of WebDriver."""
        if SeleniumBase.driver is not None:
            SeleniumBase.driver.quit()
        # Enter code for closing the driver based on local or remote
    # endregion

    @staticmethod
    def close_browser_tabs():
        """Closes all the browser tabs."""
        for i in range(len(SeleniumBase.driver.window_handles)):
            SeleniumBase.driver.close()
