import pytest

from lmc.io.file.executable_program.executable_instruction import ExecutableInstruction


class TestExecutableInstruction:
    def test_executable_instruction_getting_the_opcode(self):
        # Given an executable instruction

        executable_instruction = ExecutableInstruction(101)

        # When I get the opcode

        # Then I get the code I created the instruction with

        assert executable_instruction.get_opcode() == 101

    def test_executable_instruction_getting_the_index_when_its_not_set(self):
        # Given an executable instruction

        executable_instruction = ExecutableInstruction(101)

        # When I get the index when one is not set

        # Then I get an error

        with pytest.raises(Exception, match=r'Index is not set'):
            _ = executable_instruction.get_index()
        executable_instruction.set_index(5)
        assert executable_instruction.get_index() == '5'

    def test_executable_instruction_getting_the_index_when_it_is_set(self):
        # Given an executable instruction, that has an index set

        index_value = '5'
        executable_instruction = ExecutableInstruction(101)
        executable_instruction.set_index(index_value)

        # When I get the index

        # Then I should get the expected index

        assert executable_instruction.get_index() == str(index_value)
