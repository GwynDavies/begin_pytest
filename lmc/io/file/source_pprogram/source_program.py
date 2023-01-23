from __future__ import annotations
from typing import List, Union
from .source_instruction import SourceInstructionNoLabel, SourceInstructionWithLabel, SourceInstructionDat, SourceInstructionError


class SourceProgram:
    """
    A source program, is the list of source instructions, including any errors found
    """

    _max_size = 100

    def __init__(self):
        self.source_instructions: List[
            Union[SourceInstructionNoLabel | SourceInstructionWithLabel | SourceInstructionDat | SourceInstructionError]] = []

    @staticmethod
    def get_max_size():
        return SourceProgram._max_size

    def has_errors(self):
        for source_instruction in self.source_instructions:
            if isinstance(source_instruction, SourceInstructionError):
                return True
        return False

    def get_list_errors(self) -> List[str]:
        errors = []
        for source_instruction in self.source_instructions:
            if isinstance(source_instruction, SourceInstructionError):
                errors.append(source_instruction)
        return errors

    def append(self, source_instruction: Union[
            SourceInstructionNoLabel | SourceInstructionWithLabel | SourceInstructionDat | SourceInstructionError]):
        if len(self) > SourceProgram._max_size:
            raise Exception(
                f'Source instructions exceed max size of {SourceProgram._max_size} instructions')
        return self.source_instructions.append(source_instruction)

    def __getitem__(self, index: int) -> Union[
            SourceInstructionNoLabel | SourceInstructionWithLabel | SourceInstructionDat | SourceInstructionError]:
        return self.source_instructions[index]

    def __len__(self) -> int:
        return len(self.source_instructions)
