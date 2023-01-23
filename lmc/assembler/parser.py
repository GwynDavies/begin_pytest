from lmc.hardware.instruction import InstructionBuilder, Id, DAT
from lmc.assembler.label import Label
from lmc.io.file.source_pprogram.source_program import SourceProgram
from lmc.io.file.source_pprogram.source_instruction import SourceInstructionNoLabel, SourceInstructionDat, SourceInstructionWithLabel, SourceInstructionError
from lmc.assembler.symbol_table import SymbolTable


class Parser:
    def __init__(self):
        self.instruction_counter = 0
        self.source_instructions = SourceProgram()
        self.symbol_table = SymbolTable()

    def get_symbol_table(self):
        return self.symbol_table

    def get_source_instructions(self):
        return self.source_instructions

    def parse_source_instruction(self, source_line):
        # Tokenize
        tokens = source_line.split()
        number_tokens = len(tokens)

        if number_tokens < 1 or number_tokens > 3:
            result = SourceInstructionError(
                "Number of tokens must be between 1 and 3, found -> " + str(number_tokens) + " <- tokens")
        else:
            result = self._parse_source_line_tokens(tokens)

        result.set_line_number(self.instruction_counter+1)
        self.source_instructions.append(result)
        return result

    def _parse_source_line_tokens(self, tokens):
        if Label.is_label(tokens[0]):
            if len(tokens) > 1:
                symbol = tokens.pop(0)
                self.symbol_table[symbol] = self.instruction_counter
            else:
                return SourceInstructionError('Label without following mnemonic -> ' + tokens[0])

        mnemonic = tokens[0]

        if Id.mnemonic_has_no_label(mnemonic):
            result = self.parse_mnemonic_no_label(tokens)
        elif Id.mnemonic_has_label(mnemonic):
            result = self.parse_mnemonic_with_label(tokens)
        elif mnemonic == 'DAT':
            result = self.parse_mnemonic_dat(tokens)
        else:
            result = SourceInstructionError(
                'Token is not recognized -> ' + mnemonic)

        self.instruction_counter += 1
        return result

    def parse_mnemonic_no_label(self, tokens):
        if len(tokens) != 1:
            result = SourceInstructionError(
                'Expected 1 token, but found -> ' + ' ' .join(tokens))
        else:
            mnemonic = tokens[0]
            result = SourceInstructionNoLabel(
                InstructionBuilder.build(Id.from_mnemonic(mnemonic)))
        return result

    def parse_mnemonic_with_label(self, tokens):
        if len(tokens) != 2:
            result = SourceInstructionError(
                'Mnemonic with label should be 2 tokens, but found -> ' + str(len(tokens)))
        else:
            mnemonic, label = tokens
            if not Label.is_label(label):
                result = SourceInstructionError(
                    'Second token must be a label, but found -> '+label)
            else:
                result = SourceInstructionWithLabel(InstructionBuilder.build(
                    Id.from_mnemonic(mnemonic)), label)
        return result

    def parse_mnemonic_dat(self, tokens):
        if len(tokens) == 1:
            instruction = DAT()
            result = SourceInstructionDat(instruction)
        elif len(tokens) == 2:
            _, value = tokens
            if value.isnumeric():
                instruction = DAT(int(value))
                result = SourceInstructionDat(instruction)
            else:
                result = SourceInstructionError(
                    'DAT value must be a number, but found -> ' + value)
        else:
            result = SourceInstructionError(
                'Mnemonic DAT should be 1 or 2 tokens, but found -> ' + str(len(tokens)))
        return result
