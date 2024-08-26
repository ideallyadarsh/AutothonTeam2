import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.select import Select
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities


class SeleniumUtilities:
    """SeleniumUtilities class contains reusable methods for common Selenium user actions"""

    logobj = LoggingUtilities()
    log = logobj.logger()

    # region Reusable methods for performing common user actions in Selenium
    @staticmethod
    def click_element(web_element):
        """Clicks the Element.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error("Empty or invalid Web element passed as argument to the method: click_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.click()
        SeleniumUtilities.log.info("Clicked on the element.")

    @staticmethod
    def send_text(web_element, text):
        """Passes the value to the text field.

            Args:
                - web_element - The web element where value needs to be passed.
                - text - The value to be passed to text field. Value would be converted to string and passed.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text(web_element, text)")
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.send_keys(str(text))
        SeleniumUtilities.log.info("Sent text {0} to the element.".format(text))

    @staticmethod
    def clear_text(web_element):
        """Clears the text field.

        :Args:
            - web_element - The web element of the field to be cleared.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        web_element.clear()
        SeleniumUtilities.log.info("Cleared the field")

    @staticmethod
    def is_element_selected(web_element):
        """Verifies if the element is selected.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is selected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_selected(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_selected():
            SeleniumUtilities.log.info("Element is selected.")
            return True
        else:
            SeleniumUtilities.log.info("Element is not selected.")
            return False

    @staticmethod
    def is_element_displayed(web_element):
        """Verifies if the element is visible.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is visible.
        """
        if web_element is None:
            SeleniumUtilities.log.error("Empty or invalid Web element passed to method is_element_displayed(web_element).")
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_displayed():
            SeleniumUtilities.log.info("Element is displayed.")
            return True
        else:
            SeleniumUtilities.log.info("Element is not displayed.")
            return False

    @staticmethod
    def is_element_enabled(web_element):
        """Verifies if the element is enabled.

        :Args:
            - web_element - The web element to be checked.

        :Returns:
            - True if element is enabled.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: is_element_enabled(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if web_element.is_enabled():
            SeleniumUtilities.log.info("Element is enabled.")
            return True
        else:
            SeleniumUtilities.log.info("Element is not enabled.")
            return False

    @staticmethod
    def select_from_dropdown_using_value(web_element, value):
        """Selects option from dropdown using value.

        :Args:
            - web_element - The web element of the dropdown to be clicked.
            - value - The value of the option to be selected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: select_from_dropdown_using_value(web_element, value)")
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        select.select_by_value(value)
        SeleniumUtilities.log.info("Value {0} selected from dropdown using value.".format(value))

    @staticmethod
    def select_from_dropdown_using_visible_text(web_element, value):
        """Selects option from dropdown using visible text.

        :Args:
            - web_element - The web element of the dropdown to be clicked.
            - value - The visible text of the option to be selected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: select_from_dropdown_using_visible_text(web_element, value)")
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        select.select_by_visible_text(value)
        SeleniumUtilities.log.info("Value {0} selected from dropdown using visible text.".format(value))

    @staticmethod
    def get_selected_element_from_dropdown(web_element):
        """Retrieves the selected element from dropdown.

        :Args:
            - web_element - The web element of the dropdown to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_selected_element_from_dropdown(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        SeleniumUtilities.log.info("Selected webelement is returned from the dropdown.")
        return select.first_selected_option

    @staticmethod
    def get_selected_element_text_from_dropdown(web_element):
        """Retrieves the selected element from dropdown.

        :Args:
            - web_element - The web element of the dropdown to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_selected_element_text_from_dropdown(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        select = Select(web_element)
        SeleniumUtilities.log.info("Selected webelement's text {0} is returned from the dropdown.".format(select.first_selected_option.text))
        return select.first_selected_option.text

    @staticmethod
    def select_checkbox(web_element):
        """Selects the checkbox if it is already unchecked.

        :Args:
            - web_element - The web element of the checkbox to be selected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: select_checkbox(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if not SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)
            SeleniumUtilities.log.info("Checkbox has been selected.")

    @staticmethod
    def unselect_checkbox(web_element):
        """Unselects the checkbox if it is already checked.

        :Args:
            - web_element - The web element of the checkbox to be unselected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: unselect_checkbox(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)
            SeleniumUtilities.log.info("Checkbox has been unselected.")

    @staticmethod
    def select_radiobutton(web_element):
        """Selects the radio button if it is unselected.

        :Args:
            - web_element - The web element of the radio button to be selected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: select_radiobutton(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if not SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)
            SeleniumUtilities.log.info("Radio button has been selected.")

    @staticmethod
    def deselect_radiobutton(web_element):
        """Unselects the radio button if it is selected.

        :Args:
            - web_element - The web element of the radio button to be unselected.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: deselect_radiobutton(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        if SeleniumUtilities.is_element_selected(web_element):
            SeleniumUtilities.click_element(web_element)
            SeleniumUtilities.log.info("Radio button has been unselected.")

    @staticmethod
    def get_text(web_element):
        """Retrieves the inner text of the text field.

        :Args:
            - web_element - The web element of the text field whose text needs to be retrieved.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_text(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumUtilities.log.info("The text {0} has been retrieved from the element.".format(web_element.text))
        return web_element.text

    @staticmethod
    def get_attribute(web_element, attr):
        """Retrieves the required attribute's value of element.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
        """
        if web_element is None or attr is None:
            SeleniumUtilities.log.error(
                "Empty or invalid argument passed to the method: get_attribute(web_element, attr)")
            raise TypeError("Empty or invalid argument passed!!")
        if isinstance(attr, str) is False:
            SeleniumUtilities.log.error(
                "Attribute: {0} should be passed as a string value to the method: get_attribute(web_element, attr)".format(attr))
            raise ValueError("Attribute should be a string value!!")
        SeleniumUtilities.log.info("The text {0} has been retrieved from the element.".format(web_element.text))
        return web_element.get_attribute(attr)

    @staticmethod
    def get_css(web_element, css_property):
        """Retrieves the required attribute's value of element.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
        """
        if web_element is None or css_property is None:
            SeleniumUtilities.log.error(
                "Empty or invalid argument passed to the method: get_css(web_element, css_property)")
            raise TypeError("Empty or invalid argument passed!!")
        if isinstance(css_property, str) is False:
            SeleniumUtilities.log.error(
                "Css property: {0} should be passed as a string value to the method: get_css(web_element, css_property)".format(
                    css_property))
            raise ValueError("Attribute should be a string value!!")
        css_value = web_element.value_of_css_property(css_property)
        SeleniumUtilities.log.info("The {0} property of the web element has been retrieved: {1}.".format(css_property, css_value))
        return css_value

    # endregion

    # region Reusable methods for user actions performed using ActionChains
    @staticmethod
    def move_focus_to_element(web_element):
        """Moves the focus to element using Actions.

        :Args:
            - web_element - The web element to be interacted.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: move_focus_to_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).perform()
        SeleniumUtilities.log.info("Moved focus to element using Action chains.")

    @staticmethod
    def click_element_by_actions(web_element):
        """Clicks the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element_by_actions(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.click(web_element).perform()
        SeleniumUtilities.log.info("Clicked on element using Action chains.")

    @staticmethod
    def send_text_by_actions(web_element, text):
        """Sends text to the element using Actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_by_actions(web_element, text)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.send_keys_to_element(web_element, str(text)).perform()
        SeleniumUtilities.log.info("Sent text {0} to the element using Action Chains.".format(text))

    @staticmethod
    def send_text_to_focused_element_by_actions(text):
        """Sends text to the element using Actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if text is None:
            SeleniumUtilities.log.error(
                "No text present")
            raise TypeError("Empty text")
        action = ActionChains(SeleniumBase.driver)
        action.send_keys(str(text)).perform()
        SeleniumUtilities.log.info("Sent text {0} to the element using Action Chains.".format(text))

    @staticmethod
    def drag_drop_element_by_coordinates(web_element, x_offset, y_offset):
        """Drags and drops an element via coordinates using Actions.

        :Args:
            - web_element - The web element to be moved.
            - x-offset - The x-axis value
            - y-offset - The y-axis value
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: drag_drop_element_by_coordinates(web_element, x_offset, y_offset)")
            raise TypeError("Empty or invalid Web element passed!!")
        if isinstance(x_offset, int) is False or isinstance(y_offset, int) is False:
            raise ValueError("Integer value should be passed as offset!!")
        action = ActionChains(SeleniumBase.driver)
        action.drag_and_drop_by_offset(web_element, x_offset, y_offset).perform()
        SeleniumUtilities.log.info("Dragged and dropped the web element to the position {0}, {1}.".format(x_offset, y_offset))

    @staticmethod
    def drag_drop_element(source_web_element, target_web_element):
        """Drags and drops an element to new location using Actions.

        :Args:
            - source_web_element - The web element to be moved.
            - target_web_element - The web element of the target location
        """
        if source_web_element is None or target_web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: drag_drop_element(source_web_element, target_web_element)")
            raise TypeError("Empty or invalid argument passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.drag_and_drop(source_web_element, target_web_element).perform()
        SeleniumUtilities.log.info("Dragged the source web element to target web element.")

    @staticmethod
    def double_click(web_element):
        """Performs mouse double click on the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: double_click(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.double_click(web_element).perform()
        SeleniumUtilities.log.info("Performed double click on the element using Action chains.")

    @staticmethod
    def right_click(web_element):
        """Performs mouse right-click on the element using Actions.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: right_click(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.context_click(web_element).perform()
        SeleniumUtilities.log.info("Performed right click on the element using Action chains.")

    @staticmethod
    def clear_text_using_keys(web_element):
        """Clears the contents of element.

        :Args:
            - web_element - The web element to be cleared.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text_using_keys(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        SeleniumUtilities.log.info("Cleared value in the field using key actions.")

    @staticmethod
    def click_and_hold_an_element(web_element):
        """Click and holds a web element.

        :Args:
            - web_element - The web element to be clicked and hold.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: clear_text_using_keys(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.click_and_hold(web_element).perform()
        SeleniumUtilities.log.info(f"Clicked and hold a web element {web_element}.")

    @staticmethod
    def scroll_to_element_by_actions(web_element):
        """Scrolls the webpage until the element is displayed by actions class.

        :Args:
            - web_element - The web element up to which the web page needs to be scrolled.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: scroll_to_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.scroll_to_element(web_element).perform()
        # SeleniumBase.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        SeleniumUtilities.log.info("Scrolled to the web element using Javascript executor.")

    @staticmethod
    def scroll_by_amount_actions(delta_x, delta_y):
        """Scrolls the webpage by x and y co-ordinates.

        :Args:
            - delta_x - x co-ordinate by which the web page needs to be scrolled.
            - delta_y - y co-ordinate by which the web page needs to be scrolled.
        """
        action = ActionChains(SeleniumBase.driver)
        action.scroll_by_amount(delta_x, delta_y).perform()
        SeleniumUtilities.log.info(f"Scrolled the web page by x {delta_x} and y {delta_y} using action class.")

    @staticmethod
    def scroll_from_an_element_by_a_given_amount_by_actions(scroll_origin, delta_x, delta_y):
        """
        Scrolls by provided amount based on a provided origin. The scroll origin is either the center of an element
        or the upper left of the viewport plus any offsets. If the origin is an element, and the element is not in
        the viewport, the bottom of the element will first be scrolled to the bottom of the viewport.

           :Args:
            - scroll_origin - scroll origin is either the center of an element or the upper left of the viewport plus any offsets
            - delta_x - x co-ordinate by which the web page needs to be scrolled.
            - delta_y - y co-ordinate by which the web page needs to be scrolled.
        """

        if scroll_origin is None:
            SeleniumUtilities.log.error(
                "Empty or invalid argument to the method: scroll_from_an_element_by_a_given_amount_by_actions("
                "scroll_origin)")
            raise TypeError("Empty or invalid argument  passed to the method!!")
        action = ActionChains(SeleniumBase.driver)
        action.scroll_from_origin(scroll_origin, delta_x, delta_y).perform()
        SeleniumUtilities.log.info("Scrolled from an element by given amount")

    @staticmethod
    def copy_value_from_textbox(web_element):
        """Copy value from text field into clipboard using key actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: copy_value_from_textbox(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
        SeleniumUtilities.log.info("Copied value from the field using key actions.")

    @staticmethod
    def paste_value_into_textbox(web_element):
        """Paste value from clipboard into text field using key actions.

        :Args:
            - web_element - The web element to be interacted with.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: paste_value_into_textbox(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(web_element).click(web_element).key_down(Keys.CONTROL).send_keys('A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
        SeleniumUtilities.log.info("Pasted value into the field using key actions.")

    @staticmethod
    def copy_value_from_textbox_and_paste(source_web_element, target_web_element):
        """Copy value from a text field and pastes copied value into another text field using key actions.

        :Args:
            - source_web_element - The web element of the text field whose contents need to be copied.
            - target_web_element - The web element of the text field into which the contents need to be pasted.
        """
        if source_web_element is None or target_web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: copy_value_from_textbox_and_paste(source_web_element, target_web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        action = ActionChains(SeleniumBase.driver)
        action.move_to_element(source_web_element).click(source_web_element).key_down(Keys.CONTROL).send_keys(
            'A').key_up(
            Keys.CONTROL).key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
        action.move_to_element(target_web_element).click(target_web_element).key_down(Keys.CONTROL).send_keys(
            'A').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
        SeleniumUtilities.log.info("Copied value from a field and pasted it into another using key actions.")

    # endregion

    # region Reusable methods for actions performed using Javascript executor
    @staticmethod
    def click_element_using_javascript_executor(web_element):
        """Clicks the element using Javascript executor.

        :Args:
            - web_element - The web element to be clicked.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: click_element_using_javascript_executor(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].click();", web_element)
        SeleniumUtilities.log.info("Clicked on the element using Javascript executor.")

    @staticmethod
    def send_text_using_javascript_executor(web_element, text):
        """Sends text value to the element using Javascript executor after converting text value to string.

        :Args:
            - web_element - The web element to be interacted with.
            - text - The text value to be passed
        """
        if web_element is None or text is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: send_text_using_javascript_executor(web_element, text)")
            raise TypeError("Empty or invalid argument passed!!")
        text_input = str(text)
        SeleniumBase.driver.execute_script("arguments[0].value=arguments[1];", web_element, text_input)
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", web_element, text_input)
        SeleniumUtilities.log.info("Sent values: {0} to the field using Javascript executor.".format(text))

    @staticmethod
    def get_text_using_javascript_executor(web_element):
        """Retrieves the inner text of the text field using Javascript executor.

        :Args:
            - web_element - The web element of the text field whose text needs to be retrieved.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_text_using_javascript_executor(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        element_text = SeleniumBase.driver.execute_script("return arguments[0].innerText;", web_element)
        SeleniumUtilities.log.info("Retrieved the text: {0} from the element using Javascript executor.".format(element_text))
        return element_text

    @staticmethod
    def get_value_using_javascript_executor(web_element):
        """Retrieves the value of element using Javascript executor.

        :Args:
            - web_element - The web element of the field whose value needs to be retrieved.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_value_using_javascript_executor(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        element_value = SeleniumBase.driver.execute_script("return arguments[0].value;", web_element)
        SeleniumUtilities.log.info(
            "Retrieved the attribute value: {0} from the element using Javascript executor.".format(element_value))
        return element_value

    @staticmethod
    def get_attribute_using_javascript_executor(web_element, attr):
        """Retrieves the required attribute's value using Javascript executor.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
            - attr - The attribute whose value needs to be retrieved
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute_using_javascript_executor(web_element, attr)")
            raise TypeError("Empty or invalid Web element passed!!")
        element_attr = SeleniumBase.driver.execute_script("return arguments[0].getAttribute(arguments[1]);", web_element, attr)
        SeleniumUtilities.log.info(
            "Retrieved the attribute {0}: {1} from the element using Javascript executor.".format(attr, element_attr))
        return element_attr

    @staticmethod
    def update_attribute_using_javascript_executor(web_element, attribute, new_value):
        """Updates the value of required attribute of an element using Javascript executor.

        :Args:
            - web_element - The web element of the field whose attribute value needs to be retrieved.
            - attribute - The attribute whose value needs to be updated
            - new_value - The value that needs to be updated
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: update_attribute_using_javascript_executor(web_element, attribute, new_value)")
            raise TypeError("Empty or invalid Web element passed!!")
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute(attribute, new_value);", web_element)
        # SeleniumBase.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", web_element,
        #                                    attribute, new_value)
        SeleniumBase.driver.execute_script("arguments[0]." + attribute + "=arguments[1];", web_element, new_value)
        SeleniumUtilities.log.info("Updated the attribute {0} of the element to a new value: {1}".format(attribute, new_value))

    @staticmethod
    def scroll_to_element(web_element):
        """Scrolls the webpage until the element is displayed.

        :Args:
            - web_element - The web element up to which the web page needs to be scrolled..
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: scroll_to_element(web_element)")
            raise TypeError("Empty or invalid Web element passed!!")
        SeleniumBase.driver.execute_script("arguments[0].scrollIntoView(true);", web_element)
        # SeleniumBase.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        SeleniumUtilities.log.info("Scrolled to the web element using Javascript executor.")

    @staticmethod
    def scroll_window(scroll_value):
        """Scrolls the window up or down based on coordinate passed.

        :Args:
            - scroll_value - The coordinate value up to which the window need to be scrolled
        """
        if scroll_value is None:
            SeleniumUtilities.log.error(
                "Empty or invalid argument passed to the method: scroll_window(scroll_value)")
            raise TypeError("Empty or invalid argument passed!!")
        SeleniumBase.driver.execute_script("window.scrollBy(0," + scroll_value + ")")
        SeleniumUtilities.log.info("Scrolled the window with the coordinates {0}.".format(scroll_value))

    @staticmethod
    def highlight_field(element):
        """Highlights the element using Javascript executor.
           :args:
                - element - The web element which needs to be highlighted
        """
        if element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method: get_attribute(element,attribute)")
            raise TypeError("Empty or invalid element passed!!")
        SeleniumBase.driver.execute_script(
            "arguments[0].setAttribute('style','background: yellow; brder: 1px solid red;')", element)

    @staticmethod
    def press_keyboard_key(key):
        """
        This method presses the enter key on keyboard.
        :args:
                - key - Keyboard key needs to pass like enter, tab ,...
        """
        pyautogui.press(key)
        SeleniumUtilities.log.info("Clicked keyboard {0}.".format(key))

    @staticmethod
    def access_local_file(file_path):
        """
        This is the method which write the data into editor using pyautogui
        :args:
            -file_path- path of the file to upload or edit
        """
        SeleniumUtilities.log.info("Uploading a file: {0} ".format(file_path))
        pyautogui.write(file_path)

    # endregion

    @staticmethod
    def get_element_with_relative_locators(web_element, tag_name, relation_type):
        """
        Identifies the web element based on the relative type and return.
            :args:
                - web_element - Current element which is the base to get the relative web element
                - tag_name - tag name of the relative web element
                - relation_type - Type of the relation used to get the web element example: above ,below ,to_left_of ,to_right_of and near.
        """
        if web_element is None:
            SeleniumUtilities.log.error(
                "Empty or invalid Web element passed as argument to the method")
            raise TypeError("Empty or invalid Web element passed!!")
        if relation_type == "above":
            return SeleniumBase.driver.find_element(with_tag_name(tag_name=tag_name).above(web_element))
        elif relation_type == "below":
            return SeleniumBase.driver.find_element(with_tag_name(tag_name=tag_name).below(web_element))
        elif relation_type == "to_right_of":
            return SeleniumBase.driver.find_element(with_tag_name(tag_name=tag_name).to_right_of(web_element))
        elif relation_type == "to_left_of":
            return SeleniumBase.driver.find_element(with_tag_name(tag_name=tag_name).to_left_of(web_element))
        elif relation_type == "near":
            return SeleniumBase.driver.find_element(with_tag_name(tag_name=tag_name).near(web_element))




