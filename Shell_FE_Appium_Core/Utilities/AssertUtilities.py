
class AssertUtilities:
    """AssertionUtilities class contains reusable methods for common assertions used."""

    @staticmethod
    def assert_equals(actual_value, expected_value):
        """Asserts if the two values are equal."""
        if actual_value is None or expected_value is None:
            assert False, "Either {0} or {1} is None".format(actual_value, expected_value)
        assert actual_value == expected_value, "{0} is not equals to the {1}".format(actual_value, expected_value)

    @staticmethod
    def assert_not_equals(actual_value, expected_value):
        """Asserts if the two values are not equal."""
        if actual_value is None or expected_value is None:
            assert False, "Either {0} or {1} is None".format(actual_value, expected_value)
        assert actual_value != expected_value, "{0}is equal to the {1}".format(actual_value, expected_value)

    @staticmethod
    def assert_value_in_list(value_to_be_in_list, list_value):
        """Asserts the value in the list
           :args:
                -value_to_be_in_list - value to be searched in the list
                -list_value - List of values to be searched in
        """
        if value_to_be_in_list is None or list_value is None:
            assert False, "Either {0} or {1} is None".format(value_to_be_in_list, list_value)
        assert value_to_be_in_list in list_value, "{0} is in to the {1}".format(value_to_be_in_list, list_value)

    @staticmethod
    def assert_contains(search_value, list_value):
        """Asserts if the object contains a value (i.e.) check for substring in string or a value in list or set etc.

        :Args:
            - search_value - The value to be searched
            - list_value - List of values to be searched in
        """
        if search_value is None or list_value is None:
            assert False, "Either {0} or {1} is None".format(search_value, list_value)

        assert search_value in list_value, "{0} is not present in {1}".format(search_value, list_value)

    @staticmethod
    def assert_not_contains(search_value, list_value):
        """Asserts if the object does not contain a value (i.e.)
        check if the substring is not present in string or a value not in list or set etc.

        :Args:
            - search_value - The value to be searched
            - list_value -  List of values to be searched in
        """
        if search_value is None or list_value is None:
            assert False, "Either {0} or {1} is None".format(search_value, list_value)
        assert search_value not in list_value, "{0} is present in {1}".format(search_value, list_value)

    @staticmethod
    def assert_none(value):
        """Asserts if the value passed is None."""
        if value is None:
            assert True
        else:
            assert False, "{0} is not None".format(value)

    @staticmethod
    def assert_not_none(value_to_be_checked):
        """Asserts if the value passed is not None."""
        if value_to_be_checked is not None:
            assert True
        else:
            assert False, "Value is None"

    @staticmethod
    def assert_if_true(value_to_be_checked):
        """Asserts if the value is True."""
        if value_to_be_checked is True:
            assert True
        else:
            assert False, "{0} is False".format(value_to_be_checked)

    @staticmethod
    def assert_if_false(value_to_be_checked):
        """Asserts if the value is False."""
        if value_to_be_checked is False:
            assert True
        else:
            assert False, "{0} is True".format(value_to_be_checked)
