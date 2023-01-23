from lmc.hardware.memory import Memory
from lmc.hardware.program_counter import ProgramCounter
from lmc.hardware.accumulator import Accumulator
from lmc.hardware.inp_buffer import InpBuffer
from lmc.hardware.out_buffer import OutBuffer
from lmc.hardware.processor import Processor
from lmc.io.file.executable_program.executable_program_file import ExecutableProgramFile
from lmc.application.error_fatal import ErrorFatal
from .loader import Loader


class Computer():
    """
    Emulate a computer, that can load and run an executable program file.
    """

    def __init__(self):
        self.program_counter = ProgramCounter()
        self.memory = Memory()
        self.accumulator = Accumulator()
        self.inp_buffer = InpBuffer()
        self.out = OutBuffer()

        self.processor = Processor(
            self.program_counter, self.memory, self.accumulator, self.inp_buffer, self.out)

    def get_processor(self):
        return self.processor

    def run(self, executable_program_file_name):
        """
        Load an executable program file into the computer memory, and run it with
        the computer processor.
        """

        memory = self.processor.get_memory()

        # Load the executable program file
        executable_program_file = ExecutableProgramFile(
            executable_program_file_name)

        # Exit if the executable program file does not exist
        if not executable_program_file.exists():
            ErrorFatal.exit_file_not_found(executable_program_file_name)

        # Exit if the executable program file is empty
        if executable_program_file.is_empty():
            ErrorFatal.exit_file_is_empty(executable_program_file_name)

        # Get the executable program from the executable program file
        executable_program_file.read()
        executable_program = executable_program_file.get_executable_program()

        # Exit if there are errors in the executable program
        if executable_program.has_errors():
            ErrorFatal.exit_fatal_errors(executable_program.get_list_errors())

        # Get a memory image from the executable program
        memory_image = executable_program.get_memory_image()

        # Load the executable program into memory
        Loader.load_into_memory(memory_image, memory)

        # Perform a memory dump of the loaded executable program
        print(str(self.memory))

        # Now run the loaded executable program
        self.processor.run_program()
