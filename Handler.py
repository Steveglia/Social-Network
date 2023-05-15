"""
    Author: Stefano Veglia
"""
from Controller import Controller


class Handler:
    """
    A Class that handle the txt file and check if the file is consistent.

    Attributes:
        file: Input where the value entered for the file name is initially stored.
        Controller: Create an instance of the class Controller'
        Controller.check(): Call the function check of Controller to check if the file exist in the directory.
        items: list that contain a string with the content of the file.txt

    Methods:
        read_file: store the content of the txt file in items.
        formatter: return the data in item in order to have a list of lists with the friendships.
        get_user: return a list of the users of the social network.
        check_consistency1: return false if the file is empty.
        check_consistency2: return false if the friendship stated in the file.txt are not matching.
        check_consistency3: return false if the number of user doesn't match with the number stated in the file.txt.
        checks: return false if one of the check_consistency function is False.
    """
    def __init__(self):
        self._file = input("Enter file name or press 'n' to close the program:\n")
        self._Controller = Controller(self.file)
        self._Controller.check()
        self._items = self.read_file()

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, new_value):
        if isinstance(new_value, str):
            self._file = new_value
        else:
            print("Handler.file setter received the wrong type of data")

    @property
    def Controller(self):
        return self._Controller

    @property
    def items(self):
        return self._items

    def read_file(self):
        if self.Controller.check():
            self.file = self.Controller.file_name
            with open(self.file, 'r') as f:
                return f.readlines()

    def formatter(self):
        my_list = [line.strip() for line in self.items]
        new_list = [[x] for x in my_list]
        final_list = [y[0].split() for y in new_list]
        return final_list[1:]

    def get_users(self):
        split_list = []
        for elem in self.items:
            split_list.append(elem.split())
        flat_list = [item for elem in split_list for item in elem]
        users_list = [*set(flat_list)]
        users_list.sort()
        return users_list[1:]

    def check_consistency3(self):
        if len(self.get_users()) == int(self.items[0]):
            return True
        else:
            print(f"{self.Controller.file_name} file is inconsistent. The number of user state is not correct.")
            return False

    def check_consistency2(self):
        x = self.formatter()
        for value in x:
            if value[::-1] not in x:
                print(f"{self.Controller.file_name} file is inconsistent. The relation between users is not correct.")
                return False
        return True

    def check_consistency1(self):
        if not self.items:
            print(f"{self.Controller.file_name} file is inconsistent. The file is empty.")
            return False
        return True

    def checks(self):
        return self.check_consistency1() and self.check_consistency2() and self.check_consistency3()



