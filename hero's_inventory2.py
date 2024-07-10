# Hero's inventory 2.0
# Demonstrates tuples

# Create a tuple with some items and diplay with a for loop
inventory = ("sword,",
             "armor",
             "sheild",
             "healing potion")
print("Your items:")
for item in inventory:
    print(item)
input("\nPress the enter key to continue.")

# get the length of a tuple
print("You have ", len(inventory)," items in your possession.")
input("\nPress the enter key to continue.")

# test for membership in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# diplay one item through an index   
index = int(input("\nEnter the index number for an item in inventory:"))
print("At index", index, "is ", inventory[index])


#display a slice
start = int(input("\nEnter the index number to begin a slice:"))
finish = int(input("Enter the index number to end a slice:"))
print("inventory[", start, ":", finish, "] is", end = "")
print(inventory[start:finish])
input("\nPress the enter key to continue.")


# concantenate two tuples
chest = ("gold",
         "gem")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)	
input("\n\nPress the enter key to exit.")
