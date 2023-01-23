from .parser import Parser
from .symbol_table import SymbolTable
from ..io.file.source_pprogram.source_program import SourceProgram


class PassOne():
    """
    First pass of the assembler, converts a source program file, into a source program
    """

    def __init__(self):
        self.parser = Parser()

    def decode_source_program_file(self, source_program_file):
        # Decode each of the source instruction file lines, in the file
        for source_instruction in source_program_file:
            self.decode_source_line(source_instruction)

    def get_source_program(self) -> SourceProgram:
        return self.parser.get_source_instructions()

    def get_symbol_table(self) -> SymbolTable:
        return self.parser.get_symbol_table()

    def decode_source_line(self, source_line: str):
        self.parser.parse_source_instruction(source_line)
