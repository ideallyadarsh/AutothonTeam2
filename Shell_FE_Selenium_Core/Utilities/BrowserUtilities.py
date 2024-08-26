import os

from selenium.webdriver.common.alert import Alert
import time

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities


class BrowserUtilities:
    """BrowserUtilities class contains reusable methods for common browser related actions"""
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
            BrowserUtilities.log.error("Invalid or empty URL!!")
            raise Exception("Invalid or empty URL!!")
        SeleniumBase.driver.get(url)
        BrowserUtilities.log.info("Navigated to the URL: {0}.".format(url))

    @staticmethod
    def navigate_back():
        """Navigates back by one page."""
        SeleniumBase.driver.back()

    @staticmethod
    def navigate_forward():
        """Navigates forward by one page."""
        SeleniumBase.driver.forward()

    @staticmethod
    def refresh_page():
        """Refreshes the web page."""
        SeleniumBase.driver.refresh()
        BrowserUtilities.log.info("Page has been refreshed.")

    @staticmethod
    def get_current_url():
        """Returns the current url."""
        return SeleniumBase.driver.current_url

    @staticmethod
    def get_title():
        """Returns the current title."""
        return SeleniumBase.driver.title

    @staticmethod
    def maximize_window():
        """Maximizes the active browser window"""
        SeleniumBase.driver.maximize_window()

    @staticmethod
    def delete_cookies():
        """Deletes the cookies"""
        SeleniumBase.driver.delete_all_cookies()

    @staticmethod
    def switch_to_child_window():
        """Switches to the immediate child window."""
        child_window = SeleniumBase.driver.window_handles[1]
        SeleniumBase.driver.switch_to.window(child_window)
        BrowserUtilities.log.info("Switched to the child window: {0}.".format(child_window))

    @staticmethod
    def close_window():
        """Closes the driver instance (i.e.) the current browser tab / window."""
        SeleniumBase.driver.close()
        BrowserUtilities.log.info("Browser window has been closed.")

    @staticmethod
    def switch_to_parent_window():
        """Switches to the parent window."""
        parent_window = SeleniumBase.driver.window_handles[0]
        SeleniumBase.driver.switch_to.window(parent_window)
        BrowserUtilities.log.info("Switched to the parent window: {0}.".format(parent_window))

    @staticmethod
    def switch_to_window_by_title(expected_title):
        """Navigates through available windows and switches focus to window by the title.

        :Args:
            - expected_title - The title of the window to be matched.
        """
        if expected_title is None:
            BrowserUtilities.log.error("Empty argument passed to method switch_to_window_by_title(expected_title).")
            raise TypeError("Empty argument passed!!")
        if isinstance(expected_title, str) is False:
            BrowserUtilities.log.error(
                "String value should be passed to method switch_to_window_by_title(expected_title).")
            raise ValueError("Title should be a string value!!")
        parent_window = SeleniumBase.driver.current_window_handle
        window_handles = SeleniumBase.driver.window_handles
        if window_handles == 1:
            BrowserUtilities.log.error(
                "No child windows opened. Number of windows available is {0}.".format(window_handles))
        flag = False
        for window_handle in window_handles:
            SeleniumBase.driver.switch_to.window(window_handle)
            if SeleniumBase.driver.title == expected_title:
                flag = True
                BrowserUtilities.log.info("Switched to child window with the title: {0}.".format(expected_title))
                break
        if not flag:
            SeleniumBase.driver.switch_to.window(parent_window)
            BrowserUtilities.log.warning(
                "Could not find child window with the title {0}. Switched to Parent window {1}.".format(expected_title,
                                                                                                        parent_window))

    @staticmethod
    def switch_to_iframe(frame_value):
        """Switches to the frame.

        :Args:
            - frame_value - The value of frame (i.e.) frame name / index / locator.
        """
        if frame_value is None:
            BrowserUtilities.log.error("Empty or invalid argument passed in the method switch_to_iframe(rame_value).")
            raise TypeError("Empty or invalid argument passed!!")
        SeleniumBase.driver.switch_to.frame(frame_value)

    @staticmethod
    def exit_frame():
        """Switches to the default content from a frame."""
        SeleniumBase.driver.switch_to.parent_frame()

    @staticmethod
    def accept_alert():
        """Accepts the alert."""
        alert = Alert(SeleniumBase.driver)
        alert.accept()
        BrowserUtilities.log.info("Accepted the alert.")

    @staticmethod
    def dismiss_alert():
        """Dismisses the alert."""
        alert = Alert(SeleniumBase.driver)
        alert.dismiss()
        BrowserUtilities.log.info("Dismissed the alert.")

    @staticmethod
    def send_text_alert(text):
        """Sends text value to alert window.

        :Args:
            - text - The text to be sent to the alert window.
        """
        if text is None:
            BrowserUtilities.log.error("Empty argument passed in the method send_text_alert(text).")
            raise TypeError("Empty argument passed!!")
        alert = Alert(SeleniumBase.driver)
        alert.send_keys(str(text))
        BrowserUtilities.log.info("Sent the value {0} to the alert.".format(text))

    @staticmethod
    def get_alert_text():
        """Returns the text contained in alert"""
        alert = Alert(SeleniumBase.driver)
        return alert.text

    @staticmethod
    def take_screenshot_of_element(web_element, file_name="Element"):
        """
        Takes screenshot of the web element and saves it in the Screenshots folder under TestResults.
        :param web_element: Web element locator
        :param file_name: file name to be used to store web element screenshot
        :return:
        """
        if web_element is None:
            BrowserUtilities.log.error(
                "Empty or invalid argument passed to the method take_screenshot_of_element(web_element)")
            raise TypeError("Empty or invalid argument passed!!")
        filename = file_name + str(time.strftime("%d_%m_%H_%S")).replace("_", "") + ".png"
        web_element.screenshot(BrowserUtilities.screenshots + filename)
        BrowserUtilities.log.info("Took screenshot and saved as {0} in Screenshots folder.".format(filename))

    @staticmethod
    def take_screenshot(file_name="Screenshot"):
        """Takes screenshot of the web page and saves it in the Screenshots folder under TestResults."""
        filename = file_name + str(time.strftime("%d_%m_%H_%S")).replace("_", "") + ".png"
        SeleniumBase.driver.save_screenshot(BrowserUtilities.screenshots + filename)
        BrowserUtilities.log.info("Took screenshot and saved as {0} in Screenshots folder.".format(filename))

    @staticmethod
    def take_screenshot_base64():
        """Takes screenshot of the web page as base 64."""
        SeleniumBase.driver.get_screenshot_as_base64()

    @staticmethod
    def take_png_screenshot():
        """Takes screenshot of the web page as PNG."""
        SeleniumBase.driver.get_screenshot_as_png()

    @staticmethod
    def resize_browser(width, height):
        """Resize the browser based on the passed values.

        :Args:
            - width - The width of the browser to be set.
            - height - The height of the browser to be set.
        """
        if isinstance(width, int) is False or isinstance(height, int) is False:
            BrowserUtilities.log.error(
                "Width and Height passed to the method resize_browser(width, height) should be a number!!")
            raise ValueError("Width and Height should be a number!!")
        SeleniumBase.driver.set_window_size(width, height)
        BrowserUtilities.log.info("Browser size has been resized.")

    @staticmethod
    def switch_to_new_tab():
        """
        This method will open the new empty tab, which we can use it with current driver object
        """
        SeleniumBase.driver.switch_to.new_window('tab')

    @staticmethod
    def switch_to_new_window():
        """
        This method will open the new empty window, which we can use it with current driver object
        """
        SeleniumBase.driver.switch_to.new_window('window')
