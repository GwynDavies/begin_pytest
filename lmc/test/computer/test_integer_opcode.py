from lmc.computer.integer_opcode import IntegerOpcode
from lmc.hardware.instruction import ADD, SUB, STA, LDA, BRA, BRZ, BRP, INP, OUT, HLT, DAT
import pytest


class TestIntegerOpcode:
    test_data_integer_opcodes_to_executable_instructions = [
        (101, ADD),  # ADD opcode
        (201, SUB),  # SUB opcode
        (301, STA),  # STA opcode
        (501, LDA),  # LDA opcode
        (601, BRA),  # BRA opcode
        (701, BRZ),  # BRA opcode
        (801, BRP),  # BRP opcode
        (901, INP),  # INP opcode
        (902, OUT),  # OUT opcode
        (0,   HLT),  # HLT opcode
        (1,   DAT),  # Anything else is considered a DAT
        (903, DAT),
    ]

    @pytest.mark.parametrize("test_integer_opcode, expected_computer_instruction", test_data_integer_opcodes_to_executable_instructions)
    def test_binary_opcode_decoder(self, test_integer_opcode, expected_computer_instruction):
        """Test decoding a binary opcode, gives the corresponding executable instruction"""

        # When I decode an integer opcode

        integer_opcode_decoder = IntegerOpcode()
        executable_instruction = integer_opcode_decoder.convert_to_instruction(
            test_integer_opcode)

        # Then I should get the corresponding computer instruction

        assert isinstance(executable_instruction,
                          expected_computer_instruction)
