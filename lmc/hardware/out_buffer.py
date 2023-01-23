class OutBuffer():
    """Performs and controls output to the user from the computer

    The output written, can be captured to a file, for testing. The file to write to
    is either supplied through the constructor, or by a 'setter' method

    Alternatively, the last value written is stored, and can be retrieved for testing"""

    def __init__(self, file_to_write_to=None):
        self.file_to_write_to = file_to_write_to
        self.value = None

    def set_file_to_write_to(self, file_to_write_to):
        self.file_to_write_to = file_to_write_to

    def write_value(self, value: int):
        if self.file_to_write_to:
            # Write the output to a file
            self._write_value_to_file(value)
        else:
            # Write the putput to the user
            self._write_value_to_user(value)

    def get_value_for_test(self) -> int:
        """Gets the last value that was written"""
        if self.value is None:
            raise Exception('No value set in output buffer')
        return self.value

    def _write_value_to_user(self, value: int):
        # Record the last value written, for testing purposes
        self.value = value
        print(value)

    def _write_value_to_file(self, value: int):
        with open(self.file_to_write_to, 'a', encoding='ascii') as out_file:
            out_file.write(str(value) + "\n")
