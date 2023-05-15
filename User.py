"""
    Author: Stefano Veglia
"""


class User:
    """
    A class that represent a User.

    Attributes:
        name: string that store the user name.
        position: integer that represent the alphabetical position of the user in the guest list.
        friends: list containing the friends of the user.
        number_friends: integer representing the number of friends this user has.
        binary_friends: list that represent the number of friends in common between this user and others in the network.

    Methods:
         constructor: return the instance of user for each of the element in user list.
         count_friends: update the attribute number_friends in a user.
         sort_friends: organize the list of friends alphabetically.
    """
    def __init__(self):
        self._name = "null"
        self._position = "null"
        self._friends = []
        self._number_friends = 0
        self._binary_friends = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str):
            self._name = new_value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_value):
        if isinstance(new_value, int):
            self._position = new_value

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, new_value):
        if isinstance(new_value, list):
            self._friends = new_value

    @property
    def number_friends(self):
        return self._number_friends

    @number_friends.setter
    def number_friends(self, new_value):
        if isinstance(new_value, int):
            self._number_friends = new_value

    @property
    def binary_friends(self):
        return self._binary_friends

    @staticmethod
    def constructor(name, position):
        new_user = User()
        new_user.name = name
        new_user.position = position
        return new_user

    def count_friends(self, user):
        self.number_friends = len(user.friends)

    def sort_friends(self):
        self.friends.sort()
