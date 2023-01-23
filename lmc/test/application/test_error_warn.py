from lmc.application.error_warn import ErrorWarn
from lmc.test.util.capture_stdout import CaptureStdout


class TestErrorWarn:
    def test_warn_error(self):
        """Test a warning message can be issued for the user to stdout"""

        # When I issue a 'Warning' for the user

        error_message_text = "test error message"
        expected_message = '\nWARN ERROR ...\n' + \
            f'\n{error_message_text}\n\n'

        actual_message = CaptureStdout.redirect(
            ErrorWarn.warn_error, error_message_text)

       # Then the 'Warning' message is printed to stdout for the user

        assert actual_message == expected_message

    def test_warn_input_not_integer_or_float(self):
        """Test a warning message can be issued for the user to stdout,
        when an input value was not an integer or floating point value"""

        # When I issue a 'Warning' for the user, that I was expecting an integer or floating point value

        error_message_text = "test error message"
        expected_message = '\nWARN ERROR ...\n' + \
            f'\nInput value was not an integer or floating point number, found - {error_message_text}\n\n'

        actual_message = CaptureStdout.redirect(
            ErrorWarn.warn_input_not_integer_or_float, error_message_text)

        # Then the 'Warning' message is printed to stdout for the user

        assert actual_message == expected_message
