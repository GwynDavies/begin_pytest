from lmc.assembler.symbol_table import SymbolTable
from lmc.io.file.source_pprogram.source_instruction import SourceInstructionNoLabel, SourceInstructionWithLabel, SourceInstructionDat
from lmc.computer.memory_image import MemoryImage
from lmc.io.file.source_pprogram.source_program import SourceProgram


class PassTwo():
    def __init__(self):
        self.internal_program = MemoryImage()

    def assemble_source_instructions(self, symbol_table: SymbolTable, source_program: SourceProgram) -> MemoryImage:
        for source_instruction in source_program:
            if isinstance(source_instruction, SourceInstructionNoLabel):
                self._encode_instruction_no_label(source_instruction)

            elif isinstance(source_instruction, SourceInstructionWithLabel):
                self._encode_instruction_with_label(
                    source_instruction, symbol_table)

            elif isinstance(source_instruction, SourceInstructionDat):
                self._encode_instruction_no_label(source_instruction)

            else:
                raise Exception('Source instruction not recognized')

        return self.internal_program

    def _encode_instruction_no_label(self, source_instruction):
        instruction = source_instruction.get_instruction()

        encoded_instruction = instruction.get_code()

        self.internal_program.append(encoded_instruction)

    def _encode_instruction_with_label(self, source_instruction, symbol_table):
        label = source_instruction.get_label()
        address = symbol_table[label]

        source_instruction = source_instruction.get_instruction()
        source_instruction.set_address(address)

        encoded_instruction = source_instruction.get_code()

        self.internal_program.append(encoded_instruction)
