# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'?"))

if money:    #Interpretation of a value as True or False; "if money:" is equivalent to "if money != 0"
    print("Ah, I am reminded of a table. Right this way.")
else:
    print("Please, sit. It may be a while.")


input("\n\nPress enter to exit.")
