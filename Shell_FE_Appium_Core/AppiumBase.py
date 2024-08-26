import json
import os
from appium.webdriver.appium_service import AppiumService
from configparser import ConfigParser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


class AppiumBase:
    """AppiumBase class contains functions for reading config file, app initiation"""
    # region Class Variable Declarations
    __config = None
    __platformName = None
    __platformVersion = None
    __deviceName = None
    __remoteURL = None
    __browser_name = None
    __application_type = None
    __automation_name = None
    __remote_exe = None
    __remote_environment = None
    __implicitwait = None
    devicePlatform = None
    app = None
    udid = None
    bundle_id = None
    appPackage = None
    appActivity = None
    driver = None
    noReset = None
    appPathFlag = None
    bundleIdPath = None
    appPackageFlag = None
    __parallel = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    app_browserstack_config = current_working_directory + '/Shell_FE_Behave_Tests/browserstack.json'
    TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
    appium_Service = AppiumService()
    app_lt_config = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else '../Shell_FE_Behave_Tests/config/config.json'
    __android_browser_library = None
    __ios_browser_library = None
    # endregion

    # region Appium server instance
    @staticmethod
    def start_appium_server():
        """Starts the Appium Server"""
        AppiumBase.appium_Service.start(args=['--base-path', '/wd/hub'])

    @staticmethod
    def stop_appium_server():
        """Stops the current Appium server"""
        AppiumBase.appium_Service.stop()

    @staticmethod
    def appium_server_status():
        """Checks the appium server status
           :returns:
                   True - if the appium server instance is running
        """
        return AppiumBase.appium_Service.is_running

    # endregion

    # region Reading values from configuration file
    @staticmethod
    def read_config():
        """Reads behave.INI file present in Shell_FE_Behave_Tests folder.
           Returns:
                An instance of ConfigParser.
        """
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        return configuration

    @staticmethod
    def read_values():
        """"Read and Assigns respective values to class variables from behave.INI file.
            :args:
            -section_value - chooses the section from which value to be fetched
        """
        AppiumBase.__config = AppiumBase.read_config()
        AppiumBase.__implicitwait = AppiumBase.__config['timeout']['implicit_wait']
        # BrowserStack value initialization
        AppiumBase.__remote_exe = AppiumBase.__config.getboolean('MobilityCloudIntegration', 'remote')
        AppiumBase.__remote_environment = AppiumBase.__config['MobilityCloudIntegration']['remote_environment']

        if AppiumBase.devicePlatform.lower() == "android":
            AppiumBase.__platformName = AppiumBase.__config['Android']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['Android']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['Android']['deviceName']
            AppiumBase.app = AppiumBase.__config['Android']['appPath']
            AppiumBase.appPackage = AppiumBase.__config['Android']['appPackage']
            AppiumBase.appActivity = AppiumBase.__config['Android']['appActivity']
            AppiumBase.__remoteURL = AppiumBase.__config['Android']['remoteURL']
            AppiumBase.__application_type = AppiumBase.__config['Android']['applicationType']
            AppiumBase.__automation_name = AppiumBase.__config['Android']['automationName']
            AppiumBase.__browser_name = AppiumBase.__config['Android']['browserName']
            AppiumBase.appPathFlag = AppiumBase.__config.getboolean('Android', 'runAppWithPath')
            AppiumBase.noRest = AppiumBase.__config.getboolean('Android', 'noReset')
            AppiumBase.appPackageFlag = AppiumBase.__config.getboolean('Android', 'runAppWithPackage')
            AppiumBase.__android_browser_library = AppiumBase.__config['Android']['android_browser_Library']

        elif AppiumBase.devicePlatform.lower() == "ios":
            AppiumBase.__application_type = AppiumBase.__config['iOS']['applicationType']
            AppiumBase.__platformName = AppiumBase.__config['iOS']['platformName']
            AppiumBase.__platformVersion = AppiumBase.__config['iOS']['platformVersion']
            AppiumBase.__deviceName = AppiumBase.__config['iOS']['deviceName']
            AppiumBase.udid = AppiumBase.__config['iOS']['udid']
            AppiumBase.bundle_id = AppiumBase.__config['iOS']['bundleId']
            AppiumBase.app = AppiumBase.__config['iOS']['appPath']
            AppiumBase.__remoteURL = AppiumBase.__config['iOS']['remoteURL']
            AppiumBase.__automation_name = AppiumBase.__config['iOS']['automationName']
            AppiumBase.__browser_name = AppiumBase.__config['iOS']['browserName']
            AppiumBase.noRest = AppiumBase.__config.getboolean('iOS', 'noReset')
            AppiumBase.appPathFlag = AppiumBase.__config.getboolean('iOS', 'runAppWithPath')
            AppiumBase.bundleIdPath = AppiumBase.__config.getboolean('iOS', 'runAppWithBundleId')
            AppiumBase.__ios_browser_library = AppiumBase.__config['iOS']['ios_browser_library']

    # endregion

    # region Launch Application
    @staticmethod
    def launch_application(device_type=None,remote=False):
        """Launches the Application
           Returns the driver instance
        """
        global android_options, ios_options
        if device_type is None:
            AppiumBase.__config = AppiumBase.read_config()
            AppiumBase.devicePlatform = AppiumBase.__config['automationplatform']['platformtype']
            AppiumBase.read_values()
            if AppiumBase.devicePlatform.lower() == "android":
                android_options = UiAutomator2Options()
                android_options.platform_name = AppiumBase.__platformName
                android_options.platform_version = AppiumBase.__platformVersion
                android_options.device_name = AppiumBase.__deviceName
                android_options.automation_name = AppiumBase.__automation_name
                android_options.no_reset=True
                android_options.auto_grant_permissions=True
                # android_options.force_app_launch=True
            elif AppiumBase.devicePlatform.lower() == "ios":
                ios_options = XCUITestOptions()
                ios_options.platform_name = AppiumBase.__platformName
                ios_options.platform_version = AppiumBase.__platformVersion
                ios_options.device_name = AppiumBase.__deviceName
                ios_options.automation_name = AppiumBase.__automation_name

        elif device_type.lower() == "android":
            AppiumBase.devicePlatform = "android"
            AppiumBase.read_values()
            android_options = UiAutomator2Options()
            android_options.platform_name = AppiumBase.__platformName
            android_options.platform_version = AppiumBase.__platformVersion
            android_options.device_name = AppiumBase.__deviceName
            android_options.automation_name = AppiumBase.__automation_name
            android_options.no_reset=True
            android_options.auto_grant_permissions=True
            # android_options.force_app_launch=True
        elif device_type.lower() == "ios":
            AppiumBase.devicePlatform = "ios"
            AppiumBase.read_values()
            ios_options = XCUITestOptions()
            ios_options.platform_name = AppiumBase.__platformName
            ios_options.platform_version = AppiumBase.__platformVersion
            ios_options.device_name = AppiumBase.__deviceName
            ios_options.automation_name = AppiumBase.__automation_name

        if remote is False:

            if AppiumBase.__application_type.lower() == "native" or AppiumBase.__application_type.lower() == "hybrid":
                if AppiumBase.devicePlatform.lower() == "android":
                    if AppiumBase.appPackageFlag is True:
                        android_options.app_package= AppiumBase.appPackage
                        android_options.app_activity= AppiumBase.appActivity
                        android_options.no_reset=True
                        android_options.auto_grant_permissions=True
                        # android_options.force_app_launch=True

                    if AppiumBase.appPathFlag is True:
                        android_options.app= AppiumBase.app
                        android_options.no_reset=True
                        android_options.auto_grant_permissions=True
                        # android_options.force_app_launch=True

                elif AppiumBase.devicePlatform.lower() == "ios":
                    ios_options.udid= AppiumBase.udid

                    if AppiumBase.bundleIdPath is True:
                        ios_options.bundle_id= AppiumBase.bundle_id
                    if AppiumBase.appPathFlag is True:
                        ios_options.app= AppiumBase.app
                    if AppiumBase.noReset is True:
                        ios_options.app = AppiumBase.app

            elif AppiumBase.__application_type.lower() == "webbrowser":
                if AppiumBase.devicePlatform.lower() == "android":
                    android_options.browser_name= AppiumBase.__browser_name
                    android_options.set_capability("chromedriverExecutable", AppiumBase.__android_browser_library)
                    AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, options=android_options)
                elif AppiumBase.devicePlatform.lower() == "ios":
                    ios_options.browser_name = AppiumBase.__browser_name
                    ios_options.set_capability("safaridriverExecutable", AppiumBase.__ios_browser_library)
                    AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, options=ios_options)
            if device_type is not None:
                if device_type.lower() == "android":
                    AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, options=android_options)
                elif device_type.lower() == "ios":
                    AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, options=ios_options)
            else:
                AppiumBase.driver = webdriver.Remote(AppiumBase.__remoteURL, options=android_options)


        elif remote is True:
            remote_environment = str(AppiumBase.__remote_environment).upper()
            if remote_environment == "LAMBDATEST":
                AppiumBase.driver = AppiumBase.__app_lt_initialization()
        AppiumBase.driver.implicitly_wait(int(AppiumBase.__implicitwait))

    # endregion

    @staticmethod
    def install_app():
        """Install the App in the device"""
        AppiumBase.driver.install_app(AppiumBase.app)

    @staticmethod
    def is_App_installed():
        """Checks the app is installed in the device
            Return True- if the application is installed
        """
        app_installed = AppiumBase.driver.is_app_installed(AppiumBase.app)
        return app_installed

    @staticmethod
    def reset_app():
        """Reset the currently running app for this session"""
        AppiumBase.driver.reset()

    @staticmethod
    def close_app():
        """It closes the app on the device"""
        AppiumBase.driver.close_app()

    @staticmethod
    def remove_app():
        """Remove an app from the device"""
        AppiumBase.driver.remove_app(AppiumBase.app)

    @staticmethod
    def close_driver():
        """Closes the current driver session"""
        if AppiumBase.driver is not None:
            AppiumBase.driver.quit()

    # @staticmethod
    # def __app_browserstack_initialization():
    #     with open(AppiumBase.app_browserstack_config) as config_file:
    #         config = json.load(config_file)
    #
    #     username = config['user']
    #     accesskey = config['key']
    #
    #     server = config['appServer']
    #
    #     capabilities = config['appCapabilities']
    #     capabilities['device'] = config['appEnvironments'][AppiumBase.TASK_ID]['device']
    #     driver = webdriver.Remote(
    #         command_executor='http://{0}:{1}@{2}/wd/hub'.format(username, accesskey, server),
    #         desired_capabilities=dict(capabilities))
    #     return driver

    @staticmethod
    def __app_lt_initialization():
        with open(AppiumBase.app_lt_config) as lt_app_config_file:
            lt_app_config = json.load(lt_app_config_file)

        username = os.environ['LT_USERNAME'] if 'LT_USERNAME' in os.environ else lt_app_config['username']
        access_key = os.environ['LT_ACCESS_KEY'] if 'LT_ACCESS_KEY' in os.environ else lt_app_config['accessKey']

        if AppiumBase.devicePlatform.lower() == "android":
            desired_capabilities = lt_app_config['androidappenvironments'][AppiumBase.TASK_ID]
            android_options_lt = UiAutomator2Options()
            android_options_lt.no_reset = True
            android_options.auto_grant_permissions = True
            android_options_lt.load_capabilities(desired_capabilities)

            for key in lt_app_config["appcapabilities_android"]:
                if key not in desired_capabilities:
                    desired_capabilities[key] = lt_app_config["appcapabilities_android"][key]
                    android_options_lt.load_capabilities(desired_capabilities)
                elif key == "LT:Options":
                    desired_capabilities[key].update(lt_app_config["appcapabilities_android"][key])
                    android_options_lt.load_capabilities(desired_capabilities)
            desired_capabilities['LT:Options']['source'] = 'behave:sample-master:v1.1'

            appium_endpoint = "http://{}:{}@mobile-hub.lambdatest.com/wd/hub".format(username, access_key)

            # driver = webdriver.Remote(command_executor=appium_endpoint, desired_capabilities=desired_capabilities)
            driver = webdriver.Remote(command_executor=appium_endpoint, options=android_options_lt)
            return driver

        # if AppiumBase.devicePlatform.lower() == "ios":
        #     desired_capabilities = lt_app_config['iosappenvironments'][AppiumBase.TASK_ID]
        #     ios_options_lt = XCUITestOptions()
        #     ios_options_lt.load_capabilities(desired_capabilities)
        #
        #     for key in lt_app_config["appcapabilities_ios"]:
        #         if key not in desired_capabilities:
        #             desired_capabilities[key] = lt_app_config["appcapabilities_ios"][key]
        #             ios_options_lt.load_capabilities(desired_capabilities)
        #         elif key == "LT:Options":
        #             desired_capabilities[key].update(lt_app_config["appcapabilities_ios"][key])
        #             ios_options_lt.load_capabilities(desired_capabilities)
        #     desired_capabilities['LT:Options']['source'] = 'behave:sample-master:v1.1'
        #
        #     appium_endpoint = "http://{}:{}@mobile-hub.lambdatest.com/wd/hub".format(username, access_key)
        #
        #     driver = webdriver.Remote(command_executor=appium_endpoint, options=ios_options_lt)
        #     return driver

        if AppiumBase.devicePlatform.lower() == "ios":
            desired_capabilities = lt_app_config['iosappenvironments'][AppiumBase.TASK_ID]
            for key in lt_app_config["appcapabilities_ios"]:
                if key not in desired_capabilities:
                    desired_capabilities[key] = lt_app_config["appcapabilities_ios"][key]
                elif key == "LT:Options":
                    desired_capabilities[key].update(lt_app_config["appcapabilities_ios"][key])
            desired_capabilities['LT:Options']['source'] = 'behave:sample-master:v1.1'

            appium_endpoint = "http://{}:{}@mobile-hub.lambdatest.com/wd/hub".format(username, access_key)

            opts = XCUITestOptions()
            opts.load_capabilities(desired_capabilities)

            driver = webdriver.Remote(command_executor=appium_endpoint, options=opts)
            return driver

