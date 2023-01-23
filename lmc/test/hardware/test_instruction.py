from lmc.hardware.instruction import InstructionBuilder, Id, ADD, SUB, STA, LDA, BRA, BRZ, BRP, INP, OUT, HLT, DAT

import pytest


class TestInstructionNoLabel:
    test_data = [
        # Instruction, Expected Instruction Type, Expected Instruction opcode
        (INP(), INP, 901),  # INP
        (OUT(), OUT, 902),  # OUT
        (HLT(), HLT, 0),  # HLT
        (DAT(), DAT, 0),  # DAT
        (DAT(2), DAT, 2),  # DAT
    ]

    @pytest.mark.parametrize("test_instruction, expected_instruction_type, expected_instruction_opcode", test_data)
    def test_instruction_no_label(self, test_instruction, expected_instruction_type, expected_instruction_opcode):
        # Given an instruction that does not have a label

        instruction = test_instruction

        # WHen I get the instruction's type and opcode

        # Then I am given the expected instruction type and expected opcode

        assert isinstance(instruction, expected_instruction_type)
        assert instruction.get_code() == expected_instruction_opcode


class TestInstructionWithLabel:
    test_data = [
        # Instr      Type    Opcode    Address    Set addresss    Changed opcode
        (ADD(10), ADD, 110, 10, 11, 111),  # ADD
        (SUB(10), SUB, 210, 10, 11, 211),  # SUB

        (STA(10), STA, 310, 10, 11, 311),  # STA
        (LDA(10), LDA, 510, 10, 11, 511),  # LDA

        (BRA(10), BRA, 610, 10, 11, 611),  # BRA
        (BRZ(10), BRZ, 710, 10, 11, 711),  # BRZ
        (BRP(10), BRP, 810, 10, 11, 811),  # BRP
    ]

    @pytest.mark.parametrize(
        "test_instruction, expected_instruction_type, expected_instruction_opcode, expected_instruction_address, set_address, expected_instruction_change_address",
        test_data)
    def test_instruction_with_label(self, test_instruction, expected_instruction_type, expected_instruction_opcode,
                                    expected_instruction_address, set_address, expected_instruction_change_address):
        # Given an instruction that does have a label

        instruction = test_instruction

        # When I get the instruction's type and opcode

        # Then I am given the expected instruction type and expected opcode and address

        assert isinstance(instruction, expected_instruction_type)
        assert instruction.get_code() == expected_instruction_opcode
        assert instruction.get_address() == expected_instruction_address

        # When I set the address to a different value

        instruction.set_address(set_address)

        # Then I am given the changed address

        assert instruction.get_address() == set_address
        assert instruction.get_code() == expected_instruction_change_address


class TestInstructionNoAddressSet():
    def test_instruction_add(self):
        """Test I get an error trying to get the address of an instruction, when no address is set"""

        # Given an instruction that has a label (and hence an address), and I have not set an address

        # When I try to get the instruction's address

        # Then I should get an exception

        error_message = r'Address not set'
        with pytest.raises(Exception, match=error_message):
            instruction = ADD()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = SUB()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = STA()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = LDA()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = BRA()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = BRZ()
            instruction.get_code()
        with pytest.raises(Exception, match=error_message):
            instruction = BRP()
            instruction.get_code()

    def test_building_instruction_from_known_instruction_id(self):
        """Test I can build an instruction from an instruction id"""

        # When I try to build an instruction from a known instruction id

        # Then I get the corresponding instruction

        assert isinstance(InstructionBuilder.build(Id.ADD), ADD)
        assert isinstance(InstructionBuilder.build(Id.SUB), SUB)
        assert isinstance(InstructionBuilder.build(Id.LDA), LDA)
        assert isinstance(InstructionBuilder.build(Id.STA), STA)
        assert isinstance(InstructionBuilder.build(Id.BRA), BRA)
        assert isinstance(InstructionBuilder.build(Id.BRZ), BRZ)
        assert isinstance(InstructionBuilder.build(Id.BRP), BRP)
        assert isinstance(InstructionBuilder.build(Id.INP), INP)
        assert isinstance(InstructionBuilder.build(Id.OUT), OUT)
        assert isinstance(InstructionBuilder.build(Id.HLT), HLT)
        assert isinstance(InstructionBuilder.build(Id.DAT), DAT)

    def test_building_instruction_from_unknown_instruction_id(self):
        """Test I get an error trying to build  an instruction from an unknown instruction id"""

        # When I try to build an instruction from a unknown instruction id

        # Then I get an exception

        error_message = r'Not recognized'
        with pytest.raises(Exception, match=error_message):
            InstructionBuilder.build(None)
