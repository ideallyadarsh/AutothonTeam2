from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Shell_FE_Appium_Core.AppiumBase import AppiumBase


class WaitUtilities:
    """WaitUtilities class contains reusable methods for common waits performed."""
    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def wait_for_element_by_description(locator, timeout=10):
        """Waits for the visiblity of the element by description
           :args:
               - locator - element to be checked
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_by_description(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % locator))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(locator,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_for_element_by_text(text_to_wait, timeout):
        """Waits for the visiblity of the element by text
           :args:text_of_value
             - locator - element to be checked
        """
        if text_to_wait is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_by_index(text_to_wait, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(
                lambda x: x.find_element_by_android_uiautomator('text("%s")' % text_to_wait))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(text_to_wait,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_for_element_using_scroll_view(text_of_value, timeout=10):
        """Wait untill it scrolls to the element
           :args:
                - text_of_value - text of the element to be checked
        """
        if text_of_value is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_by_index(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(lambda x: x.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().instance(0)).scrollIntoView(text("{0}"))'.format(text_of_value)))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(text_of_value,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_for_element_by_index(index_value, timeout=10):
        """Waits for the visiblity of the element by index
           :args:
              - locator - element to be checked
        """

        if index_value is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_by_index(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(index_value)))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(index_value,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_for_element_by_xpath(locator, timeout=10):
        """Waits for the visiblity of the element by xpath
           :args:
                - locator - element to be checked
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_by_xpath(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(lambda x: x.find_element_by_xpath('%s' % locator))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(locator,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_element_to_be_visible(locator, timeout=10):
        """Waits for element to be present and visible.
           :Args:
            - locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_to_be_visible(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not visible within the specified time. Exception: {1}".format(locator,
                                                                                              err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_clickable(locator, timeout=10):
        """Waits for element to be enabled.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_to_be_clickable(by_locator, "
                "timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as err:
            WaitUtilities.log.error(
                "Element {0} is not clickable. Unable to click / find the element within the specified time. "
                "Exception: {1}".format(
                    locator, err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_selected(locator, timeout=10):
        """Waits for element to be selected.

        :Args:
            - locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_to_be_selected(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(EC.element_to_be_selected(locator))
        except Exception as err:
            WaitUtilities.log.error(
                "Element was not in selected state within the specified time. Exception: {0}".format(
                    err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_invisible(locator, timeout=10):
        """Waits for element to be not present in the DOM.

        :Args:
            - locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
        """
        if locator is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_to_be_invisible(locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except Exception as err:
            WaitUtilities.log.error("Element {0} is visible. Exception: {1}".format(locator, err.__class__.__name__))

    @staticmethod
    def wait_for_value_to_be_present(locator, expected_text, timeout=10):
        """Waits for text to be present in the element's value attribute.

        :Args:
            - by_locator - The locator of the element to be checked.
            - expected_text - Value to be matched in element's value attribute.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
        """
        if locator is None or expected_text is None:
            WaitUtilities.log.error(
                "Empty or invalid value passed as argument to the method: wait_for_value_to_be_present(by_locator, "
                "expected_text, timeout=10).")
            raise TypeError("Empty or invalid argument passed!!")
        try:
            WebDriverWait(AppiumBase.driver, timeout).until(
                EC.text_to_be_present_in_element_value(locator, expected_text))

        except Exception as err:
            WaitUtilities.log.error(
                "Value {0} not present in element {1} within the expected time.".format(expected_text, locator))

    @staticmethod
    def implicit_wait(timeout=10):
        """Waits for the element till the time """
        AppiumBase.driver.implicitly_wait(timeout)
