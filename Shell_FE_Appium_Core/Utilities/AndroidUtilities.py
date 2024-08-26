import os
import time

from appium.webdriver import WebElement

from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


class AndroidUtilities:
    """AndroidUtilities class contains reusable methods for common Android functions used."""
    current_working_directory = os.path.dirname(os.getcwd())
    screenshots = current_working_directory + "/Shell_FE_Behave_Tests/TestResults/Screenshots/"
    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def navigate_to_url(url):
        """Navigates to the url specified.

        :Args:
            - url - The url to be navigated to.
        """
        if url is None:
            AndroidUtilities.log.error("Invalid or empty URL!!")
            raise Exception("Invalid or empty URL!!")
        AppiumBase.driver.get(url)
        AndroidUtilities.log.info("Navigated to the URL: {0}.".format(url))

    @staticmethod
    def click_element(element):
        """Clicks the Element.
            :Args:
                - web_element - The web element to be clicked.
         """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element(element)")
            raise TypeError("Empty or invalid  element passed!!")
        element.click()
        AndroidUtilities.log.info("Clicked on the element.")

    @staticmethod
    def send_text_to_element(element, text_to_be_added):
        """Passes the value to the text field
           :Args:
                - element - The element where value needs to be passed
                - text_to_be_add - The value to be passed to the text field. Value would be converted to string and passed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_to_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.send_keys(str(text_to_be_added))
        AndroidUtilities.log.info("Send text {0} to the element.".format(text_to_be_added))

    @staticmethod
    def clear_text(element):
        """Clears the text field
           :Args:
              -element - The element of the field to be cleared
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.clear()
        AndroidUtilities.log.info("Cleared the field")

    @staticmethod
    def get_attribute(element, attribute):
        """Return the value of the attribute
           :Args:
                -element - The element to get the value
                -attribute - The attribute value to be retrieved from the element
        """
        if element is None or attribute is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        if isinstance(attribute, str) is False:
            AndroidUtilities.log.error(
                "Attribute: {0} should be passed as a string value to the method: get_attribute(element, attribute)".format(
                    attribute))
            raise ValueError("Attribute should be a string value!!")
        return element.get_attribute(attribute)

    @staticmethod
    def get_text(element):
        """Return the value of the attribute
           :Args:
                -element - Value of the element to be retrieved
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        return element.text

    @staticmethod
    def get_title():
        """Returns the title of the current page"""
        return AppiumBase.driver.title

    @staticmethod
    def is_element_displayed(element):
        """Checks for the element is displayed
           :Args:
                      -element - The element to be checked
           :Returns:
                      - True if the element is displayed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_displayed(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_displayed():
            AndroidUtilities.log.info("Element displayed Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not displayed")
            return False

    @staticmethod
    def is_element_enabled(element):
        """Checks for the element is Enabled
        :Args:
             -element - The element to be checked
        :Returns:
             - True if the element is displayed
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_enabled(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_enabled():
            AndroidUtilities.log.info("Element Enabled Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not Enabled")
            return False

    @staticmethod
    def is_element_selected(element):
        """Checks for the element to select
        :Args:
             -element - The element to be selected
        :Returns:
             - True if the element is selected
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_selected(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_selected():
            AndroidUtilities.log.info("Element selected Successfully")
            return True
        else:
            AndroidUtilities.log.info("Element is not selected")
            return False

    @staticmethod
    def tap_element(element):
        """Tap on the element
        :args:
             - element - Locator of the element to be tapped
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: tap_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        actions = ActionChains(AppiumBase.driver)
        actions.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.click(element)
        actions.perform()

    @staticmethod
    def tap_element_by_coordinate(x_value, y_value):
        """Tap on the element using the cooridinates
           :args:
                 x : x coordinate to tap, relative to the top left corner of the element.
                 y : y coordinate. If y is used, x must also be set, and vice versa
        """
        if x_value is None or y_value is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: tap_element_by_coordinate(x,y)")
            raise TypeError("Empty or invalid element passed!!")
        # actions = TouchAction(AppiumBase.driver)
        # actions.tap(x=x_value, y=y_value).perform()
        AppiumBase.driver.tap([(x_value, y_value)])

    @staticmethod
    def long_press(element, duration=5):
        """Long press the element
           :args:
                -element - locator of the element to get long press
                -duration (optional) - by default it will press 1000 milliseconds
        """
        if element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: long_press(element)")
            raise TypeError("Empty or invalid element passed!!")
        actions = ActionChains(AppiumBase.driver)
        actions.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.click_and_hold(element).pause(duration).release()
        actions.perform()

    @staticmethod
    def drag_and_drop(source_element, target_element_location, wait=5):
        """Drag the element from source and drop it in the target location
           :args:
                -source_element - locator of the source element
                -target_element_location- locator of the target locatore
        """
        if source_element is None or target_element_location is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: drag_and_drop(source_element,"
                "target_element_location)")
            raise TypeError("Empty or invalid element passed!!")
        # actions = TouchAction(AppiumBase.driver)
        # actions.long_press(source_element).wait(wait).move_to(target_element_location).perform().release()
        AppiumBase.driver.drag_and_drop(origin_el=source_element, destination_el=target_element_location, pause=wait)

    @staticmethod
    def move_to_element(element_locator):
        """It scrolls to the element based on the co-ordinates
           :args:
               - -element - web element to scroll
        """
        if element_locator is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: move_to_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        previous_page_source = " "
        while not AndroidUtilities.is_end_of_page(previous_page_source):
            previous_page_source = AppiumBase.driver.page_source
            try:
                if AppiumBase.driver.find_element(*element_locator).is_displayed():
                    break
            except Exception as e:
                action = ActionChains(AppiumBase.driver)
                # window_size = AppiumBase.driver.get_window_size()
                # x, y = window_size['width'] / 6, window_size['height'] / 2
                window_size = AppiumBase.driver.get_window_size()

                screenWidth = window_size['width']
                screenHeight = window_size['height']

                startX = screenWidth / 2
                startY = screenHeight / 2

                endX = startX
                endY = screenHeight * 0.25

                action.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
                action.w3c_actions.pointer_action.move_to_location(startX, startY)
                action.w3c_actions.pointer_action.pointer_down()
                action.w3c_actions.pointer_action.move_to_location(endX, endY)
                action.w3c_actions.pointer_action.release()
                action.w3c_actions.perform()
                time.sleep(2)

    @staticmethod
    def scroll_once(scroll_direction):
        match scroll_direction.upper():
            case "UP":
                action = ActionChains(AppiumBase.driver)
                # window_size = AppiumBase.driver.get_window_size()
                # x, y = window_size['width'] / 6, window_size['height'] / 2
                window_size = AppiumBase.driver.get_window_size()

                screenWidth = window_size['width']
                screenHeight = window_size['height']

                startX = screenWidth / 2
                startY = screenHeight / 2

                endX = startX
                endY = screenHeight * 0.25
                action.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
                action.w3c_actions.pointer_action.move_to_location(startX, startY)
                action.w3c_actions.pointer_action.pointer_down()
                action.w3c_actions.pointer_action.move_to_location(endX, endY)
                action.w3c_actions.pointer_action.release()
                action.w3c_actions.perform()

            case "DOWN":
                action = ActionChains(AppiumBase.driver)
                # window_size = AppiumBase.driver.get_window_size()
                # x, y = window_size['width'] / 6, window_size['height'] / 2
                window_size = AppiumBase.driver.get_window_size()

                screenWidth = window_size['width']
                screenHeight = window_size['height']

                startX = screenWidth / 2
                startY = screenHeight / 2

                endX = startX
                endY = screenHeight * 0.25
                action.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
                action.w3c_actions.pointer_action.move_to_location(endX,endY)
                action.w3c_actions.pointer_action.pointer_down()
                action.w3c_actions.pointer_action.move_to_location(startX, startY)
                action.w3c_actions.pointer_action.release()
                action.w3c_actions.perform()

    @staticmethod
    def scroll_to_bottom():
        previous_page_source = " "
        while not AndroidUtilities.is_end_of_page(previous_page_source):
            previous_page_source = AppiumBase.driver.page_source
            action = ActionChains(AppiumBase.driver)
            # window_size = AppiumBase.driver.get_window_size()
            # x, y = window_size['width'] / 6, window_size['height'] / 2
            window_size = AppiumBase.driver.get_window_size()

            screenWidth = window_size['width']
            screenHeight = window_size['height']

            startX = screenWidth / 2
            startY = screenHeight / 2

            endX = startX
            endY = screenHeight * 0.25
            action.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            action.w3c_actions.pointer_action.move_to_location(startX, startY)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(endX, endY)
            action.w3c_actions.pointer_action.release()
            action.w3c_actions.perform()
            time.sleep(2)

    @staticmethod
    def scroll_to_top():
        previous_page_source = " "
        while not AndroidUtilities.is_end_of_page(previous_page_source):
            previous_page_source = AppiumBase.driver.page_source
            action = ActionChains(AppiumBase.driver)
            # window_size = AppiumBase.driver.get_window_size()
            # x, y = window_size['width'] / 6, window_size['height'] / 2
            window_size = AppiumBase.driver.get_window_size()

            screenWidth = window_size['width']
            screenHeight = window_size['height']

            startX = screenWidth / 2
            startY = screenHeight / 2

            endX = startX
            endY = screenHeight * 0.25
            action.w3c_actions = ActionBuilder(AppiumBase.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            action.w3c_actions.pointer_action.move_to_location(endX,endY)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(startX, startY)
            action.w3c_actions.pointer_action.release()
            action.w3c_actions.perform()
            time.sleep(2)

    @staticmethod
    def is_end_of_page(page_scource) -> bool:
        return page_scource == AppiumBase.driver.page_source
    @staticmethod
    def take_screenshot(screenshot_name):
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        time_format = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
        filename = screenshot_name + "_" + time_format + ".png"
        screenshot_path = AndroidUtilities.screenshots + filename
        AppiumBase.driver.save_screenshot(screenshot_path)
        AndroidUtilities.log.info("Took screenshot and saved as {0} in screenshots folder.".format(filename))

    @staticmethod
    def get_current_context():
        """It will get the current context of the App"""
        context = AppiumBase.driver.current_context
        AndroidUtilities.log.info("Current context of the is {0}.".format(context))
        return context

    @staticmethod
    def get_app_contexts():
        """It will get all the available contexts of the App"""
        contexts = AppiumBase.driver.contexts
        return contexts

    @staticmethod
    def switch_context(switch_view):
        """Switches the view of the app
            :args:
                 - switch_view- value of the app to be switched
        """
        if switch_view is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: switch_context(switch_view)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.switch_to.context(switch_view)

    @staticmethod
    def scroll_to_text(text_of_the_element):
        """Scroll to the element using text
           :args:
                - text_of_the_element - text of the element to be scrolled
        """
        if text_of_the_element is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: scroll_to_text(text_of_the_element)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().instance(0)).scrollIntoView(text("{0}"))'.format(
                text_of_the_element))

    @staticmethod
    def swipe(start_x, start_y, end_x, end_y, duration=None):
        """Swipe up,down,right,left in the application as per the co-ordinates
           :args:
               - start_x - x-coordinate at which to start
               - start_y - y-coordinate at which to start
               - end_x - x-coordinate at which to stop
               - end_y - y-coordinate at which to stop
               - duration - (optional) time to take the swipe, in ms.
        """
        AppiumBase.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    def open_pinch_gestures(element, percent):
        """performs pinch-open gesture on the given element
           :args:
                - element_id : locator of the element need to zoom
                - percent : How much percent to zoon
        """
        AppiumBase.driver.execute_script('mobile: pinchOpenGesture', {
            'elementId': element,
            'percent': percent
        })

    @staticmethod
    def close_pinch_gestures(element, percent):
        """performs pinch-close gesture on the given element
           :args:
                - element_id : locator of the element need to zoom
                - percent : How much percent to zoom
        """
        AppiumBase.driver.execute_script('mobile: pinchCloseGesture', {
            'elementId': element,
            'percent': percent
        })

    @staticmethod
    def get_window_size():
        """Returns the size of the window"""
        return AppiumBase.driver.get_window_size()

    @staticmethod
    def get_current_window_size(current_window):
        """Returns the size of the specified window
           :args:
                - current_window- pass the window name to get the widow_size
        """
        return AppiumBase.driver.get_window_size(current_window)

    @staticmethod
    def set_device_orientation(orientation_type):
        """It will set the orientation of the current device/browser
           :args:
                - orientation_type - orientation type of the device
        """
        if orientation_type is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: set_device_orientation("
                "orientation_type)")
            raise TypeError("Empty or invalid element passed!!")
        device_orientation = orientation_type.upper()
        AppiumBase.driver.orientation = device_orientation

    @staticmethod
    def get_device_orientation():
        """Get the current device/browser orientation"""
        return AppiumBase.driver.orientation

    @staticmethod
    def press_keycode(key_value):
        """Press the mobile key for the corresponding value
           :args:
               -key_value - Pass the integer value to be pressed
        """
        if key_value is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: press_keycode(key_value)")
            raise TypeError("Empty or invalid element passed!!")
        element = AppiumBase.driver.press_keycode(key_value)
        AndroidUtilities.log.info("key has been pressed")
        return element

    @staticmethod
    def start_activity(package_name, activity_name):
        """Start an Android activity
           :args:
                - package_name - provide the package name of the app
                - activity_name - provide the activity name of the app
        """
        if package_name is None or activity_name is None:
            AndroidUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: start_activity(package_name,"
                "activity_name)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.start_activity(package_name, activity_name)

    @staticmethod
    def get_current_activity():
        """Get the name of the current Android activity"""
        return AppiumBase.driver.current_activity

    @staticmethod
    def get_current_package():
        """Get the name of the current Android package"""
        return AppiumBase.driver.current_package

    @staticmethod
    def click_back_button():
        """Press the mobile application back button"""
        AppiumBase.driver.back()
