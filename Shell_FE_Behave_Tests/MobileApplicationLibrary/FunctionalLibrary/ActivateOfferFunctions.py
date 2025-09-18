import time
from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.ActivateOfferControls import ActivateOfferControls
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from appium.webdriver.common.appiumby import AppiumBy


class ActivateOfferFunctions:
    def __init__(self):
        self.ActivateOfferControls = ActivateOfferControls(AppiumBase.driver)

    def user_login(self):
        AppiumBase.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
                                       'new UiSelector().text("🇬🇧 [TEST] United Kingdom"))'
                                       )
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Country_Name())
        time.sleep(10)
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Sign_In_Button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Sign_In_Button())
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Email_Input)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Email_Input())
        AndroidUtilities.send_text_to_element(self.ActivateOfferControls.get_Email_Input(),
                                              'HackathonTeam10activateOffer@yopmail.com')
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Password_Input)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Password_Input())
        AndroidUtilities.send_text_to_element(self.ActivateOfferControls.get_Password_Input(), 'Shell@123')
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Disable_Security_Check_button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Disable_Security_Check_button())
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Sign_In_Button_2)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Sign_In_Button_2())
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Add_payment_method_NotNow_Button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Add_payment_method_NotNow_Button())
        try:
            WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Notification_Allow_Yesplease_Button)
            AndroidUtilities.click_element(self.ActivateOfferControls.get_Notification_Allow_Yesplease_Button())
            WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Notification_Allow_Button)
            AndroidUtilities.click_element(self.ActivateOfferControls.get_Notification_Allow_Button())
        except Exception as e:
            print("Notification buttons not found or already handled: ", e)

    def navigate_to_rewards_section_and_click_for_you_tab(self):
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.Rewards_button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_Rewards_button())
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.For_You_tab)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_For_You_tab())

    def check_inactive_offer_and_activate(self):
        no_of_offers = len(AppiumBase.driver.find_elements(AppiumBy.XPATH, '//*[contains(@text, "SHELL GO+ REWARDS")]/following-sibling::*//androidx.cardview.widget.CardView[@displayed="true"]'))
        for i in range(no_of_offers):
            try:
                WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.validate_offer_toggle_off_button)
                AndroidUtilities.click_element(self.ActivateOfferControls.get_validate_offer_toggle_off_button())
                print("Offer is activated")
            except Exception as e:
                print("No more offers to activate or element not found: ", e)
                break

    def validate_activated_offers_in_mycard_section(self):
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.My_Card_button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_my_card_button())
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.scan_your_digital_card_got_it)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_scan_your_digital_card_got_it())
        AppiumBase.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)')
        self.validate_activated_offers()
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.close_mycards_section)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_close_mycards_section())

    def validate_activated_offers(self):
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.first_offer)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_first_offer())
        try:
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.validate_offer_toggle_on_button)
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.redeem_now_button)
        except Exception as e:
            print("Offer is not activated: ", e)
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.second_offer)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_second_offer())
        try:
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.validate_offer_toggle_on_button)
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.redeem_now_button)
        except Exception as e:
            print("Offer is not activated: ", e)
        AndroidUtilities.click_back_button()

    # Validate if offer is deactivated and if not deactivate it        

    def check_active_offer_and_deactivate(self):
        no_of_offers = len(AppiumBase.driver.find_elements(AppiumBy.XPATH, '//*[contains(@text, "SHELL GO+ REWARDS")]/following-sibling::*//androidx.cardview.widget.CardView[@displayed="true"]'))
        for i in range(no_of_offers):
            try:
                WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.validate_offer_toggle_on_button)
                AndroidUtilities.click_element(self.ActivateOfferControls.get_validate_offer_toggle_on_button())
                print("Offer is deactivated")
            except Exception as e:
                print("No more offers to deactivate or element not found: ", e)
                break

    def validate_deactivated_offers_in_mycard_section(self):
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.My_Card_button)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_my_card_button())
        AppiumBase.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)')
        self.validate_deactivated_offers()

    def validate_deactivated_offers(self):
        time.sleep(3)
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.first_offer)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_first_offer())
        try:
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.validate_offer_toggle_off_button)
        except Exception as e:
            print("Offer is not deactivated: ", e)
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.ActivateOfferControls.second_offer)
        AndroidUtilities.click_element(self.ActivateOfferControls.get_second_offer())
        try:
            AndroidUtilities.is_element_displayed(self.ActivateOfferControls.validate_offer_toggle_off_button)
        except Exception as e:
            print("Offer is not deactivated: ", e)
        AndroidUtilities.click_back_button()
