from appium.webdriver.common.mobileby import MobileBy


class ActivateOfferControls:

    def __init__(self, driver):
        self.driver = driver

    Country_Name = (MobileBy.XPATH, '//*[@text="🇬🇧 [TEST] United Kingdom"]')
    Sign_In_Button = (MobileBy.XPATH, '//*[@text="Sign in"]')
    Email_Input = (MobileBy.XPATH, '//*[@text="Email"]')
    Password_Input = (MobileBy.XPATH, '//*[@text="Password"]')
    Disable_Security_Check_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellListComponentSwitch"]')
    Sign_In_Button_2 = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/mainButtonTextView"]')

    Add_payment_method_NotNow_Button = (MobileBy.XPATH, '//*[@text="Not now"]')
    Notification_Allow_Yesplease_Button = (MobileBy.XPATH, '//*[@text="Yes please"]')
    Notification_Allow_Button = (MobileBy.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')

    Rewards_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellBottomBarItemIcon" and ./following-sibling::*[@text="Rewards"]]')
    For_You_tab = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellCustomTabTitleSelected"]')
    first_offer_toggle_off_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellCardActivationActivateSwitch" and ./preceding-sibling::*[@text="Valid until 16/08/2025"]]')
    second_offer_toggle_off_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellCardActivationActivateSwitch" and ./preceding-sibling::*[@text="Valid until 30/09/2025"]]')

    generic_offer_button = (MobileBy.XPATH, '//androidx.cardview.widget.CardView[@displayed="true"]//android.widget.ImageView')
    first_offer = (MobileBy.XPATH, '//*[@class="android.view.ViewGroup" and ./*[@text="welcome 4 july Title"]]')
    second_offer = (MobileBy.XPATH, '//*[@class="android.view.ViewGroup" and ./*[@text="Surprise fixed discount - 1GBP off on fuel "]]')
    redeem_now_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/extendedFabText"]')

    My_Card_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/extendedFabIcon"]')
    validate_offer_toggle_off_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellCardActivationActivateSwitch" and ./preceding-sibling::*[@resource-id="com.shell.sitibv.retail:id/shellCardActivationText"]]')
    validate_offer_toggle_on_button = (MobileBy.XPATH, '//*[@resource-id="com.shell.sitibv.retail:id/shellCardActivationActivateSwitch" and ./preceding-sibling::*[@resource-id="com.shell.sitibv.retail:id/shellCardActivatedText"]]')

    scan_your_digital_card_got_it = (MobileBy.XPATH,'//*[@resource-id="com.shell.sitibv.retail:id/mainButtonTextView"]')
    close_mycards_section = (MobileBy.XPATH,'//*[@resource-id="com.shell.sitibv.retail:id/shellTopBarNavigationIcon"]')

    def get_Country_Name(self):
        return self.driver.find_element(*ActivateOfferControls.Country_Name)
    
    def get_Sign_In_Button(self):
        return self.driver.find_element(*ActivateOfferControls.Sign_In_Button)
    
    def get_Email_Input(self):
        return self.driver.find_element(*ActivateOfferControls.Email_Input)     

    def get_Password_Input(self):
        return self.driver.find_element(*ActivateOfferControls.Password_Input)
    
    def get_Disable_Security_Check_button(self):
        return self.driver.find_element(*ActivateOfferControls.Disable_Security_Check_button)
    
    def get_Sign_In_Button_2(self):
        return self.driver.find_element(*ActivateOfferControls.Sign_In_Button_2)    
    
    def get_Add_payment_method_NotNow_Button(self):
        return self.driver.find_element(*ActivateOfferControls.Add_payment_method_NotNow_Button)

    def get_Notification_Allow_Button(self):
        return self.driver.find_element(*ActivateOfferControls.Notification_Allow_Button)
    
    def get_Notification_Allow_Yesplease_Button(self):
        return self.driver.find_element(*ActivateOfferControls.Notification_Allow_Yesplease_Button)
    
    def get_Rewards_button(self):
        return self.driver.find_element(*ActivateOfferControls.Rewards_button)
    
    def get_For_You_tab(self):
        return self.driver.find_element(*ActivateOfferControls.For_You_tab) 
    
    def get_second_offer_toggle_off_button(self):
        return self.driver.find_element(*ActivateOfferControls.second_offer_toggle_off_button)  
    
    def get_first_offer_toggle_off_button(self):
        return self.driver.find_element(*ActivateOfferControls.first_offer_toggle_off_button)  
    
    def get_first_offer(self):
        return self.driver.find_element(*ActivateOfferControls.first_offer) 
    
    def get_second_offer(self):
        return self.driver.find_element(*ActivateOfferControls.second_offer)
    
    def get_my_card_button(self):
        return self.driver.find_element(*ActivateOfferControls.My_Card_button)
    
    def get_validate_offer_toggle_off_button(self):
        return self.driver.find_element(*ActivateOfferControls.validate_offer_toggle_off_button)
    
    def get_validate_offer_toggle_on_button(self):
        return self.driver.find_element(*ActivateOfferControls.validate_offer_toggle_on_button)
    
    def get_scan_your_digital_card_got_it(self):
        return self.driver.find_element(*ActivateOfferControls.scan_your_digital_card_got_it)

    def get_close_mycards_section(self):
        return self.driver.find_element(*ActivateOfferControls.close_mycards_section)

    

