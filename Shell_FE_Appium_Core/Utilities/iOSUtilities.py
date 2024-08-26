import os
import time

from appium.webdriver.common.touch_action import TouchAction

from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities


class IOSUtilities:
    """iOSUtilities class contains reusable methods for common Android functions used."""

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
            IOSUtilities.log.error("Invalid or empty URL!!")
            raise Exception("Invalid or empty URL!!")
        AppiumBase.driver.get(url)
        IOSUtilities.log.info("Navigated to the URL: {0}.".format(url))

    @staticmethod
    def click_element(element):
        """Clicks the Element.
            :Args:
                - web_element - The web element to be clicked.
         """
        if element is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element(element)")
            raise TypeError("Empty or invalid  element passed!!")
        element.click()
        IOSUtilities.log.info("Clicked on the element.")

    @staticmethod
    def send_text_to_element(element, text_to_be_added):
        """Passes the value to the text field
           :Args:
                - element - The element where value needs to be passed
                - text_to_be_add - The value to be passed to the text field. Value would be converted to string and passed
        """
        if element is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_to_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.send_keys(str(text_to_be_added))
        IOSUtilities.log.info("Send text {0} to the element.".format(text_to_be_added))

    @staticmethod
    def clear_text(element):
        """Clears the text field
           :Args:
              -element - The element of the field to be cleared
        """
        if element is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text(element)")
            raise TypeError("Empty or invalid element passed!!")
        element.clear()
        IOSUtilities.log.info("Cleared the field")

    @staticmethod
    def get_attribute(element, attribute):
        """Return the value of the attribute
           :Args:
                -element - The element to get the value
                -attribute - The attribute value to be retrieved from the element
        """
        if element is None or attribute is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        if isinstance(attribute, str) is False:
            IOSUtilities.log.error(
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
            IOSUtilities.log.error(
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
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_displayed(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_displayed():
            IOSUtilities.log.info("Element displayed Successfully")
            return True
        else:
            IOSUtilities.log.info("Element is not displayed")
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
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_enabled(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_enabled():
            IOSUtilities.log.info("Element Enabled Successfully")
            return True
        else:
            IOSUtilities.log.info("Element is not Enabled")
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
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_selected(element)")
            raise TypeError("Empty or invalid element passed!!")
        if element.is_selected():
            IOSUtilities.log.info("Element selected Successfully")
            return True
        else:
            IOSUtilities.log.info("Element is not selected")
            return False

    @staticmethod
    def tap_element(element):
        """Tap on the element
        :args:
             - element - Locator of the element to be tapped
        """
        if element is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: tap_element(element)")
            raise TypeError("Empty or invalid element passed!!")
        actions = TouchAction(AppiumBase.driver)
        actions.tap(element).perform()

    @staticmethod
    def tap_element_by_coordinate(x_value, y_value):
        """Tap on the element using the cooridinates
           :args:
                 x : x coordinate to tap, relative to the top left corner of the element.
                 y : y coordinate. If y is used, x must also be set, and vice versa
        """
        if x_value is None or y_value is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: tap_element_by_coordinate(x,y)")
            raise TypeError("Empty or invalid element passed!!")
        actions = TouchAction(AppiumBase.driver)
        actions.tap(x=x_value, y=y_value).perform()

    @staticmethod
    def long_press(element, duration=1000):
        """Long press the element
           :args:
                -element - locator of the element to get long press
                -duration (optional) - by default it will press 1000 milliseconds
        """
        if element is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: long_press(element)")
            raise TypeError("Empty or invalid element passed!!")
        actions = TouchAction(AppiumBase.driver)
        actions.long_press(element, duration).perform()

    @staticmethod
    def drag_and_drop(source_element, target_element_location, wait=1000):
        """Drag the element from source and drop it in the target location
           :args:
                -source_element - locator of the source element
                -target_element_location- locator of the target locatore
        """
        if source_element is None or target_element_location is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: drag_and_drop(source_element,"
                "target_element_location)")
            raise TypeError("Empty or invalid element passed!!")
        actions = TouchAction(AppiumBase.driver)
        actions.long_press(source_element).wait(wait).move_to(target_element_location).perform().release()

    @staticmethod
    def move_to_element(start_x, start_y, end_x, end_y):
        """It scrolls to the element based on the co-ordinates
           :args:
               - start_x - co-ordinate of starting x-axis
               - start_y - co-ordinate of starting y-axis
               - end_x   - co-ordinate of the end x-axis
               - end_y    - co-ordinate of the end y-axis
        """
        if start_x is None or start_y is None or end_x is None or end_y is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: move_to_element(start_x,start_y,"
                "end_x,end_y)")
            raise TypeError("Empty or invalid element passed!!")
        actions = TouchAction(AppiumBase.driver)
        actions.press(start_x, start_y).wait(2000).move_to(end_x, end_y).perform()

    @staticmethod
    def take_screenshot(screenshot_name):
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        time_format = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
        filename = screenshot_name + "_" + time_format + ".png"
        screenshot_path = IOSUtilities.screenshots + filename
        AppiumBase.driver.save_screenshot(screenshot_path)
        IOSUtilities.log.info("Took screenshot and saved as {0} in screenshots folder.".format(filename))

    @staticmethod
    def get_current_context():
        """It will get the current context of the App"""
        context = AppiumBase.driver.current_context
        IOSUtilities.log.info("Current context of the is {0}.".format(context))
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
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: switch_context(switch_view)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.switch_to.context(switch_view)

    @staticmethod
    def scroll_to_text(text_of_the_element,direction):
        """Scroll to the element using text
           :args:
                - text_of_the_element - text of the element to be scrolled
                - direction - Direction should be up or down
        """
        if text_of_the_element is None or direction is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: scroll_to_text(text_of_the_element)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.execute_script('mobile: scroll', {'name': text_of_the_element, 'direction': direction})


    @staticmethod
    def scroll_picker_wheel(element_id,movement_order, offset=None):
        """Scroll the picker wheel
           :args:
                - element_id - id of the element
                - movement_oder - it should be either previous or next
                - offset -The value in range [0.01, 0.5].It defines how far from picker wheel's center the click should happen
        """
        if element_id is None or movement_order is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: scroll_picker_wheel(element_id,"
                "movement_order)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.execute_script('mobile: selectPickerWheelValue', {'elementId': element_id, 'order': movement_order , 'offset': offset})


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
        """Returns the size of the specified window in the browser
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
            IOSUtilities.log.error(
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
    def click_back_button():
        """Press the mobile application back button"""
        AppiumBase.driver.back()

    @staticmethod
    def activate_app(bundle_id):
        """Start an iOS activity
           :args:
                - package_name - provide the package name of the app
                - activity_name - provide the activity name of the app
        """
        if bundle_id is None:
            IOSUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: start_activity(package_name,"
                "activity_name)")
            raise TypeError("Empty or invalid element passed!!")
        AppiumBase.driver.activate_app(bundle_id)

    @staticmethod
    def run_app_in_background(duration=-1):
        """Runs the apps in the background
           :args:
            - duration: It holds the app in background for teh specified duration.
              By default duration is set to -1 which means app will be on background until we start the app
        """
        AppiumBase.driver.background_app(duration)

    @staticmethod
    def app_status(bundle_id):
        """Get the status of the app
        :args:
             - bundle_id - bundleId of the application needs to get the status
        :returns:(number)
              0 is not installed.
              1 is not running.
              2 is running in background or suspended.
              3 is running in background.
              4 is running in foreground.
        """
        return AppiumBase.driver.query_app_state(bundle_id)

    @staticmethod
    def shake():
        """Performs Shake operation"""
        AppiumBase.driver.shake()

    @staticmethod
    def lock_device(duration_in_seconds=None):
        """It locks the device for the particular duration
           :args:
              - duration_in_seconds - duration of the device to be locked. By default lock duration is not set
        """
        AppiumBase.driver.lock(duration_in_seconds)

    @staticmethod
    def unlock_device():
        """It unlocks the device"""
        AppiumBase.driver.unlock()

    @staticmethod
    def check_lock_status():
        """Used to check the device is locked or not
           :Returns:
              - True - If the device is locked
              - Falese -If the device is not locked
        """
        return AppiumBase.driver.is_locked()

    @staticmethod
    def show_device_time():
        """Returns the device time in String"""
        return AppiumBase.driver.get_device_time()







