from lmc.hardware.instruction import INP, STA, DAT
from lmc.io.file.source_pprogram.source_instruction import SourceInstructionNoLabel, SourceInstructionWithLabel, SourceInstructionDat, SourceInstructionError
from lmc.io.file.source_pprogram.source_program import SourceProgram
import pytest


class TestSourceInstructions:
    def test_max_size(self):
        assert SourceProgram.get_max_size() == 100

    def test_instruction_no_errors(self):
        instruction = INP()
        instruction_no_label = SourceInstructionNoLabel(instruction)

        instruction = STA()
        label = 'LABEL1'
        instruction_with_label = SourceInstructionWithLabel(instruction, label)

        instruction = DAT()
        instruction_dat = SourceInstructionDat(instruction)

        source_instructions = SourceProgram()

        source_instructions.append(instruction_no_label)
        source_instructions.append(instruction_with_label)
        source_instructions.append(instruction_dat)

        assert len(source_instructions) == 3
        assert source_instructions.has_errors() is False
        assert not source_instructions.get_list_errors()

        i = source_instructions[0].get_instruction()
        assert isinstance(i, INP)
        i = source_instructions[1].get_instruction()
        assert isinstance(i, STA)
        i = source_instructions[2].get_instruction()
        assert isinstance(i, DAT)

    def test_instruction_has_error(self):
        instruction = INP()
        instruction_no_label = SourceInstructionNoLabel(instruction)

        instruction = STA()
        label = 'LABEL1'
        instruction_with_label = SourceInstructionWithLabel(instruction, label)

        message = 'Test message'
        instruction_error = SourceInstructionError(message)

        source_instructions = SourceProgram()

        source_instructions.append(instruction_no_label)
        source_instructions.append(instruction_with_label)
        source_instructions.append(instruction_error)

        assert len(source_instructions) == 3
        assert source_instructions.has_errors() is True
        assert len(source_instructions.get_list_errors()) == 1

        source_instruction = source_instructions[0].get_instruction()
        assert isinstance(source_instruction, INP)

        source_instruction = source_instructions[1].get_instruction()
        assert isinstance(source_instruction, STA)

        source_instruction = source_instructions[2]
        assert isinstance(source_instruction, SourceInstructionError)

    def test_instruction_max_append(self):
        instruction = INP()
        instruction_no_label = SourceInstructionNoLabel(instruction)

        source_instructions = SourceProgram()
        for _ in range(101):
            source_instructions.append(instruction_no_label)

        with pytest.raises(Exception, match=r'Source instructions exceed max size of 100 instructions'):
            source_instructions.append(instruction_no_label)
