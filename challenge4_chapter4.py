# Create a game where the computer picks a random word and th player has to guess that word.
# The computer tells the player how many letters are in the word.
# Then the player gets five chances to ask if a letter is in the word.
# The computer can only respond with "yes" or "no". Then, the player must guess the word.

import random

# Create a sequence of words to choose from
WORDS = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

# Pick one word randomly from the sequence
word = random.choice(WORDS)

# Get the length of the word
word_length = len(word)

# Initialize variables for letter check
remaining_chances = 5
letters_checked = []

# Introduction to the game
print("Welcome to the Word Guessing Game!")
print(f"The word has {word_length} letters.")

# Allow the player to ask if a letter is in the word (up to 5 chances)
while remaining_chances > 0:
    letter_guess = input("\nAsk if a letter is in the word: ").lower()
    
    # Validate input to ensure it's a single letter
    if len(letter_guess) != 1 or not letter_guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    # Check if the letter has already been asked
    if letter_guess in letters_checked:
        print("You have already asked about that letter.")
        continue
    
    # Update letters_checked list
    letters_checked.append(letter_guess)
    
    # Check if the letter is in the word
    if letter_guess in word:
        print("Yes")
    else:
        print("No")
    
    remaining_chances -= 1

# Player makes a final guess for the word
final_guess = input("\nNow, guess the word: ").lower()

# Check if the final guess matches the word
if final_guess == word:
    print(f"Congratulations! You guessed the word '{word}' correctly!")
else:
    print(f"Sorry, the word was '{word}'. Better luck next time!")

print("\nThanks for playing!")
input("\n\nPress the enter key to exit.")
