from lmc.hardware.instruction import INP, STA, DAT
from lmc.io.file.source_pprogram.source_instruction import SourceInstructionNoLabel, SourceInstructionWithLabel, SourceInstructionDat, SourceInstructionError, SourceItem
import pytest


class TestSourceInstruction:
    def test_source_instruction_no_label(self):
        instruction = INP()
        instruction_no_label = SourceInstructionNoLabel(instruction)
        assert isinstance(instruction_no_label.get_instruction(), INP)
        assert isinstance(instruction_no_label.get_instruction(), INP) is True

    def test_source_instruction_with_label(self):
        instruction = STA()
        label = 'LABEL1'
        instruction_with_label = SourceInstructionWithLabel(instruction, label)
        assert isinstance(instruction_with_label.get_instruction(), STA)
        assert isinstance(
            instruction_with_label.get_instruction(), STA) is True
        assert instruction_with_label.get_label() == label

    def test_source_instruction_dat(self):
        instruction = DAT()
        instruction_dat = SourceInstructionDat(instruction)
        assert isinstance(instruction_dat.get_instruction(), DAT)
        assert isinstance(instruction_dat.get_instruction(), DAT) is True
        assert instruction_dat.get_instruction().get_code() == 0

    def test_source_instruction_error(self):
        message = 'Test message'
        instruction_error = SourceInstructionError(message)
        assert instruction_error.get_message() == message
        instruction_error.set_line_number(101)
        assert str(instruction_error) == 'Line 101 - Test message'

    def test_source_item(self):
        instruction = SourceInstructionError(None)
        instruction.set_line_number(101)
        assert instruction.get_line_number() == '101'

        instruction = SourceInstructionNoLabel(None)
        instruction.set_line_number(101)
        assert instruction.get_line_number() == '101'

        instruction = SourceInstructionWithLabel(None, None)
        instruction.set_line_number(101)
        assert instruction.get_line_number() == '101'

        instruction = SourceInstructionDat(None)
        instruction.set_line_number(101)
        assert instruction.get_line_number() == '101'

        instruction = SourceItem()
        with pytest.raises(Exception, match=r'Line number is not set'):
            _ = instruction.get_line_number()
