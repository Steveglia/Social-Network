"""
    Author: Stefano Veglia
    Student ID: 001270412
"""

from Handler import Handler
from User import User


class SocialNetwork(User):
    """
    A class that represent a Social Network.

    Attributes:
        handler: create an instance of Handler to start the formatting of the file.txt and the series of checks.
        final_list: stores the list returned by formatter of the friendships organize as a list of lists.
        user_list: stores the list returned by get_user of all the user in the social network.
        object_list: list containing the instances of the class User.

    Methods:
        insert_user: append the instances of User created from the user_list.
        add_friends: append the friends to the list friends in the object User.
        show_social_network: print a sting with every single user and his friends.
        get_binary_friends: append a list containing the number of friends in common between this user and other.
        check_get_object: return an user's object if check_get_object is true. Otherwise asked again for an input.
        check_get_object2: return true if the inputted name exist in the user_list.
        return_target(name): return the object relative to that name.
        return_target_position(name): return the position relative to that name.
        return_target_name(position): return the name relative to that position.
        friend_suggestion: print the friend suggestion for a specific user or print another message if the result is 0.
        return_number_friends: print the number of friends of a specific user.
        return_antisocial: return a list of the user with no friends.
        return_pretty_antisocial: print a message with the user/users with the least number of friends.
       #return_friend_user: return a
        erase_friends_user: return a formatted version of binary friends where the user and his friends have been set to
         0.
        return_indirect_friends(user): return a list indirect friends of a specific user.
        show_indirect_friends: print the indirect friends of a specific user or a custom message if he doesn't have any.
    """
    search_condition = False
    target_list = []

    def __init__(self):
        super().__init__()
        self._handler = Handler()
        self._final_list = self.handler.formatter()
        self._users_list = self.handler.get_users()
        self._object_list = []

    @property
    def handler(self):
        return self._handler

    @property
    def final_list(self):
        return self._final_list

    @property
    def users_list(self):
        return self._users_list

    @property
    def object_list(self):
        return self._object_list

    def insert_users(self):
        i = 0
        for names in self.users_list:
            self.object_list.append(self.constructor(names, i))
            i += 1

    def add_friends(self):
        for user in self.object_list:
            for x in self.final_list:
                if len(x) == 2:
                    if user.name == x[0]:
                        user.friends.append(x[1])
            user.sort_friends()
            user.count_friends(user)

    def show_social_network(self):
        for user in self.object_list:
            print(f"{user.name.ljust(10)}-> {', '.join(user.friends)} ")

    def get_binary_friends(self):
        for user in self.object_list:
            for target in self.object_list:
                result = set(user.friends) & set(target.friends)
                user.binary_friends.append(len(result))

    def check_get_object(self):
        while SocialNetwork.search_condition is False:
            target = input(f"Enter a user between the following list {self.users_list}:\n")
            SocialNetwork.target_list.append(target)
            self.check_get_object2(SocialNetwork.target_list[-1])
        else:
            SocialNetwork.search_condition = False
            for user in self.object_list:
                if SocialNetwork.target_list[-1] == user.name:
                    return user

    def check_get_object2(self, target):
        if target in self.users_list:
            SocialNetwork.search_condition = True
        else:
            print("The name you've insert in not in the list above. Try again.")

    def return_target(self, name):
        for user in self.object_list:
            if name == user.name:
                return user

    def return_target_position(self, name):
        for user in self.object_list:
            if name == user.name:
                return user.position

    def return_target_name(self, position):
        for user in self.object_list:
            if position == user.position:
                return user.name

    def friend_suggestion(self):
        user = self.check_get_object()
        binary_friends = self.erase_friends_user(user)
        final_targets = []
        if max(binary_friends) > 0:
            i = 0
            for y in binary_friends:
                if y == max(binary_friends):
                    final_targets.append(self.return_target_name(i))
                i += 1
            print(f" The friends suggestions are: {', '.join(final_targets)}.")
        else:
            print(f" There's no friends suggestions for this user.")

    def return_number_friends(self):
        user = self.check_get_object()
        sin_plu = "friends"
        if user.number_friends == 1:
            sin_plu = "friend"
        print(f"{user.name} has {user.number_friends} {sin_plu}: {', '.join(user.friends)} ")

    def return_antisocial(self):
        antisocial = []
        for user in self.object_list:
            if user.number_friends == 0:
                antisocial.append(user.name)
        return antisocial

    def return_pretty_antisocial(self):
        antisocial = self.return_antisocial()
        local_user_list = self.users_list
        for x in antisocial:
            if x in local_user_list:
                local_user_list.remove(x)
        if not local_user_list:
            print("There is no friends in this network")
        else:
            obj_list = []
            for x in local_user_list:
                obj_list.append(self.return_target(x))
            almost_as = [obj_list[0]]
            for user in obj_list[1:]:
                if user.number_friends < almost_as[0].number_friends:
                    almost_as = [user]
                elif user.number_friends == almost_as[0].number_friends:
                    almost_as.append(user)
            almost_as_names = []
            for user in almost_as:
                almost_as_names.append(user.name)
            print(f" In this network {', '.join(almost_as_names)} have the least number of friends,"
                  f" {almost_as[0].number_friends}.")

    def return_friend_user(self):
        user = self.check_get_object()
        print(user.friends)

    def erase_friends_user(self, user):
        target_positions = []
        copy_b_f = user.binary_friends
        for friends in user.friends:
            target_positions.append(self.return_target_position(friends))
        target_positions.append(user.position)
        for x in target_positions:
            copy_b_f[x] = 0
        return copy_b_f

    def return_indirect_friends(self, user):
        binary_friends = self.erase_friends_user(user)
        final_targets = []
        if max(binary_friends) > 0:
            i = 0
            for y in binary_friends:
                if y != 0:
                    final_targets.append(self.return_target_name(i))
                i += 1
        return final_targets

    def show_indirect_friends(self):
        user = self.check_get_object()
        if not self.return_indirect_friends(user):
            print("The user's friends don't have any friend who is not already friend with the user.")
        else:
            friends = []
            for friend in user.friends:
                friends.append(self.return_target(friend))
            for friend in friends:
                friend.friends.remove(user.name)
                print(f"{friend.name.ljust(10)} -> {', '.join(friend.friends)}")
                friend.friends.append(user.name)
            print(f"The indirect friends for {user.name} are: {', '.join(self.return_indirect_friends(user))}.")

