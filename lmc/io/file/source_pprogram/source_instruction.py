class SourceItem:
    def __init__(self):
        self.line_number = None

    def set_line_number(self, line_number: int):
        self.line_number = str(line_number)

    def get_line_number(self) -> str:
        if self.line_number is None:
            raise Exception('Line number is not set')
        return self.line_number


class SourceInstructionNoLabel(SourceItem):
    def __init__(self, instruction):
        super().__init__()
        self.instruction = instruction

    def get_instruction(self):
        return self.instruction


class SourceInstructionWithLabel(SourceItem):
    def __init__(self, instruction, label):
        super().__init__()
        self.instruction = instruction
        self.label = label

    def get_instruction(self):
        return self.instruction

    def get_label(self):
        return self.label


class SourceInstructionDat(SourceItem):
    def __init__(self, instruction):
        super().__init__()
        self.instruction = instruction

    def get_instruction(self):
        return self.instruction


class SourceInstructionError(SourceItem):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_message(self) -> str:
        return self.message

    def __str__(self) -> str:
        return f'Line {self.get_line_number():>3} - ' + self.message
