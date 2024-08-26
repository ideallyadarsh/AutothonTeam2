import traceback

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    StaleElementReferenceException, NoSuchFrameException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities


class WaitUtilities:
    """WaitUtilities class contains reusable methods for common waits performed."""

    logobj = LoggingUtilities()
    log = logobj.logger()

    @staticmethod
    def wait_for_element_to_be_visible(by_locator, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to be present in DOM and visible.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_visible""(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.visibility_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is not visible within the specified time. "
                                        "Exception: {1}".format(by_locator, err.__class__.__name__))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.visibility_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is not visible within the specified time. "
                                        "Exception: {1}".format(by_locator, err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_present(by_locator, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to be present in DOM.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_present(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.presence_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is not present. Unable to find the element within the specified "
                                        "time. Exception: {1}".format(by_locator, err.__class__.__name__))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.presence_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is not present. Unable to find the element within the "
                                        "specified time. Exception: {1}".format(by_locator, err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_clickable(by_locator, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to be enabled.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_clickable(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.element_to_be_clickable(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is not clickable. Unable to click / find the element within the "
                                        "specified time. Exception: {1}".format(by_locator, err.__class__.__name__))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.element_to_be_clickable(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Frame {0} is not available within the specified time.".format(by_locator))

    @staticmethod
    def wait_for_element_to_be_selected(web_element, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to be selected.

        :Args:
            - web_element - The element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if web_element is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_selected(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.element_to_be_selected(web_element))
            except Exception as err:
                WaitUtilities.log.error("Element was not in selected state within the specified time. "
                                        "Exception: {0}".format(err.__class__.__name__))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.element_to_be_selected(web_element))
            except Exception as err:
                WaitUtilities.log.error("Element was not in selected state within the specified time. "
                                        "Exception: {0}".format(err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_invisible(by_locator, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to be not present in the DOM.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_invisible(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.invisibility_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is visible. Exception: {1}".format(by_locator,
                                                                                        err.__class__.__name__))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.invisibility_of_element_located(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Element {0} is visible. Exception: {1}".format(by_locator,
                                                                                        err.__class__.__name__))

    @staticmethod
    def wait_for_element_to_be_stale(web_element, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for element to become stale.

        :Args:
            - web_element - The element to be checked for staleness.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if web_element is None:
            WaitUtilities.log.error(
                "Empty or invalid locator passed to the method: wait_for_element_to_be_stale(web_element, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            if WebDriverWait(SeleniumBase.driver, timeout).until(ec.staleness_of(web_element)):
                return True
            else:
                WaitUtilities.log.error("Element {0} is attached to DOM. Element is not stale!!".format(web_element))
                # raise Exception("Element {0} is attached to DOM. Element is not stale!!".format(web_element))
        elif fluent == "true":
            if WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                             ignored_exceptions=[ign_exception]).until(ec.staleness_of(web_element)):
                return True
            else:
                WaitUtilities.log.error("Element {0} is attached to DOM. Element is not stale!!".format(web_element))

    @staticmethod
    def wait_for_element_to_be_stale_and_handle_it(web_element, by_locator, timeout=10, poll_freq=2,
                                                   ign_exception=None, fluent=None):
        """Waits for a stale element to be visible within the specified time.

        :Args:
            - web_element - The element to be checked for staleness.
            - by_locator - The locator of the element to be checked for visibility.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if web_element is None or by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed to the method: "
                                    "wait_for_element_to_be_stale_and_handle_it(web_element, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                if WebDriverWait(SeleniumBase.driver, timeout).until(ec.staleness_of(web_element)):
                    WebDriverWait(SeleniumBase.driver, timeout).until(ec.visibility_of_element_located(by_locator))
            except StaleElementReferenceException as err:
                WaitUtilities.log.error("Element {0} is not attached to DOM. Element is stale!! "
                                        "Exception: {1}".format(by_locator, err.__class__.__name__))
        elif fluent == "true":
            try:
                if WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                                 ignored_exceptions=[ign_exception]).until(ec.staleness_of(web_element)):
                    WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                                  ignored_exceptions=[ign_exception]).until(ec.visibility_of_element_located(by_locator))
            except StaleElementReferenceException as err:
                WaitUtilities.log.error("Element {0} is not attached to DOM. Element is stale!! "
                                        "Exception: {1}".format(by_locator, err.__class__.__name__))

    @staticmethod
    def wait_for_title_to_contain_value(expected_value, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for the title to contain the expected value.

        :Args:
            - expected_value - Expected value to be contained in title.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if expected_value is None:
            WaitUtilities.log.error("Empty or invalid title passed as argument to the method: "
                                    "wait_for_title_to_contain_value(expected_value, timeout=10).")
            raise ValueError("Empty or invalid Title passed as argument!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.title_contains(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Title does not contain the value: {0} in the "
                                        "expected time.".format(expected_value))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.title_contains(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Title does not contain the value: {0} in the "
                                        "expected time.".format(expected_value))

    @staticmethod
    def wait_for_title_to_match_value(expected_value, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for the title to match the expected value.

        :Args:
            - expected_value - Expected value to be matched against title.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if expected_value is None:
            WaitUtilities.log.error("Empty or invalid title passed as argument to the method: "
                                    "wait_for_title_to_match_value(expected_value, timeout=10).")
            raise ValueError("Empty or invalid Title passed as argument!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.title_is(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Title does not match the value: {0} "
                                        "within the specified time.".format(expected_value))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.title_is(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Title does not match the value: {0} "
                                        "within the specified time.".format(expected_value))

    @staticmethod
    def wait_for_url_to_contain_value(expected_value, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for the url to contain the expected value.

        :Args:
            - expected_value - Expected value to be contained in url.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if expected_value is None:
            WaitUtilities.log.error("Empty or invalid url passed as argument to the method: "
                                    "wait_for_url_to_contain_value(expected_value, timeout=10).")
            raise ValueError("Empty or invalid value passed as argument!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.url_contains(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Url does not contain the value: {0} in the "
                                        "expected time.".format(expected_value))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.url_contains(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Url does not contain the value: {0} in the "
                                        "expected time.".format(expected_value))

    @staticmethod
    def wait_for_url_to_match_value(expected_value, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for the url to match the expected value.

        :Args:
            - expected_value - Expected value to be matched against url.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if expected_value is None:
            WaitUtilities.log.error("Empty or invalid url passed as argument to the method: "
                                    "wait_for_url_to_match_value(expected_value, timeout=10).")
            raise ValueError("Empty or invalid Title passed as argument!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.url_to_be(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Url does not match the value: {0} in the "
                                        "expected time.".format(expected_value))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.url_to_be(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Url does not match the value: {0} in the "
                                        "expected time.".format(expected_value))

    @staticmethod
    def wait_for_text_to_be_present(by_locator, expected_text, timeout=10, poll_freq=2, ign_exception=None,
                                    fluent=None):
        """Waits for value to be present in the element's text.

        :Args:
            - by_locator - The locator of the element to be checked.
            - expected_text - Value to be matched in element's text.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None or expected_text is None:
            WaitUtilities.log.error("Empty or invalid value passed as argument to the method: "
                                    "wait_for_text_to_be_present(by_locator, expected_text, timeout=10).")
            raise TypeError("Empty or invalid argument passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(
                    ec.text_to_be_present_in_element(by_locator, expected_text))
            except Exception as err:
                WaitUtilities.log.error("Text {0} not present in element {1} "
                                        "within the expected time.".format(expected_text, by_locator))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.text_to_be_present_in_element(by_locator,
                                                                                                         expected_text))
            except Exception as err:
                WaitUtilities.log.error("Text {0} not present in element {1} "
                                        "within the expected time.".format(expected_text, by_locator))

    @staticmethod
    def wait_for_value_to_be_present(by_locator, expected_text, timeout=10, poll_freq=2, ign_exception=None,
                                     fluent=None):
        """Waits for text to be present in the element's value attribute.

        :Args:
            - by_locator - The locator of the element to be checked.
            - expected_text - Value to be matched in element's value attribute.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None or expected_text is None:
            WaitUtilities.log.error("Empty or invalid value passed as argument to the method: "
                                    "wait_for_value_to_be_present(by_locator, expected_text, timeout=10).")
            raise TypeError("Empty or invalid argument passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(
                    ec.text_to_be_present_in_element_value(by_locator, expected_text))
            except Exception as err:
                WaitUtilities.log.error("Value {0} not present in element {1} "
                                        "within the expected time.".format(expected_text, by_locator))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.text_to_be_present_in_element_value
                                                                                        (by_locator, expected_text))
            except Exception as err:
                WaitUtilities.log.error("Value {0} not present in element {1} "
                                        "within the expected time.".format(expected_text, by_locator))

    @staticmethod
    def wait_for_number_of_windows_to_match(expected_value, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for the number of windows to match the expected value.

        :Args:
            - expected_value - Expected number of windows.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if expected_value is None:
            WaitUtilities.log.error("Empty or invalid value passed as argument to the method: "
                                    "wait_for_number_of_windows_to_match(expected_value, timeout=10).")
            raise TypeError("Empty or invalid value passed!!")
        elif isinstance(expected_value, int) is False:
            WaitUtilities.log.error("Invalid argument passed to the method: "
                                    "wait_for_number_of_windows_to_match(expected_value, timeout=10). "
                                    "Argument should be an int.")
            raise ValueError("Number of windows value should be a number")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.number_of_windows_to_be(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Number of windows available does not match the expected value: "
                                        "{0} within the expected time".format(expected_value))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.number_of_windows_to_be(expected_value))
            except Exception as err:
                WaitUtilities.log.error("Number of windows available does not match the expected value: "
                                        "{0} within the expected time".format(expected_value))

    @staticmethod
    def wait_for_alert_to_be_present(timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for alert to be present.

        :Args:
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.alert_is_present())
            except Exception as err:
                WaitUtilities.log.error("Alert is not displayed within the expected time!!")
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).until(ec.alert_is_present())
            except Exception as err:
                WaitUtilities.log.error("Alert is not displayed within the expected time!!")

    @staticmethod
    def wait_for_frame_and_switch(by_locator, timeout=10, poll_freq=2, ign_exception=None, fluent=None):
        """Waits for frame to be available.

        :Args:
            - by_locator - The locator of the element to be checked.
            - timeout - Time to wait for before throwing an exception. Has a default value of 10 seconds.
            - poll_freq - Polling Frequency, frequency with which to check the condition. Default is 2 seconds
            - ign_exception - ignore specific types of exceptions whilst waiting. Default is None.
            - fluent - Condition to decide on custom waits. Default is None.
        """
        if by_locator is None:
            WaitUtilities.log.error("Empty or invalid locator passed as argument to the method: "
                                    "wait_for_frame_and_switch(by_locator, timeout=10).")
            raise TypeError("Empty or invalid locator passed!!")
        elif fluent is None or "false":
            try:
                WebDriverWait(SeleniumBase.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Frame {0} is not available within the specified time.".format(by_locator))
        elif fluent == "true":
            try:
                WebDriverWait(SeleniumBase.driver, timeout=timeout, poll_frequency=poll_freq,
                              ignored_exceptions=[ign_exception]).\
                    until(ec.frame_to_be_available_and_switch_to_it(by_locator))
            except Exception as err:
                WaitUtilities.log.error("Frame {0} is not available within the specified time.".format(by_locator))
