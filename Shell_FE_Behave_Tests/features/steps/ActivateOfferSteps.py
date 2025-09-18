from behave import *
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Behave_Tests.MobileApplicationLibrary.FunctionalLibrary.ActivateOfferFunctions import \
    ActivateOfferFunctions


@given('User logs into the application')
def step_impl(context):
    # Ensure driver is available
    if not hasattr(context, 'driver') or context.driver is None:
        if AppiumBase.driver is None:
            raise RuntimeError("Mobile driver not initialized. Check your configuration file.")
        context.driver = AppiumBase.driver
    
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.user_login()

@when('User navigates to the Rewards section and click on For You tab')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.navigate_to_rewards_section_and_click_for_you_tab()

@when('Validate if offer is activated')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.check_inactive_offer_and_activate()

@when('Validate activated offers')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.validate_activated_offers()

@when('Validate my activated offers in mycard section')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.validate_activated_offers_in_mycard_section()    

@when('Validate if offer is deactivated')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.check_active_offer_and_deactivate()

@when('Validate deactivated offers')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.validate_deactivated_offers()

@when('Validate my deactivated offers in mycard section')
def step_impl(context):
    context.activate_offer_functions = ActivateOfferFunctions()
    context.activate_offer_functions.validate_deactivated_offers_in_mycard_section()    