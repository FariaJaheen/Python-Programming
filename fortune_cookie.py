# Demonstrates Fortune Cookie Program
import random

# Generate a random number between 1 and 5
fortune_number = random.randint(1, 5)

# Print a fortune based on the generated number
if fortune_number == 1:
    print("Fortune: You will have a great day today!")
elif fortune_number == 2:
    print("Fortune: Something unexpected will bring you joy.")
elif fortune_number == 3:
    print("Fortune: A thrilling time is in your immediate future.")
elif fortune_number == 4:
    print("Fortune: A fresh start will put you on your way.")
elif fortune_number == 5:
    print("Fortune: Adventure can be real happiness.")

input("\nPress the enter key to exit.")
