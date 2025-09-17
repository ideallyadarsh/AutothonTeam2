import os
import sys
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from allure_commons.types import AttachmentType
import allure
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.iOSUtilities import IOSUtilities
import base64
import os
import shutil
import sys
import time
from configparser import ConfigParser
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
sys.path.insert(0, os.path.dirname(os.getcwd()))
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Azure_Test_Result_update import TestResultUpdate
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
 
current_working_directory = os.path.dirname(os.getcwd())
 
def before_all(context):
    try:
        AppiumBase.start_appium_server()
        print("Appium server started successfully")
    except Exception as e:
        print(f"Failed to start Appium server: {e}")
        # Continue without server for remote execution

    SeleniumBase.initialize_values()
 
def before_feature(context, feature):
    if "web" in feature.tags:
        pass
    else:
        try:
            print("Attempting to launch Android application...")
            
            # Check configuration before launching
            config = AppiumBase.read_config()
            print(f"Config sections: {list(config.keys())}")
            
            if 'Android' not in config:
                raise KeyError("Android section missing from configuration file")
            
            android_config = config['Android']
            required_keys = ['platformName', 'deviceName', 'appPackage', 'appPath']
            missing_keys = [key for key in required_keys if key not in android_config]
            
            if missing_keys:
                raise KeyError(f"Missing required Android configuration keys: {missing_keys}")
            
            print(f"Platform: {android_config.get('platformName')}")
            print(f"Device: {android_config.get('deviceName')}")
            print(f"App Package: {android_config.get('appPackage')}")
            print(f"App Path: {android_config.get('appPath')}")
            
            AppiumBase.launch_application("android")
            context.driver = AppiumBase.driver
            
            print(f"Driver initialized successfully: {AppiumBase.driver is not None}")
            
        except Exception as e:
            print(f"Failed to launch application: {e}")
            AppiumBase.driver = None
            context.driver = None
            raise
 
def before_scenario(context, scenario):
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()
    else:
        # Only execute if driver exists
        if AppiumBase.driver is not None:
            try:
                AppiumBase.driver.start_recording_screen(videoQuality='low', timeLimit=1800, videoFps=5, videoType='mpeg4')
                AppiumBase.driver.execute_script(f'lambda-name={scenario.name}')
            except Exception as e:
                print(f"Error in before_scenario: {e}")
 
def before_step(context, step):
    SeleniumUtilities.log.info(f"Step: {step.name}")
 
def after_step(context, step):
    if step.status == "failed":
        screenshot_name = str(context.scenario.name).replace(" ", "_")
        # For UI automation
        if "web" in context.feature.tags:
            BrowserUtilities.take_screenshot(screenshot_name)
        # For Mobile automation
        elif AppiumBase.driver is not None:
            try:
                AndroidUtilities.take_screenshot(screenshot_name)
            except Exception as e:
                print(f"Error taking mobile screenshot: {e}")
 
def after_scenario(context, scenario):
    # Only execute if driver exists
    if AppiumBase.driver is not None:
        try:
            if scenario.status == "passed":
                AppiumBase.driver.execute_script('lambda-status=passed')
            elif scenario.status == "failed":
                AppiumBase.driver.execute_script('lambda-status=failed')
        except Exception as e:
            print(f"Error updating scenario status: {e}")
 
def after_feature(context, feature):
    """The below code is used to mark the test results in Browserstack as passed or failed based on the assertions
    validated. This method should be commented out or removed if in case Browserstack execution is not performed"""
    
    if "web" in feature.tags:
        pass
    else:
        # Only execute cleanup if driver exists
        if AppiumBase.driver is not None:
            try:
                config = AppiumBase.read_config()
                if 'Android' in config and 'appPackage' in config['Android']:
                    AppiumBase.driver.terminate_app(config['Android']['appPackage'])
                AppiumBase.driver.quit()
            except Exception as e:
                print(f"Error during cleanup: {e}")
            finally:
                AppiumBase.driver = None
        
        try:
            AppiumBase.stop_appium_server()
        except Exception as e:
            print(f"Error stopping Appium server: {e}")
 
def after_all(context):
    try:
        config = AppiumBase.read_config()
        azure_value = config.getboolean('Azure_Test_plan', 'update_result')
        file_name = config['azure_test_result']['filename']
        time.sleep(10)
        if azure_value:
            TestResultUpdate.test_plan_result_update(file_name)
            FileUtilities.copy_file_to_directory(f"{file_name}", f"AzureTestResultHistory/{file_name}")
            FileUtilities.delete_file(f"{file_name}")
    except Exception as e:
        print(f"Error in after_all: {e}")