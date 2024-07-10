# Hero's Inventory
# Demonstrates tuple creation

# Create an empty inventory
inventory = ()

# Treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("\n\nPress the enter key to continue.")

# Create a tuple with some items
inventory = ("sword",
             "armor",
             "sheild",
             "healing potion")
# Print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# Print each element of the tuple
print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
