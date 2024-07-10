# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if theguess is too high, too low
# or right on the money

import random # Importing the random module

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("\nTake a guess:"))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower. . .")
    else:
        print("Higher. . .")

    guess = int(input("Take a guess:"))
    tries += 1


print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\nPress the enter key to exit.")
