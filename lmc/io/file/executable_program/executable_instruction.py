class ExecutableItem:
    """An executable item, has an index in an executable program or its file representation

    This is it's position in that program or file representation

    The index can be used, when an error is encountered with a executable opcode in a file, so we can
    identify, where the error is at"""

    def __init__(self):
        self.index = None

    def set_index(self, index: int) -> None:
        self.index = str(index)

    def get_index(self) -> str:
        if self.index is None:
            raise Exception('Index is not set')
        return self.index


class ExecutableInstruction(ExecutableItem):
    """An instruction capable of being executed by the computer

     It is primarily a executable_program 'opcode', which is an integer number"""

    def __init__(self, opcode: int):
        super().__init__()
        self.opcode = opcode

    def get_opcode(self) -> int:
        return self.opcode


class ExecutableInstructionError(ExecutableItem):
    """Represents an error encountered, in getting an executable instruction from a program file"""

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self) -> str:
        return self.message

    def __str__(self) -> str:
        if self.index:
            return f'Index {self.get_index():>3} - ' + self.message
        return self.message
