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

current_working_directory = os.path.dirname(os.getcwd())
# def before_all(context):
#     if "mobile" in context.feature.tags:
#         AppiumBase.start_appium_server()
#     else:
#         SeleniumBase.initialize_values()

def before_all(context):
    # AppiumBase.start_appium_server()
    SeleniumBase.initialize_values()

def before_feature(context, feature):
        # AppiumBase.launch_application("android")
        # SeleniumBase.browser_initialization()
    # context.feature = feature
    if "web" in feature.tags:
        # SeleniumBase.browser_initialization()
        pass
    else:
        # behave --define remote=True
        # can launch lambda device or local android device
        my_param = "True" == context.config.userdata.get('remote', False)
        AppiumBase.launch_application("android",my_param)
        config = AppiumBase.read_config()
        # AppiumBase.driver.activate_app(config['Android']['appPackage'])

def before_scenario(context, scenario):
    if "web" in context.feature.tags:
        SeleniumBase.browser_initialization()
    else:
        AppiumBase.driver.start_recording_screen(videoQuality='low', timeLimit=1800, videoFps=5, videoType='mpeg4')

def after_step(context, step):
    screenshot_name = str(context.scenario.name).replace(" ", "_") + '_' +str(step.name).replace(" ", "_")
    if "web" in context.feature.tags:
        BrowserUtilities.take_screenshot(screenshot_name)
        allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name= screenshot_name,
                    attachment_type=AttachmentType.PNG)
    else:
        AndroidUtilities.take_screenshot(screenshot_name)
        allure.attach(AppiumBase.driver.get_screenshot_as_png(), name= screenshot_name,
                    attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    my_param = "True" == context.config.userdata.get('remote', False)
    if "mobile" in context.feature.tags and my_param == False:
        # time.sleep(20)
        video_rawData = AppiumBase.driver.stop_recording_screen()
        # time.sleep(25)
        configuration = ConfigParser()
        configuration.read(AppiumBase.configfile)
        device_name = "Phone"
        video_name = (context.scenario.name).replace(" ","_") +"_" +time.strftime("%Y_%m_%d_%H%M%S")
        file_path = os.path.join(current_working_directory + "/Shell_FE_Behave_Tests/TestResults/Videos/",
                                 device_name + " " + video_name + ".mp4")
        with open(file_path, "wb+") as vd:
            vd.write(base64.b64decode(video_rawData))
    elif "web" in context.feature.tags:
        # SeleniumBase.close_browser_tabs()
        SeleniumBase.driver.quit()
        
    config = SeleniumBase.read_config()
    azure_value = config.getboolean('Azure_Test_plan', 'update_result') 
    if scenario.status == "failed":
        if "web" in context.feature.tags:
            allure.attach(SeleniumBase.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
 
        if azure_value:
 
            for tag in context.scenario.tags:
                try:
                    print(tag)
                    pid = int(tag)
                    if "int" in str(type(pid)):
                        dictionary = {pid: "failed"}
                        FileUtilities.append_dictionary_into_json(dictionary,
                                                                  f"{config['azure_test_result']['filename']}")
                        BrowserUtilities.log.info("Test case ID and status value:" + str(dictionary))
                except:
                    pass
 
    elif scenario.status == "passed":
        if azure_value:
            for tag in context.scenario.tags:
                try:
                    print(tag)
                    pid = int(tag)
                    if "int" in str(type(pid)):
                        dictionary = {pid: "passed"}
                        FileUtilities.append_dictionary_into_json(dictionary,
                                                                  f"{config['azure_test_result']['filename']}")
                        BrowserUtilities.log.info("Test case ID and status value:" + str(dictionary))
                except:
                    pass
 

    


# def after_feature(context, scenario):
#     if "web" in scenario.name.lower():
#         SeleniumBase.close_browser_tabs()
#     else:
#         AppiumBase.close_driver()
#         AppiumBase.stop_appium_server()
#     if scenario.status == "failed":
#         allure.attach(AppiumBase.driver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)
          




def after_feature(context, feature):
    """The below code is used to mark the test results in Browserstack as passed or failed based on the assertions
    validated. This method should be commented out or removed if in case Browserstack execution is not performed"""
    # if context.failed is True:
    #     AppiumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At '
    #         'least 1 assertion failed"}}')
    # if context.failed is not True:
    #     AppiumBase.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All '
    #         'assertions passed"}}')
    if "web" in feature.tags:
        # SeleniumBase.close_browser_tabs()
        pass
    else:
        
        config = AppiumBase.read_config()
        AppiumBase.driver.terminate_app(config['Android']['appPackage'])
        AppiumBase.driver.quit()
        AppiumBase.stop_appium_server()
        


# def after_scenario(context, scenario):
#     if scenario.status == "failed":
#         allure.attach(AppiumBase.driver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)

# def after_feature(context, feature):
#     if "web" in feature.tags:


def after_all(context):
    # AppiumBase.close_driver()
    config = AppiumBase.read_config()
    azure_value = config.getboolean('Azure_Test_plan', 'update_result')
    file_name = config['azure_test_result']['filename']
    time.sleep(10)
    if azure_value:
        # file_name - name of the file, that you have declared in the behave.ini
        TestResultUpdate.test_plan_result_update(file_name)
        FileUtilities.copy_file_to_directory(f"{file_name}", f"AzureTestResultHistory/{file_name}")
        FileUtilities.delete_file(f"{file_name}")