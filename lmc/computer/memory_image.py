import io


class MemoryImage:
    """
    Image of a program that resides in computer memory, contains opcodes the computer can execute.

    These opcodes are represented as integer numbers.
    """

    _max_size = 100

    def __init__(self):
        self.opcodes: list[int] = []

    @staticmethod
    def get_max_size():
        return MemoryImage._max_size

    def append(self, opcode: int):
        if len(self) > MemoryImage._max_size:
            raise Exception(
                f'Program exceeds max size of {MemoryImage._max_size} opcodes')
        return self.opcodes.append(opcode)

    def __setitem__(self, index: int, opcode: int):
        self.opcodes[index] = opcode

    def __getitem__(self, index: int) -> int:
        return self.opcodes[index]

    def __len__(self) -> int:
        return len(self.opcodes)

    def __str__(self):
        output = io.StringIO()

        # Memory rows except the last one
        for opcode in self.opcodes:
            print(f'{opcode:03}',  end='\n', file=output)

        contents = output.getvalue()
        output.close()
        return contents
