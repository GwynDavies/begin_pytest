# pylint: disable=redefined-outer-name
# Above required to prevent PYlint warning: W0621: Redefining name 'fixture_processor' from outer scope (line ..) (redefined-outer-name)

import pytest

from lmc.hardware.accumulator import Accumulator
from lmc.hardware.inp_buffer import InpBuffer
from lmc.hardware.memory import Memory
from lmc.hardware.out_buffer import OutBuffer
from lmc.hardware.processor import Processor
from lmc.hardware.program_counter import ProgramCounter
from lmc.test.util.temp_file import TempFile


@pytest.fixture
def fixture_processor():
    """Create a processor instance, with the program counter, memory, accumulator, input buffer and output buffer"""
    program_counter = ProgramCounter()
    memory = Memory()
    accumulator = Accumulator()
    inp_buffer = InpBuffer()
    out = OutBuffer()
    processor = Processor(program_counter, memory,
                          accumulator, inp_buffer, out)
    return processor


@pytest.fixture
def fixture_processor_with_example_program_1(fixture_processor):
    """Create a processor instance, with a test program loaded into the processor memory

    The example program does the following :

        Inputs a value
        Store the value into memory
        Loads the value back from memory into the accumulator
        Branch to step to the end of the program
        Outputs the value"""

    temp_file = TempFile()
    temp_file.writeln('5')

    processor = fixture_processor

    processor.get_input_buffer().set_file_to_read_from(temp_file.get_filename())

    memory = processor.get_memory()
    memory.set_value(0, 901)  # INP
    memory.set_value(1, 306)  # STA 6
    memory.set_value(2, 506)  # LDA 6
    memory.set_value(3, 902)  # OUT
    # BRA - not really needed, just to have a simple branch instruction
    memory.set_value(4, 605)
    memory.set_value(5, 0)  # HLT
    # DAT 0 - memory location to store and retrieve a value to
    memory.set_value(6, 0)

    expected_output_value = 5
    return processor, temp_file, expected_output_value


@pytest.fixture
def fixture_processor_with_example_program_2(fixture_processor):
    """Create a processor instance, with a test program loaded into the processor memory

    The example program does the following :

        Inputs a value
        Store the value into memory
        Loads the value back from memory into the accumulator
        Branch-if-positive to step to the end of the program
        Outputs the value"""

    processor = fixture_processor

    # Place value in the input buffer, so the user is not prompted
    temp_file = TempFile()
    temp_file.writeln('5')
    processor.get_input_buffer().set_file_to_read_from(temp_file.get_filename())

    memory = processor.get_memory()
    memory.set_value(0, 901)  # INP
    memory.set_value(1, 306)  # STA 6
    memory.set_value(2, 506)  # LDA 6
    # BRP - not really needed, just to have a simple branch-if-positive instruction
    memory.set_value(3, 804)
    memory.set_value(4, 902)  # OUT
    memory.set_value(5, 0)  # HLT
    memory.set_value(6, 0)  # DAT

    expected_output_value = 5
    return processor, temp_file, expected_output_value


@pytest.fixture
def fixture_processor_with_example_program_3(fixture_processor):
    """Create a processor instance, with a test program loaded into the processor memory

    The example program does the following :

        Inputs a value
        Store the value into memory
        Loads the value back from memory into the accumulator
        Branch-if-zero to step to the end of the program
        Outputs the value"""

    processor = fixture_processor

    # Place value in the input buffer, so the user is not prompted
    temp_file = TempFile()
    temp_file.writeln('5')
    processor.get_input_buffer().set_file_to_read_from(temp_file.get_filename())

    memory = processor.get_memory()
    memory.set_value(0, 901)  # INP
    memory.set_value(1, 306)  # STA 6
    memory.set_value(2, 506)  # LDA 6
    # BRZ - not really needed, just to have a simple branch-if-zero instruction
    memory.set_value(3, 704)
    memory.set_value(4, 902)  # OUT
    memory.set_value(5, 0)  # HLT
    memory.set_value(6, 0)  # DAT

    expected_output_value = 5
    return processor, temp_file, expected_output_value


@pytest.fixture
def fixture_processor_with_example_program_4(fixture_processor):
    """Create a processor instance, with a test program loaded into the processor memory

    The example program does the following :

        Input a value to the accumulator
        Store the value to memory
        Add the value back to the accumulator, so it is now doubled
        Add the value back to the accumulator, so it is now tripled
        Subtract the value from the accumulator is it is again only doubled
        Output the value from the accumulator"""
    processor = fixture_processor

    # Place value in the input buffer, so the user is not prompted
    temp_file = TempFile()
    temp_file.writeln('5')
    processor.get_input_buffer().set_file_to_read_from(temp_file.get_filename())

    memory = processor.get_memory()
    memory.set_value(0, 901)  # INP value to accumulator
    memory.set_value(1, 307)  # STA value into location 7
    memory.set_value(2, 107)  # ADD value from location 7 to accumulator
    # ADD value again from location 7 to accumulator, so it is now tripled
    memory.set_value(3, 107)
    # SUB value from location 7 from accumulator, so it is now only doubled
    memory.set_value(4, 207)
    memory.set_value(5, 902)  # OUT value from accumulator
    memory.set_value(6, 0)  # HLT
    memory.set_value(7, 0)  # DAT 0

    expected_output_value = 10
    return processor, temp_file, expected_output_value
