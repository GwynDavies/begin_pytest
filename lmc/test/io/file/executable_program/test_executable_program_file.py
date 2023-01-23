from os.path import exists
from typing import List

import pytest

from lmc.io.file.executable_program.executable_instruction import ExecutableInstruction, ExecutableInstructionError
from lmc.io.file.executable_program.executable_program_file import ExecutableProgramFile
from lmc.test.util.test_data_file import TestDataFile
from lmc.test.util.test_data_opcodes import TestDataOpcodes


class TestExecutableProgramFile:
    #
    # Fixtures
    #

    @pytest.fixture
    def fixture_test_subtract_program_opcodes(self) -> List[int]:
        """Test program used by a number of the tests here - subtract 2 numbers program"""
        return TestDataOpcodes.opcodes_subtract()

    @pytest.fixture
    def fixture_test_executable_filename(self, tmp_path) -> List[int]:
        """Test executable program file name, also cleans up the file if it exists after the test

        See here for temporary files in pytest https://docs.pytest.org/en/6.2.x/tmpdir.html"""
        value = tmp_path / 'test_executable_program_file.lmcb'

        yield value

        # Clean up after test runs
        TestDataFile.clean_test_file_if_exists(value)

    #
    # Tests
    #

    def test_write_file(self, fixture_test_subtract_program_opcodes, fixture_test_executable_filename):
        # Given opcodes for a program

        test_program_opcodes = fixture_test_subtract_program_opcodes
        temporary_executable_filename = fixture_test_executable_filename

        # When I create and write an executable program, using the opcodes

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.write(test_program_opcodes)

        # Then I can see that the executable file exists, and it has the expected size in bytes

        assert exists(temporary_executable_filename)
        assert executable_program_file.exists() is True
        assert executable_program_file.size_in_bytes() == 30

    def test_read_file(self, fixture_test_subtract_program_opcodes, fixture_test_executable_filename):
        # Given an existing executable program file

        test_program_opcodes = fixture_test_subtract_program_opcodes
        temporary_executable_filename = fixture_test_executable_filename

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.write(test_program_opcodes)
        assert exists(temporary_executable_filename)

        # When I read the executable program file

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.read()

        # Then I get the expected length of the executable program files, executable program
        #     and the expected program opcodes

        assert len(executable_program_file) == 10
        opcodes = executable_program_file.get_executable_program()

        assert len(opcodes) == 10
        assert opcodes[0].get_opcode() == "901"  # INP
        assert opcodes[1].get_opcode() == "308"  # STA
        assert opcodes[2].get_opcode() == "901"  # INP
        assert opcodes[3].get_opcode() == "309"  # STA
        assert opcodes[4].get_opcode() == "508"  # LDA
        assert opcodes[5].get_opcode() == "209"  # SUB
        assert opcodes[6].get_opcode() == "902"  # OUT
        assert opcodes[7].get_opcode() == "000"  # HLT
        assert opcodes[8].get_opcode() == "000"  # DAT 0
        assert opcodes[9].get_opcode() == "000"  # DAT 0

    def test_python_get_method(self, fixture_test_subtract_program_opcodes, fixture_test_executable_filename):
        # Given an existing executable program file

        test_program_opcodes = fixture_test_subtract_program_opcodes
        temporary_executable_filename = fixture_test_executable_filename

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.write(test_program_opcodes)
        assert exists(temporary_executable_filename)

        # When I read the executable program file

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.read()

        # Then I get the expected length of the executable program files, executable program
        #     and the expected program opcodes

        assert len(executable_program_file) == 10
        assert executable_program_file[0].get_opcode() == "901"  # INP
        assert executable_program_file[1].get_opcode() == "308"  # STA
        assert executable_program_file[2].get_opcode() == "901"  # INP
        assert executable_program_file[3].get_opcode() == "309"  # STA
        assert executable_program_file[4].get_opcode() == "508"  # LDA
        assert executable_program_file[5].get_opcode() == "209"  # SUB
        assert executable_program_file[6].get_opcode() == "902"  # OUT
        assert executable_program_file[7].get_opcode() == "000"  # HLT
        assert executable_program_file[8].get_opcode() == "000"  # DAT 0
        assert executable_program_file[9].get_opcode() == "000"  # DAT 0

    def test_getting_as_a_string(self, fixture_test_subtract_program_opcodes, fixture_test_executable_filename):
        # Given an existing executable program file

        test_program_opcodes = fixture_test_subtract_program_opcodes
        temporary_executable_filename = fixture_test_executable_filename

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        for opcode in test_program_opcodes:
            executable_program_file.append(opcode)

        expected_value = '901\n' + \
                         '308\n' + \
                         '901\n' + \
                         '309\n' + \
                         '508\n' + \
                         '209\n' + \
                         '902\n' + \
                         '0\n' + \
                         '0\n' + \
                         '0\n'

        # Then I can get the executable program as a string

        assert str(executable_program_file) == expected_value

    # No fixtures

    def test_when_executable_program_has_an_error(self):
        # Given an existing executable program file that has a valid opcode and an error

        executable_program_file = ExecutableProgramFile(None)
        executable_program_file.append(ExecutableInstruction('901'))
        executable_program_file.append(
            ExecutableInstructionError('test error'))

        # When I get the executable program it contains

        executable_program = executable_program_file.get_executable_program()

        # Then it has the expected length (2 opcodes), and the valid opcode and the error

        assert len(executable_program) == 2
        assert executable_program[0].get_opcode() == '901'
        assert executable_program[1].get_message() == 'test error'

    def test_when_executable_program_has_multiple_errors(self, fixture_test_executable_filename):
        # Given an existing executable program file that has a valid opcode and two errors

        temporary_executable_filename = fixture_test_executable_filename

        with open(temporary_executable_filename, 'w', encoding='ascii') as text_file:
            my_string = '901abc12'
            text_file.write(my_string)
        assert exists(temporary_executable_filename)

        executable_program_file = ExecutableProgramFile(
            temporary_executable_filename)
        executable_program_file.read()
        assert len(executable_program_file) == 3

        # When I get the executable program it contains

        binary_opcodes = executable_program_file.get_executable_program()

        # Then it has the expected length (3 opcodes), and the valid opcode and the two errors

        assert len(binary_opcodes) == 3

        assert binary_opcodes[0].get_opcode() == '901'

        assert binary_opcodes[1].get_message(
        ) == 'Opcode abc is not valid, must be numeric'
        assert binary_opcodes[2].get_message(
        ) == 'Opcode 12 is not valid, should be 3 chars'
