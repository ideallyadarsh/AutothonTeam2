from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.TestAutothon_Functions import TestAutothon_Functions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.Autothon_Functions import AutothonFunctions

# Mobile Application Steps
@Given('I launch the step in application')
def step_def(context):
    context.app_functions = TestAutothon_Functions()
    context.app_functions.click_get_products()

@When('I fetch product details')
def ste_def(context):
    context.app_functions.get_product_details()

@Then('I post and verify the product details')
def step_def(context):
    context.app_functions.post_and_validate_product_details()

@Given('I Navigate to Indian Express')
def step_def(context):
    context.functions = AutothonFunctions()
    context.functions.navigate_to_indian_express()
 
@When('I Click on Politics')
def step_def(context):
    context.functions.click_on_politics()

@when(u'I Click on carousel')
def step_impl(context):
    context.functions.click_on_carousel()

@then("I post and verify article details")
def step_impl(context):
    context.functions.post_and_validate_article_details()