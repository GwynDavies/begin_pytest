from lmc.hardware.accumulator import Accumulator


class TestAccumulator():
    def test_accumulator_initial_value(self):
        """Test that the initial value of a new accumulator is 0"""

        # Given a new accumulator

        accumulator = Accumulator()

        # When I get the initial value

        # Then that value is 0

        assert accumulator.get_value() == 0

    def test_set_and_get_of_accumulator_to_integer_value(self):
        """Test that the value of an accumulator can be set to an integer value and retrieved"""
        # Given an accumulator

        accumulator = Accumulator()

        # When I set the accumulator to an integer value

        integer_test_value = 5
        accumulator.set_value(integer_test_value)

        # Then, when I retrieve its value, it is the same as it was set to

        assert accumulator.get_value() == integer_test_value

    def test_set_and_get_of_accumulator_to_a_floating_point_value(self):
        """Test that the value of an accumulator can be set to a floating point value and retrieved"""
        # Given an accumulator

        accumulator = Accumulator()

        # When I set the accumulator to an floating point value

        integer_test_value = 5.0
        accumulator.set_value(integer_test_value)

        # Then, when I retrieve its value, it is the same as it was set to

        assert accumulator.get_value() == integer_test_value
