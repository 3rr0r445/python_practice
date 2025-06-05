import random
import time

class Room(object):
    def __init__(self, name, description, exits, items):
        self.name = name
        self.description = description
        self.exits = {}
        self items = []

class Player(object):
        def __init__(self, name, location,):
        self.name = name
        self.location = location
        self inventory = []

living_room = Room("The Living Room", "Your living room. It's exactly as it should be, except the electricity has been cut off.", {"S" : hallway}, [flashlight])

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
    print("Escape is probably a pipedream at this point. You must collect resources in this house and get")
    time.sleep(1)
    print()





if __name__ == '__main__':
    main()