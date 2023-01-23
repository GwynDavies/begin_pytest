import os.path
import re
from lmc.computer.computer import Computer
import pytest


class TestComputerProgramFileHandling:
    @pytest.fixture
    def this_tests_directory(self):
        test_files_directory = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(test_files_directory, 'lmcb_test_files')

    def test_file_not_found_error_when_file_to_run_not_exist(self, this_tests_directory):
        # Given a file path that does not exist, and a computer

        test_file = os.path.join(this_tests_directory, 'does_not_exist.lmcb')
        computer = Computer()

        # When I try to run the file on the computer

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            computer.run(test_file)

        # Then I get an exception with a corresponding error message

        assert pytest_wrapped_e.type == SystemExit
        expected_message_pattern = r'FATAL ERROR .+File not found - .+does_not_exist.lmcb.+Exiting'
        assert re.search(expected_message_pattern,
                         pytest_wrapped_e.value.code, re.S)

    def test_file_empty(self, this_tests_directory):
        # Given a file path that is an empty file, and a computer

        test_file = os.path.join(this_tests_directory, 'empty.lmcb')
        computer = Computer()

        # When I try to run the file on the computer

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            computer.run(test_file)

        # Then I get an exception with a corresponding error message

        assert pytest_wrapped_e.type == SystemExit
        expected_message_pattern = r'FATAL ERROR .+File is empty - .+empty.lmcb.+Exiting'
        assert re.search(expected_message_pattern,
                         pytest_wrapped_e.value.code, re.S)

    def test_file_has_bad_opcodes(self, this_tests_directory):
        # Given a file path that is program file that has bad opcode, and a computer

        test_file = os.path.join(this_tests_directory, 'bad_opcodes.lmcb')
        computer = Computer()

        # When I try to run the file on the computer

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            computer.run(test_file)

        # Then I get an exception with a corresponding error message

        assert pytest_wrapped_e.type == SystemExit
        expected_message_pattern = r'FATAL\sERROR\(S\).+Opcode 9a1 is not valid, must be numeric.+Opcode 3 6 is not valid, must be numeric.+Opcode 00 is not valid, should be 3 chars.+Exiting'
        assert re.search(expected_message_pattern,
                         pytest_wrapped_e.value.code, re.S)
