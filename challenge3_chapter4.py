# Improve "Word Jumble" so that each word is paired with a hint.
# The player should be able to see the hint if he or she is stuck.
# As a scoring system that rewards players who solve a jumble without asking for the hint.
 

import random

# Words and their corresponding hints
WORD_HINTS = {
    "python": "A widely-used programming language.",
    "jumble": "To mix up or confuse.",
    "easy": "Not difficult.",
    "difficult": "Not easy; requiring effort or skill to do or understand.",
    "answer": "A response to a question or problem.",
    "xylophone": "A musical instrument consisting of wooden bars that are struck with mallets."
}

# pick one word randomly from the sequence
word = random.choice(list(WORD_HINTS.keys()))

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
# 
# Initialize scoring system
score = 10  # Starting score

# start the game
print("""
            Welcome to Word Jumble

    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
""")
print("The jumble is:", jumble)
print("Hint:", WORD_HINTS[correct])  # Display hint

guess = input("\nYour guess: ").lower()

while guess != correct and guess != "":
    print("Sorry, that's not it.")
    score -= 1  # Decrease score for incorrect guesses
    guess = input("Your guess: ").lower()
    
    if guess == "hint":
        print("Hint:", WORD_HINTS[correct])  # Give hint if requested
        score -= 2  # Deduct additional points for using hint

if guess == correct:
    print(f"That's it! You guessed it!\nYour score is: {score}")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
