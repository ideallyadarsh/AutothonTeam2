from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.Auto_Controls import Auto_Controls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
import time
import base64


class Auto_Functions:
    log = LoggingUtilities()
    log_file = log.logger()

    def __init__(self):
        self.auto_controls = Auto_Controls(AppiumBase.driver)
        # with open("..\..\Web_Autothon\Shell_FE_Behave_Tests\TestData\Images\tweet.png", 'rb') as image_file:
        #     image_data = image_file.read()
        # AppiumBase.driver.push_file("/storage/emulated/0/DCIM/image.png", image_data)

    def login_to_instagram(self):
        # AndroidUtilities.click_element(self.auto_controls.get_cancel())
        # AndroidUtilities.click_element(self.auto_controls.get_username())
        with open("./TestData/Images/tweet.png", 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        AppiumBase.driver.push_file("/storage/emulated/0/Pictures/Screenshots/image.png", image_data)
        pass

    def upload_image(self):
        AndroidUtilities.click_element(self.auto_controls.get_new_post())
        AndroidUtilities.click_element(self.auto_controls.get_image_1())
        AndroidUtilities.click_element(self.auto_controls.get_next())
        AndroidUtilities.click_element(self.auto_controls.get_next())
        AndroidUtilities.send_text_to_element(self.auto_controls.get_caption(), "First Post on Instagram from appium!! \n \n #automation #appium")
        AndroidUtilities.click_element(self.auto_controls.get_share())


    def click_views(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.auto_controls.view_tab)
        text = AndroidUtilities.get_text(self.auto_controls.get_view_tab())
        AssertUtilities.assert_equals(text, "Views")
        AndroidUtilities.click_element(self.auto_controls.get_view_tab())
        AndroidUtilities.take_screenshot('Test_confirm')
        Auto_Functions.log_file.info("Element clicked")

    def click_controls(self):
        WaitUtilities.wait_for_element_using_scroll_view("Controls")
        WaitUtilities.wait_for_element_to_be_clickable(self.auto_controls.control_tab)
        AndroidUtilities.is_element_displayed(self.auto_controls.get_controls_view())
        AndroidUtilities.click_element(self.auto_controls.get_controls_view())

    def click_checkbox(self):
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.light_theme_tab)
        AndroidUtilities.click_element(self.auto_controls.get_light_theme())
        WaitUtilities.wait_for_value_to_be_present(self.auto_controls.check_box, "Checkbox 1")
        AndroidUtilities.click_element(self.auto_controls.get_checkbox())

    def check_back_button(self):
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.light_theme_tab)
        AndroidUtilities.click_back_button()
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.control_tab)

    def check_drag_and_drop(self):
        WaitUtilities.wait_for_element_to_be_clickable(self.auto_controls.drag_and_drop)
        AndroidUtilities.click_element(self.auto_controls.get_drag_and_drop_tab())
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.source_element)
        AndroidUtilities.drag_and_drop(self.auto_controls.get_source_element(),self.auto_controls.get_target_element())
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.result_text)
        print("############Result Text #####", AndroidUtilities.get_text(self.auto_controls.get_result_text()))

    def check_scroll(self):
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.drag_and_drop)
        AndroidUtilities.scroll_to_text("TextSwitcher")
        AndroidUtilities.click_element(self.auto_controls.get_text_switcher())

    def check_tap(self):
        WaitUtilities.wait_element_to_be_visible(self.auto_controls.next_btn)
        AndroidUtilities.tap_element(self.auto_controls.get_next_btn())
