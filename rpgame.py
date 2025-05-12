import random

#game setup
health = 100
inventory = []


#introduction to the game
print("The outbreak has begun. The news fell silent hours ago.")
print("You smell smoke and the sounds of gunfire and screams echo through your apartment.")
print("It's time to go. You simply cannot stay here any longer.")
print()
print("You have to move from the safety of your home.")
print("There are only a few places you can go in town and the choice is up to you.")



print("\n\n")
print("A sudden pounding from your front door shakes you from your panic.")
print("You're entirely out of time. You stand from your couch and look around")
print("What do you do?")
print("     1) Answer your door")
print("     2) Look for supplies")
print("     3) Run to your backdoor")

choice = input("> ").strip()

if choice == 1:
    print("You cautiously begin to open the door.")
    print("A rotten claw-like hand reaches through the crack and scratches you!")
    print("You slam the door closed and lock it, but the scratch on your arm hurts.")
    global health
    health = 25
    print(health)



