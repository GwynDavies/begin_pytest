from lmc.application.error_fatal import ErrorFatal
import pytest


class TestComputer:
    def test_fatal_error(self):
        """Test I can cause the application to exit, giving a single error message"""

        # When I call a Fatal-Error with a single error message
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ErrorFatal.exit_fatal_error('error 1')

        # Then a System-Exit exception is raised with the expected error message
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == '\nFATAL ERROR ...\n\nerror 1\n\nExiting\n'

    def test_fatal_errors(self):
        """Test I can cause the application to exit, giving multiple error messages"""

        # When I call a Fatal-Error with multiple error messages
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ErrorFatal.exit_fatal_errors(['error 1', 'error 2'])

        # Then a System-Exit exception is raised with the expected error messages
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == '\nFATAL ERROR(S) ...\n\nerror 1\n\nerror 2\n\nExiting\n'

    def test_fatal_error_file_not_found(self):
        """Test I can cause the application to exit, when a file was not found"""

        # When I call a Fatal-Error with a single error message relating to a file not being found
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            file_name = 'testfilename'
            ErrorFatal.exit_file_not_found(file_name)

        # Then a System-Exit exception is raised with an expected error message, relating to the file not being found
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == '\nFATAL ERROR ...\n\nFile not found - testfilename\n\nExiting\n'

    def test_fatal_error_file_is_empty(self):
        """Test I can cause the application to exit, when a file was empty"""

        # When I call a Fatal-Error with a single error message relating to a file being empty
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            file_name = 'testfilename'
            ErrorFatal.exit_file_is_empty(file_name)

        # Then a System-Exit exception is raised with an expected error message, relating to the file being empty
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == '\nFATAL ERROR ...\n\nFile is empty - testfilename\n\nExiting\n'
