from os.path import exists
from os import stat


class ProgramFile:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def exists(self):
        return exists(self.file_name)

    def is_empty(self):
        return stat(self.file_name).st_size == 0

    def size_in_bytes(self):
        return stat(self.file_name).st_size
