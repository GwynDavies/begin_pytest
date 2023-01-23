from os import path

from lmc.assembler.pass_one import PassOne
from lmc.hardware.instruction import INP, OUT, DAT, BRZ, SUB, BRA, HLT
from lmc.io.file.source_pprogram.source_program_file import SourceProgramFile


class TestPassOne:
    """Test the assembler can perform the 'pass one' stage"""

    def test_stage_pass_one_can_decode_a_source_program_file(self):
        # Given a source program file
        test_file_path = path.join(path.dirname(
            __file__), 'test_pass_one_source_program_file.lmcs')
        source_program_file = SourceProgramFile(test_file_path)
        source_program_file.read()

        # When I use the assembler 'pass one' stage to decode the source program file
        pass_one = PassOne()
        pass_one.decode_source_program_file(source_program_file)
        source_program = pass_one.get_source_program()

        # Then I should get the corresponding source program instructions
        source_program = pass_one.get_source_program()
        assert source_program.has_errors() is False

        assert isinstance(source_program[0].get_instruction(), INP)
        assert isinstance(source_program[1].get_instruction(), OUT)
        assert isinstance(source_program[2].get_instruction(), BRZ)
        assert isinstance(source_program[3].get_instruction(), SUB)
        assert isinstance(source_program[4].get_instruction(), OUT)
        assert isinstance(source_program[5].get_instruction(), BRA)
        assert isinstance(source_program[6].get_instruction(), HLT)
        assert isinstance(source_program[7].get_instruction(), DAT)
        assert isinstance(source_program[8].get_instruction(), DAT)

        # And I should get the corresponding symbol table for the source instructions
        symbol_table = pass_one.get_symbol_table()
        assert len(symbol_table) == 4
        assert symbol_table['LOOP'] == 2
        assert symbol_table['ONE'] == 7
        assert symbol_table['QUIT'] == 6
        assert symbol_table['TWO'] == 8
