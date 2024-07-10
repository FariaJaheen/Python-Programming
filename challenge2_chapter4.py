# Create a program that gets a message from the user and then prints it out backwards.

print("\n\t\tWelcome to the Printing Message in Backwards Game\n")

# Get message from the user
message = input("Enter your message here:")

# Initialize an empty string to store the reversed message
reversed_message = ""

# Iterate over each character in the message from last to first
for i in range(len(message) - 1, -1, -1):
    reversed_message += message[i]

# Print the reversed message
print("Reversed of the message you entered is:", reversed_message)

input("\n\nPress the enter key to exit.")
