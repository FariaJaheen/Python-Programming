# Question 2: Write a program that allows a user to enter his or her two favourite foods.
# The program should then print out the name of a new food by joining the original food names together.
# Solution

favfood1 = input("What is your 1st favourite food?")
favfood2 = input("What is your 2nd favourite food?")


newfood = favfood1 + favfood2
print("\nThe name of a new food by joining the original food names togethe is:", newfood,".")

input("\n\nPress enter to exit.")


# Question 3: Write a Tipper program that allows a user to enters a returant bill total.
# The program should then display two amounts: a 15 percent tip and a 20 percent tip.

bill = int(input("What is the total of resturant bill:"))

tip15 = (bill * 15)/100
tip20 = (bill * 20)/100

print("The 15 percent tip of the total bill", tip15, ".")
print("The 20 percent tip of the total bill", tip20, ".")


input("\n\nPress enter to exit.")


# Question 4: Write a Car Salesman program where the user enters the base price of a car.
# The program should add on a bunch of extra fees such as tax, license, dealer prep 
# and destination charge. Make tax and license a percent of the base price. Then other
# fees should be set values. Display the actual price of the car once all the extras are applied.

base = int(input("What is the base price of your car?"))

tax = (base * 1)/100
license_ = (base * 1)/100
dealer = 500
dest_charge = 175

actual = base + tax + license_ + dealer + dest_charge

print("\nThe actual price of the car including all the extras is", actual, ".")

input("\n\nPress enter to exit.")
