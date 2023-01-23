from lmc.io.file.program_file import ProgramFile
from lmc.test.util.empty_test_file import EmptyTestFile


class TestProgram:
    def test_exists_and_is_empty(self):
        try:
            # Given an empty test file

            test_file_name = 'test_program_file.test'
            empty_test_file = EmptyTestFile(test_file_name)
            empty_test_file.create()

            # When I create a Program File that uses the empty test file

            program_file = ProgramFile(test_file_name)

            # Then the Program file reprots teh file exists, and that the file is empty

            assert program_file.exists() is True
            assert program_file.is_empty() is True

        finally:
            # Clean up
            if empty_test_file:
                empty_test_file.remove_if_exist()
