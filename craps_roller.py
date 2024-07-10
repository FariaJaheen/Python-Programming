# Craps Roller
# Demonstrates random number generation

import random

# Generate random numbers 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and", die2, "for a total of", total)

input("\n\nPress enter key to exit.")
