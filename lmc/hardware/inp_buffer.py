import re
from lmc.application.error_warn import ErrorWarn


class InpBuffer():
    """
    Performs and controls input from the user to the computer

    Test values can be set from a given file. This file is supplied by the constructor
    or by a 'setter' method
    """

    def __init__(self, file_to_read_from=None):
        """
        Set file_to_read_From, if you want to take input from a file, else it will be got from the user
        """
        self.file_to_read_from = file_to_read_from
        if self.file_to_read_from:
            self._get_test_values_from_file()
        else:
            self.test_values = None

        self.floating_point_regex = r'^[+-]?[0-9]+.[0-9]+$'
        self.integer_regex = r'^[+-]?[0-9]+$'

    def set_file_to_read_from(self, file_to_read_from):
        """Set a file to load test values from, these will be used in place of prompting the user """
        self.file_to_read_from = file_to_read_from
        self._get_test_values_from_file()

    def get_value(self):
        """ If we have test values then use one of them, else get the value from the user """
        if self.test_values:
            return int(self.test_values.pop(0))
        return self._get_value_from_user()

    def _get_test_values_from_file(self) -> None:
        """
        Intended for use during testing, a file is supplied with values simulating user input
        """
        with open(self.file_to_read_from, "r", encoding='ascii') as inp:
            file_contents = inp.read()
            self.test_values = file_contents.split("\n")

    def _get_value_from_user(self):  # pragma: no cover
        value_accepted = False
        while not value_accepted:
            input_value = input('Enter a number: ').strip()
            if re.search(self.floating_point_regex, input_value):
                # Accept floating point number
                value_input = float(input_value)
                value_accepted = True
            elif re.search(self.integer_regex, input_value):
                # Accept integer number
                value_input = int(input_value)
                value_accepted = True
            else:
                ErrorWarn.warn_input_not_integer_or_float(input_value)

        return value_input
