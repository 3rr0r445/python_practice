import random
import time

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable
flashlight = Item("Flashlight", "A new flashlight", True)
table = Item("Coffee Table", "A worn coffee table", False)


living_room = Room("The Living Room", "Your living room. It's exactly as it should be, except the electricity has been cut off.")
living_room.items.append(flashlight)
living_room.items.append(table)

player = Player("The Player", living_room,)


def intro():
    print("Welcome to Travis' Zombie Survival Game!")
    print("Created by: Travis Duran")
    print("Special Thanks to: CodeinPlace and Stanford.")
    print("Also a huge thanks to my fellow students in my section!")
    print()
    input("Press Enter to Begin...")
    print()
    print()
    print("--------------------------------")
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

# Start of the game
intro()
print("")
print(player.location.name)
print(player.location.description)
print("Exits: ")
for exit in player.location.exits:
    print(exit)
print("You see the following: ")
for item in player.location.items:
    print(item.name)


#Set up the get command
while true:
    command = input("> ").strip()
    words = command.split()

    if len(words) == 0:
        continue

    verb = words[0]
    noun = words[1] if len(words) > 1 else None


#Set up examine command
if verb == "examine":
    for item in player.location.items:
        if item.name == noun:
            print(item.description)

#Set up get command
if verb == "get":
    for item in player.location.items:
        if item.name == noun:
            print("You take the {}".format(item.name))
            #Remove item from room
            player.location.items.remove(item)
            #Add to player inventory
            player.inventory.append(item)