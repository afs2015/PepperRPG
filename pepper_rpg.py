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
    print(Color.PURPLE + rooms[currentRoom]["description"] + '\n' + Color.END)


def showHelp():
    """ prints list of commands """
    print("Commands:")
    print("'help'")
    print("'go [direction]'")
    print("'(l)ook'")
    print("'quit'")


def showStatus(currentRoom):
    """ print the player's current status """
    print("----------------------------")
    print("You are in the {}".format(rooms[currentRoom]["name"]))
    print("-----------------------------")


def movePlayer(direction, currentRoom):
    """ checks if a direction is allowed, if so move player """
    if direction in rooms[currentRoom]:
        room = rooms[currentRoom][direction]
    else:
        room = currentRoom
        print("You can't go that way! \n")
    return room


def parseMove(move, current_room, directions):
    """ takes in a player move and does appropriate actions """

    move_results = {
        'has_player_moved': False,
        'current_room': current_room,
        'used_look': False,
    }

    # Handle go command
    if move[0] == "go":
        move_results['current_room'] = movePlayer(move[1], current_room)
        move_results['has_player_moved'] = True
    elif str(move[0]) in directions:
        move_results['current_room'] = movePlayer(move[0], current_room)
        move_results['has_player_moved'] = True
    elif move[0] == "help":
        showHelp()
    elif move[0] == "look" or move[0] == "l":
        showDescription(current_room)
        move_results['used_look'] = True
    elif move[0] == "quit" or move[0] == "exit":
        print(Color.RED + "Doh, you didn't win this time. Thanks "
        + "for playing Pepper RPG, have a nice day!" + Color.END)
        exit(0)
    else:
        print("Not a valid command")

    return move_results


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
        + "floor. There are exits north, north-west, south, and west.",
        "name": "Living room",
        "north": 1,
        "north-west": 5,
        "south": 3,
        "west": 4,
    },
    3: {
        "description": "The bonus room has two desks, a cat tree, and several"
        + " musical instruments. There is an exit north.",
        "name": "Bonus room",
        "north": 2,
    },
    4: {
        "description": "The bathroom has a sink, toliet, and a white bathtub"
        + " with a teal shower curtain. There is an exit east.",
        "name": "Bathroom",
        "east": 2,
    },
    5: {
        "description": "The kitchen has a black and white checkered floor with a"
        + "wooden table and two chairs. There is an exit south.",
        "name": "Kitchen",
        "south": 2,
    }
}

showInstructions()


def main():

    # Game Variables
    current_room = 1
    game_status = "ongoing"
    used_look = False
    directions = ["north", "north-east", "north-west", "south", "east", "west"]

    # Game loop
    while game_status == "ongoing":

        if not used_look:
            showStatus(current_room)

        used_look = False

        # Get player's next 'move'
        move = input(">").lower().split()

        # Handle player's move
        player_move = parseMove(move, current_room, directions)
        
        # On player move command update current room
        # import pdb; pdb.set_trace()
        if player_move['has_player_moved']:
            current_room = player_move['current_room']

        if player_move['used_look']:
            used_look = True


if __name__ == "__main__":
    main()
