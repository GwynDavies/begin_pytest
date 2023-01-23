from lmc.hardware.inp_buffer import InpBuffer
from lmc.test.util.temp_file import TempFile


class TestInpBuffer:
    def test_get_single_value_when_using_temp_file(self):
        """Test setting the input buffer with a single value using a temporary file

        This is used primarily to facilitate automated testing"""

        # Given a temporary file, containing a single integer value

        temp_file = TempFile()
        temp_file.writeln('123')

        # When I create an input buffer using this temporary file

        inp_buffer = InpBuffer(temp_file.get_filename())

        # Then I can retrieve this value from the input buffer

        try:
            assert inp_buffer.get_value() == 123
        finally:
            temp_file.delete()

    def test_get_two_values_when_using_temp_file(self):
        """Test setting the input buffer with two values using a temporary file

         This is used primarily to facilitate automated testing"""

        # Given a temporary file, containing two integer values

        temp_file = TempFile()
        temp_file.writeln('123')
        temp_file.appendln('456')

        # When I create an input buffer using this temporary file

        inp_buffer = InpBuffer(temp_file.get_filename())

        # Then I can retrieve these values from the input buffer in order

        try:
            assert inp_buffer.get_value() == 123
            assert inp_buffer.get_value() == 456
        finally:
            temp_file.delete()

    def test_get_multi_values_when_using_temp_file(self):
        """Test setting the input buffer with multiple values using a temporary file

         This is used primarily to facilitate automated testing"""

        # Given a temporary file, containing multiple integer values

        temp_file = TempFile()
        temp_file.writeln('2')
        temp_file.appendln('3')
        temp_file.appendln('0')

        # When I create an input buffer using this temporary file

        inp_buffer = InpBuffer(temp_file.get_filename())

        # Then I can retrieve these values from the input buffer in order

        try:
            assert inp_buffer.get_value() == 2
            assert inp_buffer.get_value() == 3
            assert inp_buffer.get_value() == 0
        finally:
            temp_file.delete()
