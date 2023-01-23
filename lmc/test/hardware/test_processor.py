import io
import sys

from lmc.hardware.instruction import ADD, SUB, STA, LDA, BRA, BRZ, BRP, INP, OUT, DAT
from lmc.test.util.temp_file import TempFile


class TestProcessorProcessInstructions:
    def test_instruction_add(self, fixture_processor):
        # Given a processor and a value in memory

        processor = fixture_processor
        processor.get_memory().set_value(0, 123)

        # When I use the processor to perform an ADD instruction using the value in memory

        address = 0
        processor.process_instruction(ADD(address))

        # Then the accumulator has the value, as it was initially zero

        assert processor.get_accumulator().get_value() == 123

    def test_instruction_sub(self, fixture_processor):
        # Given a processor and a value in memory and a value in the accumulator

        processor = fixture_processor
        processor.get_accumulator().set_value(124)
        processor.get_memory().set_value(0, 123)

        # When I use the processor to perform a SUB instruction using the value in memory

        address = 0
        processor.process_instruction(SUB(address))

        # Then the accumulator has the result of the subtraction

        assert processor.get_accumulator().get_value() == 1

    def test_instruction_sta(self, fixture_processor):
        # Given a processor and a value in the accumulator

        processor = fixture_processor
        processor.get_accumulator().set_value(123)
        processor.get_memory().set_value(0, 0)

        # When I use the processor to perform an STA instruction to an address memory

        address = 0
        processor.process_instruction(STA(address))

        # Then the memory location now has the value from the accumulator

        assert processor.get_memory().get_value(0) == 123

    def test_instruction_lda(self, fixture_processor):
        # Given a processor and a value in memory

        processor = fixture_processor
        processor.get_memory().set_value(0, 123)

        # When I use the processor to perform an LDA instruction from memory

        address = 0
        processor.process_instruction(LDA(address))

        # Then the accumulator now has the value from memory

        assert processor.get_accumulator().get_value() == 123

    def test_instruction_bra(self, fixture_processor):
        # Given a processor and a value in the program counter

        processor = fixture_processor
        processor.get_program_counter().set_value(1)

        # When I use the processor to perform an BRA instruction to an address

        address = 5
        processor.process_instruction(BRA(address))

        # Then the program counter now has the value from the BRA instruction

        assert processor.get_program_counter().get_value() == 5

    def test_instruction_brz(self, fixture_processor):
        # Given a processor, and zero value in the accumulator, and a value in the program counter

        processor = fixture_processor
        processor.get_accumulator().set_value(0)
        processor.get_program_counter().set_value(1)

        # When I use the processor to perform an BRZ instruction to an address

        address = 5
        processor.process_instruction(BRZ(address))

        # Then the program counter now has the value from the BRZ instruction

        assert processor.get_program_counter().get_value() == 5

    def test_instruction_brp(self, fixture_processor):
        # Given a processor, and positive value in the accumulator, and a value in the program counter

        processor = fixture_processor
        processor.get_accumulator().set_value(1)
        processor.get_program_counter().set_value(1)

        # When I use the processor to perform an BRZ instruction to an address

        address = 5
        processor.process_instruction(BRP(address))

        # Then the program counter now has the value from the BRP instruction

        assert processor.get_program_counter().get_value() == 5

    def test_instruction_inp_when_input_buffer_set_to_use_a_file(self, fixture_processor):
        # Given a processor, and a temporary file with a single number in it, and an input buffer that uses the file

        processor = fixture_processor

        temp_file = TempFile()
        temp_file.writeln('5')
        processor.get_input_buffer().set_file_to_read_from(temp_file.get_filename())

        # When I use the processor to perform an INP instruction to get a value from the input buffer

        processor.process_instruction(INP())

        # Then the accumulator will receive the value

        assert processor.get_accumulator().get_value() == 5

        temp_file.delete()

    def test_instruction_inp_when_input_buffer_set_to_have_stdin_redirected(self, fixture_processor):
        # Given a processor, and Python stdin is redirected to take input programmatically, and an
        # input buffer that uses the file

        processor = fixture_processor
        # Save stdin so we can restore it
        saved_stdin = sys.stdin
        # Fake user entering this value from keyboard
        sys.stdin = io.StringIO('5')

        # When I use the processor to perform an INP instruction to get a value from the input buffer

        processor.process_instruction(INP())

        # Then the accumulator will receive the value

        assert processor.get_accumulator().get_value() == 5
        sys.stdin = saved_stdin

    def test_instruction_out_when_output_buffer_automatically_collects_value_set(self, fixture_processor):
        # Given a processor, and an output buffer that automatically collects the value it has been set with

        processor = fixture_processor
        processor.get_accumulator().set_value(5)

        # When I use the processor to perform an OUT instruction to get a value from the input buffer

        processor.process_instruction(OUT())

        # Then the output buffer will get the value from the accumulator and will be able to return the value
        # for tests to check it

        assert processor.get_output_buffer().get_value_for_test() == 5

    def test_instruction_that_does_not_require_processing_such_as_dat(self, fixture_processor):
        # Given a processor

        processor = fixture_processor

        # When I use the processor to perform an instruction that does not reauire 'processing' such as DAT

        processor.process_instruction(DAT(1))

        # Then the processor will just ignore the instruction, and will not give an error
