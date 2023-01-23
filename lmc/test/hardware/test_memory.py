from lmc.hardware.memory import Memory
import pytest


class TestMemory:
    @pytest.fixture
    def fixture_memory(self):
        return Memory()

    def test_uninitialized_memory_locations_are_set_to_zero(self, fixture_memory):
        """Test memory initial value is 0"""

        # Given an initial memory instance

        memory = fixture_memory

        # When I get the memory value at a location

        # Then the memory value is 0

        assert memory.get_value(5) == 0

    def test_setting_and_getting_memory_location_value(self, fixture_memory):
        """Test memory value can be set and retrieved"""

        # Given an initial memory instance

        memory = fixture_memory

        # When I set the value of the memory at a location

        memory.set_value(5, 101)

        # Then, when I retrieve that memory location value, I get the value it was set to

        assert memory.get_value(5) == 101

    def test_get_memory_using_python_str_method(self, fixture_memory):
        """Test I can get the contents of memory as a string"""

        # Given an initial memory instance

        memory = fixture_memory

        # When I get the contents of the memory as a string

        # Then I get a string representation of the memory with location identifiers

        expected_value = "\n" + \
                         "Memory HEX Dump : 100 cells, 0-99\n" + \
                         "\n" + \
                         "                       0                    1                    2                    3                    4\n" + \
                         "                       5                    6                    7                    8                    9\n" + \
                         "\n" + \
                         "  0                    0                    0                    0                    0                    0       0 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 10                    0                    0                    0                    0                    0      10 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 20                    0                    0                    0                    0                    0      20 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 30                    0                    0                    0                    0                    0      30 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 40                    0                    0                    0                    0                    0      40 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 50                    0                    0                    0                    0                    0      50 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 60                    0                    0                    0                    0                    0      60 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 70                    0                    0                    0                    0                    0      70 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 80                    0                    0                    0                    0                    0      80 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         " 90                    0                    0                    0                    0                    0      90 \n" + \
                         "                       0                    0                    0                    0                    0 \n" + \
                         "\n"

        assert str(memory) == expected_value
