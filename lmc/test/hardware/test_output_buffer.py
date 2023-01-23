from lmc.hardware.out_buffer import OutBuffer
from lmc.test.util.temp_file import TempFile
import pytest


class TestOutBuffer:
    def test_trying_to_get_value_when_empty_gives_error(self):
        # Given an initial instance of an output buffer

        out_buffer = OutBuffer()

        # When I try to get a value from it - for testing

        # Then I should get an error

        error_message = r'No value set in output buffer'
        with pytest.raises(Exception, match=error_message):
            out_buffer.get_value_for_test()

    def test_trying_to_get_value_when_it_has_one(self):
        # Given an initial instance of an output buffer, that has a single value

        out_buffer = OutBuffer()
        out_buffer.write_value(5)

        # When I try to get a value from it - for testing

        # Then I should get the value it contains

        assert out_buffer.get_value_for_test() == 5

    def test_writing_a_single_value_to_a_file(self):
        # Given an initial instance of an output buffer, that is configured to write to a file

        temp_file = TempFile()
        out_buffer = OutBuffer(temp_file.get_filename())

        # When I write a value to the output buffer

        # Then I can retrieve the value from the file

        try:
            out_buffer.write_value(101)
            value_written = temp_file.read()
            assert value_written == '101'
        finally:
            temp_file.delete()

    def test_writing_a_two_values_to_a_file(self):
        # Given an initial instance of an output buffer, that is configured to write to a file

        temp_file = TempFile()
        out_buffer = OutBuffer(temp_file.get_filename())

        # When I write two values to the output buffer

        # Then I can retrieve the values from the file

        try:
            out_buffer.write_value(5)
            out_buffer.write_value(101)
            values_written = temp_file.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 2
            assert values_written[0] == '5'
            assert values_written[1] == '101'
        finally:
            temp_file.delete()
