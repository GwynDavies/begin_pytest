from os.path import exists
from os import remove


class EmptyTestFile():
    def __init__(self, filename):
        self.filename = filename

    def create(self):
        # pylint: disable-next=consider-using-with
        open(self.filename, 'w', encoding='ascii').close()

    def remove_if_exist(self):
        if exists(self.filename):
            remove(self.filename)
