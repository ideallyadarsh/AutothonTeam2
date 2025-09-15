from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.TestAutothon_Functions import TestAutothon_Functions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.Template_Functions import TemplateFunctions
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities

# run pipeline
@given(u'I Navigate to X')
def step_impl(context):
    context.functions = TemplateFunctions()
    context.functions.navigate_to_x()
#test
@when(u'I Click on Sign in button')
def step_impl(context):
    context.functions.click_on_sign_in_button()

@when(u'I Enter email/username and click next')
def step_impl(context):
    context.functions.enter_username_and_click_next()

@when(u'I Enter password and click Log in button')
def step_impl(context):
    context.functions.enter_password_and_click_log_in()

@then(u'I make posts and verify successful response')
def step_impl(context):
    context.functions.make_posts_and_verify_success()

@then(u'I search the three posts and verify the search results')
def step_impl(context):
    context.functions.search_three_posts_and_verify_results()


@then(u'I take a screenshot of the posts and save it in local')
def step_impl(context):
    context.functions.take_screenshot_of_posts_and_save_locally()