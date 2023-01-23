import os.path
from lmc.computer.computer import Computer
from lmc.test.util.temp_file import TempFile
import pytest


class TestComputerWithExamplePrograms:
    @pytest.fixture
    def this_tests_directory(self):
        test_files_directory = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(test_files_directory, 'lmcb_test_files')

    def test_example_program_add_numbers(self, this_tests_directory):
        # Given a file path that is program that has opcodes to add two numbers, and a computer

        test_file = os.path.join(this_tests_directory, 'add_numbers.lmcb')
        computer = Computer()

        # When I try to run the file on the computer, and I place two numbers in the computer input buffer

        input_buffer = computer.get_processor().get_input_buffer()
        temp_file_inp = TempFile()
        temp_file_inp.writeln('3')
        temp_file_inp.appendln('4')
        input_buffer.set_file_to_read_from(temp_file_inp.get_filename())

        # Then I see the correct value was written in the output buffer

        output_buffer = computer.get_processor().get_output_buffer()
        temp_file_out = TempFile()
        output_buffer.set_file_to_write_to(temp_file_out.get_filename())

        try:
            computer.run(test_file)
            values_written = temp_file_out.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 1
            assert values_written[0] == '7'
        finally:
            temp_file_inp.delete()
            temp_file_out.delete()

    def test_example_program_count_down(self, this_tests_directory):
        # Given a file path that is program that has opcodes to count down from a number to zero, and a computer

        test_file = os.path.join(this_tests_directory, 'count_down.lmcb')

        # When I try to run the file on the computer, and I place two numbers in the computer input buffer

        computer = Computer()
        input_buffer = computer.get_processor().get_input_buffer()
        temp_file_inp = TempFile()
        temp_file_inp.writeln('10')
        input_buffer.set_file_to_read_from(temp_file_inp.get_filename())

        # Then I see the correct values were written in the output buffer

        output_buffer = computer.get_processor().get_output_buffer()
        temp_file_out = TempFile()
        output_buffer.set_file_to_write_to(temp_file_out.get_filename())

        try:
            computer.run(test_file)
            values_written = temp_file_out.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 11
            assert values_written[0] == '10'
            assert values_written[1] == '9'
            assert values_written[2] == '8'
            assert values_written[3] == '7'
            assert values_written[4] == '6'
            assert values_written[5] == '5'
            assert values_written[6] == '4'
            assert values_written[7] == '3'
            assert values_written[8] == '2'
            assert values_written[9] == '1'
            assert values_written[10] == '0'
        finally:
            temp_file_inp.delete()
            temp_file_out.delete()

    def test_example_print_self(self, this_tests_directory):
        # Given a file path that is program that has opcodes to print the program itself, and a computer

        test_file = os.path.join(this_tests_directory, 'print_self.lmcb')

        computer = Computer()

        # When I try to run the file on the computer

        # Then I see the correct values were written in the output buffer

        output_buffer = computer.get_processor().get_output_buffer()
        temp_file_out = TempFile()
        output_buffer.set_file_to_write_to(temp_file_out.get_filename())

        try:
            computer.run(test_file)
            values_written = temp_file_out.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 10
            assert values_written[0] == '500'
            assert values_written[1] == '902'
            assert values_written[2] == '209'
            assert values_written[3] == '709'
            assert values_written[4] == '500'
            assert values_written[5] == '109'
            assert values_written[6] == '300'
            assert values_written[7] == '600'
            assert values_written[8] == '0'
            assert values_written[9] == '1'
        finally:
            temp_file_out.delete()

    def test_example_program_square_a_number(self, this_tests_directory):
        # Given a file path that is program that has opcodes to square a number, and a computer

        test_file = os.path.join(this_tests_directory, 'square.lmcb')

        computer = Computer()

        # When I try to run the file on the computer, and I place a number in the computer input buffer

        input_buffer = computer.get_processor().get_input_buffer()
        temp_file_inp = TempFile()
        temp_file_inp.writeln('2')
        temp_file_inp.appendln('3')
        temp_file_inp.appendln('0')
        input_buffer.set_file_to_read_from(temp_file_inp.get_filename())

        # Then I see the correct value was written in the output buffer

        output_buffer = computer.get_processor().get_output_buffer()
        temp_file_out = TempFile()
        output_buffer.set_file_to_write_to(temp_file_out.get_filename())

        try:
            computer.run(test_file)
            values_written = temp_file_out.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 2
            assert values_written[0] == '4'
            assert values_written[1] == '9'
        finally:
            temp_file_inp.delete()
            temp_file_out.delete()

    def test_sub_two_numbers(self, this_tests_directory):
        # Given a file path that is program that has opcodes to subtract two numbers, and a computer

        test_file = os.path.join(this_tests_directory, 'sub_numbers.lmcb')

        computer = Computer()

        # When I try to run the file on the computer, and I place two numbers in the computer input buffer

        input_buffer = computer.get_processor().get_input_buffer()
        temp_file_inp = TempFile()
        temp_file_inp.writeln('10')
        temp_file_inp.appendln('6')
        input_buffer.set_file_to_read_from(temp_file_inp.get_filename())

        # Then I see the correct value was written in the output buffer

        output_buffer = computer.get_processor().get_output_buffer()
        temp_file_out = TempFile()
        output_buffer.set_file_to_write_to(temp_file_out.get_filename())

        try:
            computer.run(test_file)
            values_written = temp_file_out.read()
            values_written = values_written.split("\n")
            assert len(values_written) == 1
            assert values_written[0] == '4'
        finally:
            temp_file_inp.delete()
            temp_file_out.delete()
