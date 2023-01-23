class Accumulator:
    """
    Holds values for calculations
    """

    def __init__(self):
        self.value = 0

    def get_value(self) -> int:
        return self.value

    def set_value(self, value: int):
        self.value = value
