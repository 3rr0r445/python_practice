import random


def number_quiz():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome To The Number Guessing Game By Travis Duran")
    user_name = input("What's your name?")
    print(f"Okay {user_name}, I'm thinking of a number between 1 and 100.")
    print("Your job will be to guess, and I'll let you know if you're off.")
    print("You have ten tries. I'll keep track for you.")
    print()

    for i in range(attempts):
        print(f"You have {attempts} tries remaining.")
        guess = int(input("What is your guess? "))


        if guess < secret_number:
            print("Sorry, your number is too low. Guess Again.")
        elif guess > secret_number:
            print("Sorry, your number is too high. Guess Again.")
        else:
            print(f"Congrats! The number was {secret_number} and you guessed it in {i + 1} tries.")
            break

    else:
        print("Sorry, you ran out of attempts.")

if __name__ == "__main__":
    number_quiz()
    