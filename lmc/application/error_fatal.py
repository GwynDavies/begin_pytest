import sys
from typing import List


class ErrorFatal:
    """For generating fatal errors when running the assembler or computer.

    Generates the error message, and exits execution, returning to the operating system
    """

    @staticmethod
    def exit_fatal_error(error_message: str):
        error_text = '\nFATAL ERROR ...\n'
        error_text = error_text + f'\n{error_message}\n'
        error_text = error_text + '\nExiting\n'
        sys.exit(error_text)

    @staticmethod
    def exit_fatal_errors(error_messages: List[str]):
        error_text = '\nFATAL ERROR(S) ...\n'
        for error_message in error_messages:
            error_text = error_text + f'\n{error_message}\n'

        error_text = error_text + '\nExiting\n'
        sys.exit(error_text)

    # File

    @staticmethod
    def exit_file_not_found(file_name: str):
        ErrorFatal.exit_fatal_error(f'File not found - {file_name}')

    @staticmethod
    def exit_file_is_empty(file_name: str):
        ErrorFatal.exit_fatal_error(f'File is empty - {file_name}')
