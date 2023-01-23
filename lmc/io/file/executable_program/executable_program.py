from typing import List

from lmc.computer.memory_image import MemoryImage
from .executable_instruction import ExecutableInstruction, ExecutableInstructionError


class ExecutableProgram:
    """
    An executable program, is the list of executable instructions, including any errors
    found with the instructions
    """
    _max_size = 100

    def __init__(self):
        self.executable_instructions: List[ExecutableInstruction] = []

    @staticmethod
    def get_max_size() -> int:
        """Get the maximum number of executable_program opcodes that can be allocated"""
        return ExecutableProgram._max_size

    def has_errors(self) -> bool:
        """Determine if the executable instructions contains any errors"""
        for binary_opcode in self.executable_instructions:
            if isinstance(binary_opcode, ExecutableInstructionError):
                return True
        return False

    def get_list_errors(self) -> List[str]:
        """Get a list of the errors, found with the instructions"""
        errors = []
        for binary_opcode in self.executable_instructions:
            if isinstance(binary_opcode, ExecutableInstructionError):
                errors.append(binary_opcode)
        return errors

    def append(self, executable_instruction: ExecutableInstruction):
        """Append an executable instruction"""
        if len(self) > ExecutableProgram._max_size:
            raise Exception(
                f'Binary opcodes exceed max size of {ExecutableProgram._max_size} opcodes')
        return self.executable_instructions.append(executable_instruction)

    def __getitem__(self, index: int) -> str:
        return self.executable_instructions[index]

    def __len__(self) -> int:
        return len(self.executable_instructions)

    def is_empty(self):
        return not self.executable_instructions

    def get_memory_image(self):
        if self.has_errors():
            raise Exception("Cannot create memory image as program has errors")
        if self.is_empty():
            raise Exception("Cannot create memory image as program is empty")

        memory_image = MemoryImage()
        for executable_instruction in self.executable_instructions:
            memory_image.append(int(executable_instruction.get_opcode()))
        return memory_image
