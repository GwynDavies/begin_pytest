import sys
from os.path import exists
from os import remove


class CaptureStdout:
    TEMP_STDOUT_FILE_NAME = 'test_temp_stdout_file.txt'

    @staticmethod
    def redirect(method, text):
        original_stdout = sys.stdout
        try:
            with open(CaptureStdout.TEMP_STDOUT_FILE_NAME, 'w', encoding='ascii') as test_stdout_file:
                # Redirect stdout to a file
                sys.stdout = test_stdout_file
                method(text)
        finally:
            # Reset stdout back to its original setting
            sys.stdout = original_stdout

        with open(CaptureStdout.TEMP_STDOUT_FILE_NAME, 'r', encoding='ascii') as test_stdout_file:
            stdout_text = test_stdout_file.read()

        if exists(CaptureStdout.TEMP_STDOUT_FILE_NAME):
            remove(CaptureStdout.TEMP_STDOUT_FILE_NAME)

        return stdout_text
