from os.path import exists
from typing import List
from lmc.hardware.memory import Memory
from lmc.io.file.executable_program.executable_program_file import ExecutableProgramFile
from lmc.computer.loader import Loader
from lmc.test.util.test_data_opcodes import TestDataOpcodes
from lmc.test.util.test_data_file import TestDataFile
import pytest

FILE_NAME = 'test_binary_program_file.lmcb'


class TestLoader:
    @pytest.fixture
    def fixture_test_loader_opcodes(self) -> List[int]:
        return TestDataOpcodes.opcodes_subtract()

    def test_read_into_memory(self, fixture_test_loader_opcodes):
        # Give the program opcodes for a computer binary program created as a file

        test_program_opcodes = fixture_test_loader_opcodes
        executable_program_file = ExecutableProgramFile(FILE_NAME)
        executable_program_file.write(test_program_opcodes)

        assert exists(FILE_NAME)

        # When I load the file from disk into computer memory

        executable_program_file.read()
        executable_program = executable_program_file.get_executable_program()
        memory_image = executable_program.get_memory_image()
        memory = Memory()
        Loader.load_into_memory(memory_image, memory)

        # Then the computer memory should have the correct corresponding instructions loaded into the memory

        assert memory.get_value(0) == 901  # INP
        assert memory.get_value(1) == 308  # STA
        assert memory.get_value(2) == 901  # INP
        assert memory.get_value(3) == 309  # STA
        assert memory.get_value(4) == 508  # LDA
        assert memory.get_value(5) == 209  # SUB
        assert memory.get_value(6) == 902  # OUT
        assert memory.get_value(7) == 0    # HLT
        assert memory.get_value(8) == 0    # DAT 0
        assert memory.get_value(9) == 0    # DAT 0

        TestDataFile.clean_test_file_if_exists(FILE_NAME)
