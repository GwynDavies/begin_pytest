import pytest

from lmc.io.file.executable_program.executable_instruction import ExecutableInstruction, ExecutableInstructionError, \
    ExecutableItem
from lmc.io.file.executable_program.executable_program import ExecutableProgram


class TestExecutableProgram:
    @pytest.fixture()
    def fixture_executable_program_with_no_errors(self) -> ExecutableProgram:
        executable_program = ExecutableProgram()
        executable_program.append(ExecutableInstruction(101))
        executable_program.append(ExecutableInstruction(102))
        executable_program.append(ExecutableInstruction(103))
        return executable_program

    @pytest.fixture()
    def fixture_executable_program_with_an_error(self) -> ExecutableProgram:
        executable_program = ExecutableProgram()
        executable_program.append(ExecutableInstruction(101))
        executable_program.append(ExecutableInstructionError('test error'))
        executable_program.append(ExecutableInstruction(103))
        return executable_program

    #
    # Executable program that does not have an error
    #

    def test_executable_program_has_no_errors_check_length(self, fixture_executable_program_with_no_errors):
        # Given an executable program that has instructions but no errors

        executable_program = fixture_executable_program_with_no_errors

        # When I get the len of the program
        # Then I get the expected number of opcodes,

        assert len(executable_program) == 3

    def test_executable_program_has_no_errors_check_has_errors(self, fixture_executable_program_with_no_errors):
        # Given an executable program that has instructions but no errors

        executable_program = fixture_executable_program_with_no_errors

        # When I check whether the executable program has errors
        # Then I get that there are no errors in the executable program

        assert executable_program.has_errors() is False
        assert not executable_program.get_list_errors()

        # When I check the type of each of the executable program opcodes

        # Then all the opcodes are instances of an Executable Instruction

        for opcode in executable_program:
            assert isinstance(opcode, ExecutableInstruction)

    def test_executable_program_has_no_errors_check_opcodes(self, fixture_executable_program_with_no_errors):
        # Given an executable program that has instructions but no errors

        executable_program = fixture_executable_program_with_no_errors

        # When I check the type of each of the executable program opcodes
        # Then all the opcodes are instances of an Executable Instruction

        for opcode in executable_program:
            assert isinstance(opcode, ExecutableInstruction)

    #
    # Executable program that does have an error
    #

    def test_executable_program_has_an_error_check_lengths(self,
                                                           fixture_executable_program_with_an_error):
        # Given an executable program that has instructions and an error

        executable_program_with_error = fixture_executable_program_with_an_error

        # When I get the len of the program
        # Then I get the expected number of opcodes,

        assert len(executable_program_with_error) == 3

    def test_executable_program_has_an_error_check_has_errors(self,
                                                              fixture_executable_program_with_an_error):
        # Given an executable program that has instructions and an error

        executable_program_with_error = fixture_executable_program_with_an_error

        # When I check whether the executable program has errors
        # Then I get that there are errors in the executable program

        assert executable_program_with_error.has_errors() is True
        assert len(executable_program_with_error.get_list_errors()) == 1

    def test_executable_program_has_an_error_check_get_the_expected_values(self,
                                                                           fixture_executable_program_with_an_error):
        # Given an executable program that has instructions and an error

        executable_program_with_error = fixture_executable_program_with_an_error

        # When I check the type of each of the executable program opcodes
        # Then I find the Executable Instructions and the Executable Instruction Error
        # are in the expected locations

        executable_item: ExecutableItem = executable_program_with_error[0]
        assert isinstance(executable_item, ExecutableInstruction)

        executable_item = executable_program_with_error[1]
        assert isinstance(executable_item, ExecutableInstructionError)

        executable_item = executable_program_with_error[2]
        assert isinstance(executable_item, ExecutableInstruction)

    def test_get_memory_image_when_program_has_error(self, fixture_executable_program_with_an_error):
        # Given an executable program that has instructions and an error

        executable_program_with_error = fixture_executable_program_with_an_error

        # When I get the memory image
        # Then I get an exception

        with pytest.raises(Exception, match=r'Cannot create memory image as program has errors'):
            executable_program_with_error.get_memory_image()

    #
    # Maximum number of opcodes
    #

    def test_max_size(self):
        # Given an executable program
        # When I get its maximum size of an executable program
        # Then it says that the maximum size is 100 memory locations

        assert ExecutableProgram.get_max_size() == 100

    def test_appending_maximum_number_of_opcodes(self):
        # Given an executable program that has an Executable Instruction

        binary_opcode = ExecutableInstruction(101)
        binary_opcodes = ExecutableProgram()

        # When I append executable instructions
        # Then I can append up to the maximum allowed number of opcodes, and
        #     after that, appending additional opcodes gives an error

        for _ in range(101):
            binary_opcodes.append(binary_opcode)

        with pytest.raises(Exception, match=r'Binary opcodes exceed max size of 100 opcodes'):
            binary_opcodes.append(binary_opcode)

    def test_get_memory_image_when_program_is_empty(self):
        # Given an empty executable program

        executable_program = ExecutableProgram()

        # When I get the memory image
        # Then I get an exception

        with pytest.raises(Exception, match=r'Cannot create memory image as program is empty'):
            executable_program.get_memory_image()
