class Color:
    """ Adds basic colors for print statements """
    RED = '\033[91m'
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    END = '\033[0m'


def showInstructions():
    """ print a main menu and the commands """
    print(Color.PURPLE + "Welcome to Pepper RPG v 1.0!" + Color.END)
    print("========")
    print("In this game you are Pepper, a small Russian Blue cat"
          + " who is craving a jelly filled donut. \nYour mission "
          + "if you choose to accept it is to acquire "
          + "a donut by any means necessary.")
    print("========")
    showHelp()


def showDescription(currentRoom):
    """ prints the description of the current room """
    print(Color.PURPLE + rooms[currentRoom]["description"] + Color.END)


def showHelp():
    """ prints list of commands """
    print("Commands:")
    print("'help'")
    print("'go [direction]'")
    print("'look'")
    print("'quit'")


def showStatus(currentRoom):
    """ print the player's current status """
    print("----------------------------")
    print("You are in the {}".format(rooms[currentRoom]["name"]))
    print("-----------------------------")


# Dictionary that links rooms to other room positions
rooms = {
    1: {
        "description": "The bedroom of the house has two windows with"
        + " blue curtains and a walk-in closet. There is an exit south.",
        "name": "Bedroom",
        "south": 2,
    },
    2: {
        "description": "The living room has a vintage red couch and hardwood "
        + "floor. There are exits north, south, and west.",
        "name": "Living room",
        "north": 1,
        "south": 3,
    },
    3: {
        "description": "The bonus room has two desks, a cat tree, and several "
        + " musical instruments. There is an exit north.",
        "name": "Bonus room",
        "north": 2,
    },
}

showInstructions()


def main():

    # Game Variables
    currentRoom = 1
    gameStatus = "ongoing"

    # Game loop
    while gameStatus == "ongoing":

        showStatus(currentRoom)

        # Get player's next 'move'
        move = input(">").lower().split()

        # Handle go command
        if move[0] == "go":
            # Check if movement is allowed
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("You can't go that way!")
        elif str(move[0]) in ["north", "south", "east", "west"]:
            # Check if movement is allowed
            if move[0] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[0]]
            else:
                print("You can't go that way!")
        elif move[0] == "help":
            showHelp()
        elif move[0] == "look":
            showDescription(currentRoom)
        elif move[0] == "quit" or move[0] == "exit":
            print(Color.RED + "Doh, you didn't win this time. Thanks" +
                  "for playing Pepper RPG, have a nice day!" + Color.END)
            exit(0)
        else:
            print("Not a valid command")


if __name__ == "__main__":
    main()
