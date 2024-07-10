# Trust Fund Program - Bad
# Demonstrates a logical error

print(
"""

              Trust Fund Buddy
Totals your monthly spending so that your trust fund doesn\'t run out
(and you\'re forced to get a real job).

Please enter the requested, monthly costs. Since you\'re rich, ignore pennies
and use only dollar amounts.

""")

car = input("Lamborghini Tune-Ups:")
rent = input("Manhattan Apartment:")
jet = input("Private Jet Rental:")
gifts = input("Gifts:")
food = input("Dining Out:")
staff = input("Staff (butlers, chef, driver, assistant):")
guru = input("Personal Guru and Coach:")
game = input("Computer Game:")


total = car + rent + jet + gifts + food + staff + guru + game

print("Grand Total:", total)

input("\n\nPress the enter key to exit.")






# Trust Fund Program - Good
# Demonstrates a fixing the logical error

print(
"""

              Trust Fund Buddy
Totals your monthly spending so that your trust fund doesn\'t run out
(and you\'re forced to get a real job).

Please enter the requested, monthly costs. Since you\'re rich, ignore pennies
and use only dollar amounts.

""")

car = int(input("Lamborghini Tune-Ups:"))
rent = int(input("Manhattan Apartment:"))
jet = int(input("Private Jet Rental:"))
gifts = int(input("Gifts:"))
food = int(input("Dining Out:"))
staff = int(input("Staff (butlers, chef, driver, assistant):"))
guru = int(input("Personal Guru and Coach:"))
game = int(input("Computer Game:"))


total = car + rent + jet + gifts + food + staff + guru + game

print("Grand Total:", total)

input("\n\nPress the enter key to exit.")
