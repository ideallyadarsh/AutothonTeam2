from behave import *
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.Auto_Functions import Auto_Functions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.Autothon_Functions import AutothonFunctions

@Given('I open and login to instagram')
def step_def(context):
    context.app_functions = Auto_Functions()
    context.app_functions.login_to_instagram()

@Then('I upload the image')
def step_def(context):
    context.app_functions.upload_image()


@given(u'when I login in to twitter')
def step_impl(context):
    #whenever initiaizing functions, add maximise window
    context.functions = AutothonFunctions()
    context.functions.navigate_to_twitter()

@when('I call twitter API and stores the screenshot')
def step_impl(context):
    tweet_id = context.functions.call_twitter_api()
    context.functions.screenshot_tweet(tweet_id)

@given(u'when I login in to linkedin')
def step_impl(context):
    context.functions = AutothonFunctions()
    context.functions.navigate_to_linkedin()

@when('I call linkedin API and  store the screenshot')
def step_impl(context):
    post_id = context.functions.call_linkedin_api()
    context.functions.screenshot_linkedin_post(post_id)

    

# @given('I have launched the apidemos app')
# def open_views(context):
#     context.api_Demos_functions = Auto_Functions()
#     context.api_Demos_functions.click_views()


# @when('I test views')
# def open_controls(context):
#     context.api_Demos_functions.click_controls()


# @then('I verify checkbox and radio buttons')
# def verify_check_box(context):
#     context.api_Demos_functions.click_checkbox()


# # @when('I Click on Views')
# # def verify_back_btn(context):
# #     context.api_Demos_functions.check_back_button()
# #
# #
# # @then('I verify popups')
# # def check_scroll_function(context):
# #     #context.feature.api_Demos_functions.check_drag_and_drop()
# #     context.api_Demos_functions.check_scroll()
# #     context.api_Demos_functions.check_tap()

