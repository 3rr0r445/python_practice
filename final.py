import random
import time

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item:
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# Define items
flashlight = Item("Flashlight", "A new flashlight", True)
table = Item("Coffee Table", "A worn coffee table", False)

# Define room and assign items
living_room = Room("The Living Room", "Your living room. It's exactly as it should be, except the electricity has been cut off.")
living_room.items.append(flashlight)
living_room.items.append(table)

# Create the player
player = Player("The Player", living_room)

# Game introduction
def intro():
    print("Welcome to Travis' Zombie Survival Game!")
    print("Created by: Travis Duran")
    print("Special Thanks to: CodeinPlace and Stanford.")
    print("Also a huge thanks to my fellow students in my section!")
    print()
    input("Press Enter to Begin...")
    print("\n--------------------------------")
    time.sleep(1)
    print("The outbreak has begun. The news fell silent hours ago.")
    time.sleep(1)
    print("You called for help before the phones went down and have been waiting since.")
    time.sleep(1)
    print("You smell smoke and something else you can't quite place, something sweet and sickly.")
    time.sleep(1)
    print("Gunfire, screams—once constant. Now gone. The world outside is eerily still.")
    time.sleep(1)
    print("What you can vaguely hear from outside is the sound of shambling footsteps and moaning.")
    time.sleep(1)
    print("Escape is probably a pipedream at this point. You must collect resources in this house and get to the basement to await rescue.")
    time.sleep(1)
    print()


#Function to display the users location and relevant items
def show_location():
    print(f"\n{player.location.name}")
    print(player.location.description)
    print("\nExits:")
    for exit in player.location.exits:
        print(exit)
    
    print("\nYou see the following:")
    for item in player.location.items:
        print(item.name)


# Start the game
intro()
print(f"\n{player.location.name}")
print(player.location.description)
print("\nExits:")
for exit in player.location.exits:
    print(exit)

print("\nYou see the following:")
for item in player.location.items:
    print(item.name)

# Game loop to process commands continuously
while True:  # Fixed 'true' to 'True'
    command = input("> ").strip()
    words = command.split()

    if len(words) == 0:
        continue  # Ignore empty input

    verb = words[0]
    noun = words[1] if len(words) > 1 else None

    # Examine command
    if verb.lower() == "examine" and noun:
        found_item = next((item for item in player.location.items if item.name.lower() == noun.lower()), None)
        if found_item:
            print(found_item.description)
        else:
            print(f"There is no {noun} here.")

    # Get command
    elif verb.lower() == "get" and noun:
        found_item = next((item for item in player.location.items if item.name.lower() == noun.lower()), None)
        if found_item and found_item.is_movable:
            player.inventory.append(found_item)
            player.location.items.remove(found_item)
            print(f"You take the {noun}.")
        elif found_item and not found_item.is_movable:
            print(f"The {noun} is too heavy to take.")
        else:
            print(f"There is no {noun} here.")

    elif verb.lower() == "quit":
        print("Thanks for playing! Stay safe out there.")
        break

    else:
        print("I don't understand that command.")
    
    #Show details after the command is processed
    show_location()