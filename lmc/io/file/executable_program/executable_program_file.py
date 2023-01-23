from __future__ import annotations
from typing import Union
import io
from lmc.computer.memory_image import MemoryImage
from lmc.io.file.program_file import ProgramFile
from .executable_instruction import ExecutableInstruction, ExecutableInstructionError
from .executable_program import ExecutableProgram


class ExecutableProgramFile(ProgramFile):
    """
    An executable program file, is a stored version of an internal program, that can be
    written as a file, and read back in using a string encoding for the opcodes.
    """

    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.executable_program = ExecutableProgram()

    def write(self, internal_program: MemoryImage) -> None:
        """
        Write an internal program out as a sored executable program file.

        Do this by writing the internal program opcodes out, as 3 digit string
        representations.
        """
        with open(self.file_name, "w", encoding='ascii') as output_executable_file:
            for opcode in internal_program:
                # Write each executable_program opcode a 3 digit string opcode representation, with
                # leading zeros being padded
                output_executable_file.write(f'{opcode:03}')

    def read(self) -> None:
        """
        Read 3 digit string opcodes representations from a file
        """
        end_of_file = ''
        with open(self.file_name, encoding='ascii') as input_executable_file:
            executable_program_file_opcode = input_executable_file.read(3)

            while executable_program_file_opcode != end_of_file:
                executable_program_opcode = self.parse_external_opcode(
                    executable_program_file_opcode)
                self.executable_program.append(executable_program_opcode)
                executable_program_file_opcode = input_executable_file.read(3)

    def __getitem__(self, index: int) -> str:
        return self.executable_program[index]

    def get_executable_program(self) -> ExecutableProgram:
        return self.executable_program

    def append(self, executable_instruction: ExecutableInstruction) -> None:
        self.executable_program.append(executable_instruction)

    def __len__(self) -> int:
        """Return the length of the program file's executable program"""
        return len(self.executable_program)

    def __str__(self) -> str:
        output = io.StringIO()

        for executable_program_opcode in self.executable_program:
            print(executable_program_opcode, file=output)

        contents = output.getvalue()
        output.close()
        return contents

    def parse_external_opcode(self, opcode) -> Union[ExecutableInstruction | ExecutableInstructionError]:
        """Parse an external opcode from a file, into an internal opcode"""
        if len(opcode) != 3:
            result = ExecutableInstructionError(
                f'Opcode {opcode} is not valid, should be 3 chars')
        elif not opcode.isnumeric():
            result = ExecutableInstructionError(
                f'Opcode {opcode} is not valid, must be numeric')
        else:
            result = ExecutableInstruction(opcode)
        return result
