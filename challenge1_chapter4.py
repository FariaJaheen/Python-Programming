# Write a program that counts for the user.
# Let the user enter starting number, the ending number, and the amount by which to count.

print("\n\t\tWelcome to the Counting Number Game.\n")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
amount = int(input("Enter the amount by which to count: "))

print("Counting from ", start, "to", end, "by", amount, ":")
if start <= end:
    numbers = range(start, end + 1, amount)
else:
    numbers = range(start, end - 1, -amount)

for number in numbers:
    print(number)
    
input("\n\nPress the enter key to exit.")
