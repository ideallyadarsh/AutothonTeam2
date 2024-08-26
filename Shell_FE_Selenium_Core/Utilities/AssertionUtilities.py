class AssertionUtilities:
    """AssertionUtilities class contains reusable methods for common assertions used."""

    @staticmethod
    def assert_equals(value1, value2):
        """Asserts if the two values are equal."""
        if value1 is None:
            assert False, "{0} is None or empty".format(value1)
        if value2 is None:
            assert False, "{0} is None or empty".format(value2)
        assert value1 == value2, "{0} is not equal to {1}".format(value1, value2)

    @staticmethod
    def assert_not_equals(value1, value2):
        """Asserts if the two values are not equal."""
        if value1 is None:
            assert False, "{0} is None or empty".format(value1)
        if value2 is None:
            assert False, "{0} is None or empty".format(value2)
        assert value1 != value2, "{0} is equal to {1}".format(value1, value2)

    @staticmethod
    def assert_contains(valuetobesearched_for, valuetobesearched_in):
        """Asserts if the object contains a value (i.e.) check for substring in string or a value in list or set etc.

        :Args:
            - valuetobesearched_for - The value to be searched
            - valuetobesearched_in - The object in which the search is to be made
        """
        if valuetobesearched_for is None:
            assert False, "{0} is None or empty".format(valuetobesearched_for)
        if valuetobesearched_in is None:
            assert False, "{0} is None or empty".format(valuetobesearched_in)
        assert valuetobesearched_for in valuetobesearched_in, "{0} is not present in {1}".format(valuetobesearched_for,
                                                                                                 valuetobesearched_in)

    @staticmethod
    def assert_not_contains(valuetobesearched_for, valuetobesearched_in):
        """Asserts if the object does not contain a value (i.e.)
        check if the substring is not present in string or a value not in list or set etc.

        :Args:
            - valuetobesearched_for - The value to be searched
            - valuetobesearched_in - The object in which the search is to be made
        """
        if valuetobesearched_for is None:
            assert False, "{0} is None or empty".format(valuetobesearched_for)
        if valuetobesearched_in is None:
            assert False, "{0} is None or empty".format(valuetobesearched_in)
        assert valuetobesearched_for not in valuetobesearched_in, "{0} is present in {1}".format(valuetobesearched_for,
                                                                                                 valuetobesearched_in)

    @staticmethod
    def assert_none(value):
        """Asserts if the value passed is None."""
        if value is None:
            assert True
        else:
            assert False, "{0} is not None".format(value)

    @staticmethod
    def assert_not_none(value):
        """Asserts if the value passed is not None."""
        if value is not None:
            assert True
        else:
            assert False, "Value is None"

    @staticmethod
    def assert_if_true(value):
        """Asserts if the value is True."""
        if value is True:
            assert True
        else:
            assert False, "{0} is False".format(value)

    @staticmethod
    def assert_if_false(value):
        """Asserts if the value is False."""
        if value is False:
            assert True
        else:
            assert False, "{0} is True".format(value)
