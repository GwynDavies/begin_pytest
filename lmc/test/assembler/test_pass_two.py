from lmc.assembler.pass_one import PassOne
from lmc.assembler.pass_two import PassTwo

import pytest


class TestPassTwo:
    """Test the assembler can perform the 'pass stage' stage"""

    @pytest.fixture
    def fixture_pass_one(self):
        # Source program
        pass_one = PassOne()
        pass_one.decode_source_line('      INP')
        pass_one.decode_source_line('      OUT')
        pass_one.decode_source_line('LOOP  BRZ QUIT')
        pass_one.decode_source_line('SUB   ONE')
        pass_one.decode_source_line('      OUT')
        pass_one.decode_source_line('      BRA LOOP')
        pass_one.decode_source_line('QUIT  HLT')
        pass_one.decode_source_line('ONE   DAT 1')
        pass_one.decode_source_line('TWO   DAT')

        # Get the corresponding symbol table for the source instructions processed by "pass one"
        return pass_one

    def test_encode(self, fixture_pass_one):
        # Given a setup 'pass one'  that provides valid source instructions and corresponding symbol table
        symbol_table = fixture_pass_one.get_symbol_table()
        source_program = fixture_pass_one.get_source_program()

        # When I create a Pass Two and use it to encode the source instructions using the symbol table

        pass_two = PassTwo()
        program = pass_two.assemble_source_instructions(
            symbol_table, source_program)

        # Then I should get the corresponding Binary Program

        assert len(program) == 9
        assert program[0] == 901
        assert program[1] == 902
        assert program[2] == 706
        assert program[3] == 207
        assert program[4] == 902
        assert program[5] == 602
        assert program[6] == 0
        assert program[7] == 1
        assert program[8] == 0

    def test_encode_bad_source_instruction(self):
        # Given the source_instructions that would have come from Pass One
        source_instructions = [None]

        # When I try to encode those source instructions with Pass Two

        # Then I should get an exception
        with pytest.raises(Exception, match=r'Source instruction not recognized'):
            pass_two = PassTwo()
            symbol_table = None
            pass_two.assemble_source_instructions(
                symbol_table, source_instructions)
