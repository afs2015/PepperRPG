class color:
    ''' Adds basic colors for print statements '''
    RED = '\033[91m'
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def showInstructions():
    # print a main menu and the commands
    print(color.PURPLE + "Welcome to Pepper RPG v 1.0!" + color.END)
    print("========")
    print( "In this game you are Pepper, a small Russian Blue cat"
          + " who is craving a jelly filled donut. \nYour mission if you choose"
          + " to accept it is to acquire a donut by any means necessary.")
    print("========")
    showHelp()

def showDescription(currentRoom):
    # print the description of the current room
    print(color.PURPLE + rooms[currentRoom]["description"] + color.END)

def showHelp():
    # prints list of commands
    print("Commands:")
    print("'help'")
    print("'go [direction]'")
    print("'look'")
    print("'quit'")

def showStatus(currentRoom):
    # print the player's current status
    print("----------------------------")
    print("You are in the {}".format(rooms[currentRoom]["name"]))
    print("-----------------------------")

# dictionary that links rooms to other room positions
rooms = { 1 : { "description": "The bedroom of the house has two windows with" +
                                " blue curtains and a walk-in closet. There is an exit south.",
                "name"  : "Bedroom",
                "south" : 2, },
          2 : { "description": "The living room has a vintage red couch and hardwood floor. There" +
                                " are exits north, south, and west.",
                "name"  : "Living room",
                "north" : 1, }
        }

showInstructions()

def main():

    # Game Variables
    currentRoom = 1
    gameStatus = "ongoing"

    # game loop
    while gameStatus == "ongoing":

        showStatus(currentRoom)

        # get player's next 'move'
        move = input(">").lower().split()

        # handle go command
        if move[0] == "go":
            # check if movement is allowed
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("You can't go that way!")
        elif str(move[0]) in  ["north", "south", "east", "west"]:
            # check if movement is allowed
            if move[0] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[0]]
            else:
                print("You can't go that way!")
        elif move[0] == "help":
            showHelp()
        elif move[0] =="look":
            showDescription(currentRoom)
        elif move[0] == "quit" or move[0] == "exit":
            print(color.RED + "Doh, you didn't win this time. Thanks for playing Pepper RPG, have a nice day!" + color.END)
            exit(0)
        else:
            print("Not a valid command")

if __name__== "__main__":
    main()
