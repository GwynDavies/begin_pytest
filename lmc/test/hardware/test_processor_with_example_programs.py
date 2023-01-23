
class TestProcessorWithExamplePrograms:
    def test_run_example_1(self, fixture_processor_with_example_program_1):
        # Given a processor with example program loaded into memory

        processor, temp_file, expected_output_value = fixture_processor_with_example_program_1

        # When I run the program on the processor

        processor.run_program()

        # Then I get the expected value in the output buffer

        assert processor.get_output_buffer().get_value_for_test() == expected_output_value
        temp_file.delete()

    def test_run_example_2(self, fixture_processor_with_example_program_2):
        # Given a processor with example program loaded into memory

        processor, temp_file, expected_output_value = fixture_processor_with_example_program_2

        # When I run the program on the processor

        processor.run_program()

        # Then I get the expected value in the output buffer

        assert processor.get_output_buffer().get_value_for_test() == expected_output_value
        temp_file.delete()

    def test_run_example_3(self, fixture_processor_with_example_program_3):
        # Given a processor with example program loaded into memory

        processor, temp_file, expected_output_value = fixture_processor_with_example_program_3

        # When I run the program on the processor

        processor.run_program()

        # Then I get the expected value in the output buffer

        assert processor.get_output_buffer().get_value_for_test() == expected_output_value
        temp_file.delete()

    def test_run_example_4(self, fixture_processor_with_example_program_4):
        # Given a processor with example program loaded into memory

        processor, temp_file, expected_output_value = fixture_processor_with_example_program_4

        # When I run the program on the processor

        processor.run_program()

        # Then I get the expected value in the output buffer

        assert processor.get_output_buffer().get_value_for_test() == expected_output_value
        temp_file.delete()
