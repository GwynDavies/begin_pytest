import os
from os.path import exists
from os import remove
import tempfile


class TempFile:
    def __init__(self):
        self.filename = os.path.join(
            tempfile.gettempdir(), next(tempfile._get_candidate_names()))

    def get_filename(self) -> str:
        return self.filename

    def delete(self):
        if exists(self.filename):
            remove(self.filename)

    def writeln(self, value: str):
        with open(self.filename, 'w', encoding='ascii') as file:
            file.write(value+"\n")

    def appendln(self, value: str):
        with open(self.filename, 'a', encoding='ascii') as file:
            file.write(value+"\n")

    def read(self) -> str:
        with open(self.filename, 'r', encoding='ascii') as file:
            value = file.read()
        return value.strip()
