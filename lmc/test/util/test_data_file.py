from os.path import exists
from os import remove


class TestDataFile:
    @staticmethod
    def clean_test_file_if_exists(filename):
        if exists(filename):
            TestDataFile.clean_test_file(filename)

    @staticmethod
    def clean_test_file(filename):
        remove(filename)
