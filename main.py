"""
    Author: Stefano Veglia
    Student ID: 001270412
"""

from SocialNetwork import SocialNetwork


def next_command(command):
    """
    This method takes an input to continue after a command has been executed. In this case works for command that can be
    reiterated. If the input is X it will go back to the menu, if the input is C will close the program and if it's R it
    will repeat the last command.
    :param command: The previous command
    :return: Boolean
    """
    while True:
        choice1 = input("\n Press 'X' to go back to the menu, 'R' to repeat this function or C to close the program.\n")
        if choice1 == "X":
            menu()
            break
        elif choice1 == "C":
            quit()
            break
        elif choice1 == "R":
            execute(command)
            break
        else:
            print(" Wrong input. Try again.\n")


def next_command_not_iterable():
    """
    This method takes an input to continue after a command has been executed. In this case works for command that cannot
     be reiterated. If the input is X it will go back to the menu and if the input is C will close the program.
    :return: Boolean
    """
    while True:
        choice1 = input("\n Press X to go back to the menu or C to close the program.\n")

        if choice1 == "X":
            menu()
            break
        elif choice1 == "C":
            quit()
            break
        else:
            print(" Wrong input. Try again.\n")


def execute(command):
    """
    This method analyze the requested command to be run. If the command is not between 1-6 it will ask to insert it
     again.
    :param command:
    :return: relative function and customize methods for the next step.
    """
    while True:
        if int(command) == 1:
            case.show_social_network()
            next_command_not_iterable()

        if int(command) == 2:
            print("You choose: Recommend a friend to another member.")
            case.friend_suggestion()
            next_command(command)

        if int(command) == 3:
            print("You choose: Display how many friends a member has.")
            case.return_number_friends()
            next_command(command)

        if int(command) == 4:
            print("You choose: Display the members with the least number of or have no friends.")
            if case.return_antisocial():
                print(f" In this network {', '.join(case.return_antisocial())} have no friends.")
            else:
                print("Everyone has at least a friend in this network.")
            case.return_pretty_antisocial()
            next_command_not_iterable()

        if int(command) == 5:
            print("You choose: Display the friends of friends of a given member.")
            case.show_indirect_friends()
            next_command(command)

        if int(command) == 6:
            print("You choose: Open a new network.")
            choice = input("Enter 'Y' to open a new network or 'C' to close the program.")
            if choice == "Y":
                break
            elif choice == "C":
                print("Thank you for using Arctic Network.")
                quit()
            else:
                print(" Wrong input. Try again.\n")


def menu():
    """
    This method show the different option the user has to interact with the SN. also takes an iput for the command and
    call the function execute()
    :return: print a message and store an input
    """
    print("-------->  Choose between the following options   <--------\n")
    print(" Press 1 - Display Arctic Network.")
    print(" Press 2 - Recommend a friend to another member.")
    print(" Press 3 - Display how many friends a member has.")
    print(" Press 4 - Display the members with the least number of or have 0 friends.")
    print(" Press 5 - Display the friends of friends of a given member.")
    print(" Press 6 - Open a new network\n")
    choice = input("Enter command:\n")
    if choice in ["1", "2", "3", "4", "5", "6"]:
        execute(choice)
    else:
        print(" Wrong input. Try again.\n")
        menu()


while True:
    print("-------->  Welcome to Arctic Network   <--------\n")
    case = SocialNetwork()  # load the file and store the data in the social network.
    if not case.handler.checks():  # check if the file is consistent.
        case.insert_users()
        case.add_friends()
        case.show_social_network()  # show the structure even if the file is not consistent.
        continue
    case.insert_users()  # create the object out of user.
    case.add_friends()  # add the friends to the instances.
    case.get_binary_friends()   # add the common friend count to the instances.
    menu()  # run the function menu.
