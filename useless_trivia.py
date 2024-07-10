# Useless Trivia
#
# Gets personal information from the use and then
# prints true but useless information about him or her

name = input("Hi, What's your name?")

age = input("How old are you?")
age = int(age)

weight = int(input("Okay, last question. How many pounds do you weigh?"))

print("\nIf poet ee cummings were to email you, he'd adrees you as", name.lower())
print("But if ee were mad, he'd call you", name.upper())


# Printing name Five Times

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

# Calculating Seconds: The user's age in second

seconds = age * 365 * 24 * 60 * 60
print("\nYou're over", seconds, "seconds old")


# Calculating moon_weight and sun_weight: The user's age in Moon and Sun

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only", moon_weight , "pounds?")

sun_weight = weight * 27.1
print("On the sun you would weigh", sun_weight, "(but, ah . . . not for long).")

input("\n\nPress the enter key to exit.
      ")
