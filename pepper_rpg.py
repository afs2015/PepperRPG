class color:
    ''' Adds basic colors for print statements '''
    RED = '\033[91m'
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def showInstructions():
    # print a main menu and the commands
    print(color.PURPLE + "Pepper RPG v 1.0" + color.END)
    print("========")
    print("Commands:")
    print("'go [direction]'")
    print("'quit'")

def showStatus(currentRoom):
    # print the player's current status
    print("----------------------------")
    print("You are in {}".format(rooms[currentRoom]["name"]))
    print("-----------------------------")

# dictionary that links rooms to other room positions
rooms = { 1 : { "name"  : "Bedroom",
                "south" : 2 },
          2 : { "name"  : "Living room",
                "north" : 1}
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
        elif move[0] == "quit":
            print(color.RED + "Doh, you didn't win this time. Thanks for playing Pepper RPG, have a nice day!" + color.END)
            exit(0)
        else:
            print("Not a valid command")

if __name__== "__main__":
    main()
