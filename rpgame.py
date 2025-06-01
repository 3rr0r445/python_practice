import random
import time

def main():
    game_intro()
    living_room()



def game_intro():
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
    print("You smell smoke and something else you can't quite place, something sweet and sickly.")
    time.sleep(1)
    print("Gunfire, screams—once constant. Now gone. The world outside is eerily still.")
    time.sleep(1)
    print("What you can vaguely hear from outside is the sound of shambling footsteps and moaning.")
    time.sleep(1)
    print("Escape is probably a pipedream at this point. Maybe something in this house can help you survive.")
    time.sleep(1)
    print()




def living_room():
    living_room_intro()
    living_room_choice()

def living_room_intro():
    print("The living room isn't much to look at, but it's your home.")
    time.sleep(1)
    print("A city map lies on the table, but you know it's not safe to go outside anymore.")
    time.sleep(1)
    print("As you sit on the couch plotting your next move..")
    time.sleep(1)
    print("A series of loud BANG rattles the front door on it's hinges.")
    time.sleep(1)
    print("You instinctively hold your breath, your heart pounding in your chest.")
    time.sleep(2)
    print("BANG! BANG! BANG!")
    time.sleep(1)
    print("Your next decision is critical. Your choices are few.")
    time.sleep(1)
    print()
    print()
    

def living_room_choice():
    print("What should you do? ")
    print("1) Open the door (Why would you do this?")
    print("2) Lock the door and try to remain as hidden as possible.")
    print("3) Leave the living room and try to find a something useful.")
    print("4) Search the Living Room for supplies.")
    print()
    living_room_choice = input("Enter your choice: ")

    if living_room_choice == "1":
        print("You confidently walk to the door and throw it open.")

    

if __name__ == '__main__':
    main()