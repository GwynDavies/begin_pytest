from lmc.hardware.instruction import INP, OUT, HLT, ADD, SUB, STA, LDA, BRA, BRZ, BRP, DAT
from lmc.assembler.parser import Parser
from lmc.io.file.source_pprogram.source_instruction import SourceInstructionNoLabel, SourceInstructionWithLabel, \
    SourceInstructionDat, SourceInstructionError
import pytest


class TestParserMnemonicHasNoLabel:
    """Test source language instructions that do not have an associated label"""
    test_data = [
        ("INP", SourceInstructionNoLabel, INP),
        ("OUT", SourceInstructionNoLabel, OUT),
        ("HLT", SourceInstructionNoLabel, HLT),
    ]

    @pytest.mark.parametrize(
        "test_source_instruction,  expected_source_instruction_type, expected_hardware_instruction", test_data)
    def test_mnemonic_no_label(self, test_source_instruction, expected_source_instruction_type,
                               expected_hardware_instruction):
        """Test the parser correctly determines when a source language instruction has no associated
        label - INP, OUT, HLT"""

        # Given a test-source-instruction

        # When the test-source-instruction is parsed
        parser = Parser()
        result = parser.parse_source_instruction(test_source_instruction)

        # Then I should get the expected-source-instruction-type
        assert isinstance(result, expected_source_instruction_type)

        # And I should also get the corresponding expected_hardware_instruction
        assert isinstance(result.get_instruction(),
                          expected_hardware_instruction)


class TestParserMnemonicHasLabel:
    """Test source language instructions that do have an associated label"""
    test_data = [
        ("ADD Label1", SourceInstructionWithLabel, ADD, 'Label1'),
        ("SUB Label1", SourceInstructionWithLabel, SUB, 'Label1'),
        ("STA Label1", SourceInstructionWithLabel, STA, 'Label1'),
        ("LDA Label1", SourceInstructionWithLabel, LDA, 'Label1'),
        ("BRA Label1", SourceInstructionWithLabel, BRA, 'Label1'),
        ("BRZ Label1", SourceInstructionWithLabel, BRZ, 'Label1'),
        ("BRP Label1", SourceInstructionWithLabel, BRP, 'Label1'),
    ]

    @pytest.mark.parametrize(
        "test_source_instruction,  expected_source_instruction_type, expected_hardware_instruction, expected_label",
        test_data)
    def test_mnemonic_that_has_a_label(self, test_source_instruction, expected_source_instruction_type,
                                       expected_hardware_instruction,
                                       expected_label):
        """Test the parser correctly determines when a source language instruction has an associated
        label - ADD, SUB, STA, LDA, BRA, BRZ and BRP"""

        # Given a test-source-instruction

        # When the test-source-instruction is parsed
        parser = Parser()
        result = parser.parse_source_instruction(test_source_instruction)

        # Then I should get the expected-source-instruction-type
        assert isinstance(result, expected_source_instruction_type)

        # And I should also get the corresponding expected_hardware_instruction
        assert isinstance(result.get_instruction(),
                          expected_hardware_instruction)

        # And I should also get the corresponding expected-label
        assert result.get_label() == expected_label

        # And I should also see that the instruction does not yet have an address corresponding to the label
        assert result.get_instruction().get_address() is None


class TestParserMnemonicIsDat:
    """Test source language DAT instruction"""

    test_data = [
        ("DAT", SourceInstructionDat, DAT, 0),
        ("DAT 1", SourceInstructionDat, DAT, 1),
    ]

    @pytest.mark.parametrize(
        "test_dat_source_instruction,  expected_source_instruction_type, expected_dat_hardware_instruction, expected_value",
        test_data)
    def test_mnemonic_dat_with_without_value(self, test_dat_source_instruction, expected_source_instruction_type,
                                             expected_dat_hardware_instruction, expected_value):
        """Test the parser correctly determines when a DAT source language instruction, has or does
        not have an associated value"""

        # Given a test_dat_source_instruction

        # When the test-dat-source-instruction is parsed
        parser = Parser()
        result = parser.parse_source_instruction(
            test_dat_source_instruction)

        # Then I should get the corresponding expected-source-instruction-type
        assert isinstance(result, expected_source_instruction_type)

        # And I should also get the corresponding expected-dat-hardware-instruction
        assert isinstance(result.get_instruction(),
                          expected_dat_hardware_instruction)

        # And I should also get the corresponding expected-value for the DAT instruction
        assert result.get_instruction().get_code() == expected_value


class TestParserMnemonicHasError:
    """Test source language instructions that have an error"""

    test_data = [
        ("     ", SourceInstructionError,
         'Number of tokens must be between 1 and 3, found -> 0 <- tokens'),  # String has no tokens
        ('TOKEN1 TOKEN2  TOKEN3   TOKEN4    ', SourceInstructionError,
         'Number of tokens must be between 1 and 3, found -> 4 <- tokens'),  # String has 4 tokens
        ('LABEL', SourceInstructionError,
         'Label without following mnemonic -> LABEL'),  # String has just a label
        # String has just a label
        ('LABEL    BAD', SourceInstructionError,
         'Token is not recognized -> BAD'),
        # String has mnemonic but has missing label
        ('LDA', SourceInstructionError,
         'Mnemonic with label should be 2 tokens, but found -> 1'),
        # String has mnemonic with unexpected label
        ('INP TOKEN', SourceInstructionError,
         'Expected 1 token, but found -> INP TOKEN'),
        # String has mnemonic with mnemonic instead of a label
        ('LDA LDA', SourceInstructionError,
         'Second token must be a label, but found -> LDA'),
        # String has DAT mnemonic with number following it
        ('DAT TOKEN', SourceInstructionError,
         'DAT value must be a number, but found -> TOKEN'),
        # String has DAT mnemonic with more than one number following it
        ('DAT 1 2', SourceInstructionError,
         'Mnemonic DAT should be 1 or 2 tokens, but found -> 3'),
    ]

    @pytest.mark.parametrize(
        "test_source_instruction_containing_error,  expected_source_instruction_error, expected_error_message",
        test_data)
    def test_mnemonic_has_error(self, test_source_instruction_containing_error, expected_source_instruction_error,
                                expected_error_message):
        """Test the parser parses an erroneous source language instruction, and gives the
        corresponding error message"""

        # Given a test-source-instruction-containing-error

        # When the test_source-instruction-containing-error is parsed
        parser = Parser()
        result = parser.parse_source_instruction(
            test_source_instruction_containing_error)

        # Then I should get the corresponding expected-source-instruction-error
        assert isinstance(result, expected_source_instruction_error)

        # And I should also get the corresponding expected-error-message
        assert result.get_message() == expected_error_message
