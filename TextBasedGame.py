from time import sleep

rooms = {
    "Main Lair": {
        "South": "Dungeon",
        "North": "Cellar",
        "East": "Throne Room",
        "West": "Great Hall",
    },
    "Throne Room": {"North": "Gates of Hell", "West": "Main Lair"},
    "Dungeon": {"East": "Chamber", "North": "Main Lair"},
    "Great Hall": {"East": "Main Lair"},
    "Chamber": {"West": "Dungeon"},
    "Cellar": {"East": "Court Yard", "South": "Main Lair"},
    "Court Yard": {"West": "Cellar"},
}

items = {
    "Cellar": "Shield",
    "Main Lair": "Sword",
    "Dungeon": "Helmet",
    "Chamber": "Body Armor",
    "Throne Room": "Gauntlet",
    "Court Yard": "Lance",
}

inventory = []
current_room = "Great Hall"
list_of_directions = ["North", "East", "West", "South"]

def introduction():
    sleep(3)
    print("\nHello {}, Welcome to the Devil's Labyrinth of Doom!\n".format(user_name))
    sleep(3)
    line_print("You are stuck down here for eternity.\nUnless you can manage to obtain all the "
               "necessary equipment you need to defeat the Gate Keeper.\nOnly then can you "
               "escape this God forsaken place.\n")
    

def show_instructions():
    print(
        "\nCommands and Instructions:\n"
        "   Move commands: go north, go east, go south, go west\n"
        "   To get item: get 'name of item'\n"
        "   Remember, you can't face the Gate Keeper before collecting all 6 items!\n"
    )


def player_status():
    slow_print("\nYou are currently in the {}\n".format(current_room))
    sleep(2)
    if len(inventory) > 0:
        slow_print("Your current items are: {}\n".format(", ".join(inventory)))
    else:
        slow_print("You have no items\n")
        
    if current_room in items.keys():
        # Key has been popped if not found.
        slow_print(f"You see a {items[current_room]}.")
    else:
        slow_print("There are no items to collect in this room.\n")
        # Item would be in Inventory.


def get_item():
    item_name = " ".join(move[1:])
    if current_room in items.keys():
        if item_name == items[current_room]:
            retrieved_item = items.pop(current_room)
            inventory.append(retrieved_item)
            slow_print("\nYou got the {}!".format(retrieved_item))
        elif item_name in items.values():
            slow_print("\nThis item is in another room.")
        else:
            print("\nInvalid input.")
    elif item_name in inventory:
        slow_print("\nYou already have the {}.".format(item_name))
    elif item_name in items.values():
        slow_print("\nThis item is in another room.")
    else:
        print("There are no items in this room.")


def move_between_rooms():
    global current_room
    try:
        if move[1] in list_of_directions:
            if move[1] in rooms[current_room].keys():
                current_room = rooms[current_room][move[1]]
            else:
                print("\nSorry, you can't go that way.")
        else:
            print("Invalid Input")
    except IndexError:
        print("\nInvalid Input")


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        if char == "\n":
            sleep(1)
        else:
            sleep(0.05)

def line_print(text):
    for line in text:
        print(line, end="", flush=True)
        if line == "\n":
            sleep(2)
        else:
            sleep(0.02)



# Game Start

sleep(2)
slow_print("Welcome to this text based adventure.\n")
sleep(2)
slow_print("What is your name?")
user_name = input().title()

introduction()

slow_print("\nWould you like to proceed?  Y / N\n")
proceed = input().lower().strip()
if proceed == "y":
    pass
    proceed = ""
elif proceed == "n":
    quit()


sleep(2)
show_instructions()
sleep(4)

slow_print("\nPress 'Y' to start game.\n")
proceed = input().lower().strip()
while proceed != "y":
    proceed = input("Invalid Input")



while current_room != "Gates of Hell":
    # Continue loop until player enters Gates of Hell.

    player_status()

    slow_print("\nWhat would you like to do:")
    move = input().title().split()
    print("<--------------------------------->")

    if "Go" in move:
        move_between_rooms()
    elif "Get" in move:
        get_item()
    else:
        print("\nInvalid Input")

    # End while loop.

if len(inventory) < 6:  # Decide if player has all 6 items when room is entered.
    lose_game_prompt = "\nWomp! Womp!\n YOU LOSE!"
    slow_print(lose_game_prompt)
else:
    win_game_prompt = "\nCONGRATULATIONS!\n You made it through Gates of Hell!"
    slow_print(win_game_prompt)
