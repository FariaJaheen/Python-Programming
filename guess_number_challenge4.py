# Demonstrates Guess My Number by the Computer

print("Think of a number between 1 and 100 and I will try to guess it.")

# Initialize the range
low = 1
high = 100
attempts = 0

# Loop until the guess is correct
while True:
    # Make a guess in the middle of the current range
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is {guess}.")
    
    # Get feedback from the player
    feedback = input("Is it 'high', 'low', or 'correct'? ").strip().lower()

    if feedback == "correct":
        print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
        break
    elif feedback == "high":
        high = guess - 1  # Adjust the high end of the range
    elif feedback == "low":
        low = guess + 1  # Adjust the low end of the range
    else:
        print("Invalid input. Please respond with 'high', 'low', or 'correct'.")
        
input("\nPress the enter key to exit.")
