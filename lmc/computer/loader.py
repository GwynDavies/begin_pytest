from lmc.computer.memory_image import MemoryImage
from lmc.hardware.memory import Memory


class Loader:
    @staticmethod
    def load_into_memory(memory_image: MemoryImage, memory: Memory):
        """
        Load an executable program into the computer memory, so it can be executed.

        To do this, we get the opcode from each of the executable program's instructions.
        """
        location: int = 0

        for opcode in memory_image:
            memory.set_value(location, opcode)
            location += 1
