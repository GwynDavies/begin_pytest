class ErrorWarn:
    """
    For generating warnings to the user, when running the assembler or computer.
    """

    @staticmethod
    def warn_error(error_message: str):
        error_text = '\nWARN ERROR ...\n'
        error_text = error_text + f'\n{error_message}\n'
        print(error_text)

    @staticmethod
    def warn_input_not_integer_or_float(input_value: str):
        ErrorWarn.warn_error(
            f'Input value was not an integer or floating point number, found - {input_value}')
