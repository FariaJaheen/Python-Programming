# Guess My Number Game

import random

def guess_my_number():
    print("Welcome to 'Guess My Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    # Main game loop
    while True:
        # Get the player's guess
        guess = int(input("Take a guess: "))

        # Increment the number of attempts
        attempts += 1

        # Check the player's guess
        if guess < number:
            print("Higher...")
        elif guess > number:
            print("Lower...")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_my_number()


input("\n\nPress enter key to exit")
