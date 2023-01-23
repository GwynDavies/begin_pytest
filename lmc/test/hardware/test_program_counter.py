from lmc.hardware.program_counter import ProgramCounter


class TestProgramCounter:
    def test_initial_value(self):
        # Give a new program counter

        program_counter = ProgramCounter()

        # Then the current value is 0

        assert program_counter.debug_get_value() == 0

    def test_set_value(self):
        # Give a new program counter

        program_counter = ProgramCounter()

        # When I set its value

        program_counter.set_value(5)

        # Then each time I get its value, it is incremented by 1 after I have got its value

        assert program_counter.get_value() == 5
        assert program_counter.get_value() == 6
        assert program_counter.get_value() == 7
