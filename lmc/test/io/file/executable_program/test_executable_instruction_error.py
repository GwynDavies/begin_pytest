from lmc.io.file.executable_program.executable_instruction import ExecutableInstructionError


class TestExecutableInstructionError:

    def test_executable_instruction_error_that_has_no_index_set(self):
        # GIven an executable instruction error

        message = 'Test message'
        executable_instruction_error = ExecutableInstructionError(message)

        # When I get its message or call its __str__ method

        # Then I get the message I set on it

        assert executable_instruction_error.get_message() == message
        assert str(executable_instruction_error) == message

    def test_executable_instruction_error_that_has_an_index_set(self):
        # GIven an executable instruction error that also has an index set
        index = 101
        message = 'Test message'
        executable_instruction_error = ExecutableInstructionError(message)
        executable_instruction_error.set_index(index)

        # When I get its message

        # Then I can get the index I set on it, and I get the index value with
        # the message when I call its __str__method

        assert executable_instruction_error.get_index() == str(index)
        assert str(executable_instruction_error) == 'Index ' + \
            str(index) + ' - ' + message
