from os.path import exists
# from os import remove, stat
import os
from lmc.io.file.source_pprogram.source_program_file import SourceProgramFile

FILE_NAME = 'test_source_program_file.lmcs'

TEST_FILE_LINES = [
    '        INP',
    '        STA FIRST',
    '        INP',
    '        STA SECOND',
    '        LDA FIRST',
    '        SUB SECOND',
    '        OUT',
    '        HLT',
    'FIRST   DAT',
    'SECOND  DAT']


class TestSourceProgram:
    def create_test_file(self):
        with open(FILE_NAME, 'w', encoding='ascii') as source_program_file:
            for test_file_line in TEST_FILE_LINES:
                source_program_file.write(test_file_line)
                source_program_file.write('\n')

    def clean_test_file_if_exists(self):
        if exists(FILE_NAME):
            os.remove(FILE_NAME)

    def test_read_file(self):
        # Create test file
        self.clean_test_file_if_exists()
        self.create_test_file()

        source_program_file = SourceProgramFile(FILE_NAME)
        assert source_program_file.exists() is True
        # Check size matches the system reported file size in bytes
        assert source_program_file.size_in_bytes() == os.stat(FILE_NAME).st_size

        source_program_file.read()

        assert len(source_program_file) == 10
        assert source_program_file[0].rstrip() == TEST_FILE_LINES[0]
        assert source_program_file[9].rstrip() == TEST_FILE_LINES[-1]
        assert source_program_file[-1].rstrip() == TEST_FILE_LINES[-1]

        # Clean up
        self.clean_test_file_if_exists()

    def test_str(self):
        # Create test file
        self.clean_test_file_if_exists()
        self.create_test_file()

        source_program_file = SourceProgramFile(FILE_NAME)
        source_program_file.read()
        expected_value = "        INP\n" + \
                         "        STA FIRST\n" + \
                         "        INP\n" + \
                         "        STA SECOND\n" + \
                         "        LDA FIRST\n" + \
                         "        SUB SECOND\n" + \
                         "        OUT\n" + \
                         "        HLT\n" + \
                         "FIRST   DAT\n" + \
                         "SECOND  DAT\n"

        assert str(source_program_file) == expected_value

        # Clean up
        self.clean_test_file_if_exists()
