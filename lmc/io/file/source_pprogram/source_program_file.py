import io
from lmc.io.file.program_file import ProgramFile


class SourceProgramFile(ProgramFile):
    """
    A source program file, is the collection of lines representing the source
    code, for a 'little man computer' program
    """

    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.source_instructions: [str] = []

    def read(self):
        with open(self.file_name, encoding='ascii') as source_program_file:
            for line in source_program_file:
                # Get source program line, also uppercase it
                self.source_instructions.append(line.upper())

    def __getitem__(self, index: int) -> str:
        return self.source_instructions[index]

    def __len__(self) -> int:
        return len(self.source_instructions)

    def __str__(self) -> str:
        output = io.StringIO()

        for source_instruction in self.source_instructions:
            print(source_instruction.rstrip(), file=output)

        contents = output.getvalue()
        output.close()
        return contents
