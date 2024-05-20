import io
from typing import List


class Memory:
    """
    The internal computer memory, which is 100 integer cells - initialized to zeros
    """

    def __init__(self):
        self.size = 100
        self.cells: List[int] = []
        # Initialize memory to all zeros
        self.cells = [0 for i in range(self.size)]

    def get_value(self, address: int) -> int:
        return self.cells[address]

    def set_value(self, address: int, value: int):
        self.cells[address] = value

    def __str__(self):
        def format_cell_value(memory_cell_value: int) -> str:
            value = hex(memory_cell_value)
            return value.replace("0x", "  ").upper()

        output = io.StringIO()

        print("", file=output)
        print("Memory HEX Dump : 100 cells, 0-99", file=output)
        print("", file=output)
        # Header
        print("                       0                    1                    2                    3                    4", file=output)
        print("                       5                    6                    7                    8                    9", file=output)
        print("", file=output)

        # Memory rows except the last one
        for cell_row in range(10):
            print(f'{cell_row*10:3} ', end='', file=output)
            # First 5 row cells
            for cell_counter in range(5):
                cell_offset = (cell_row*10) + cell_counter
                value = format_cell_value(self.cells[cell_offset])
                print(f'  {value:>18} ',  end='', file=output)
            print(f'    {cell_row*10:3} ', end='', file=output)
            print(file=output)

            print('    ', end='', file=output)
            # Second 5 row cells
            for cell_counter in range(5, 10):
                cell_offset = (cell_row*10) + cell_counter
                value = format_cell_value(self.cells[cell_offset])
                print(f'  {value:>18} ',  end='', file=output)
            print(file=output)

        # Footer
        print("", file=output)

        contents = output.getvalue()
        output.close()
        return contents
