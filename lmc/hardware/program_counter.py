class ProgramCounter():
    """
    The internal computer program, used during the execution of internal computer instructions
    """

    def __init__(self):
        self.value = 0

    def get_value(self):
        current_value = self.value
        self.value += 1
        return current_value

    def debug_get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
