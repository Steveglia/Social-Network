from os.path import exists


class Controller:
    """
    A class that check if the file is the directory.

    Attributes:
        file_name: Stores the file name in a string.

    Methods:
        check: return true if the file name insert exist in the directory. Restart the process if the search is null.
    """
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, new_value):
        if isinstance(new_value, str):
            self._file_name = new_value

    def check(self):
        if self.file_name == "n":
            print("Thank you for using Arctic Network.")
            exit()
        elif exists(self.file_name):
            return True
        else:
            print("This file doesn't exist")
            self.file_name = input("Enter file name or press n to close the program:\n")
            self.check()

