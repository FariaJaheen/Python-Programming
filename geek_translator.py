# Geek Translator
# Demonstrates using dictionaries

geek = {"404": "clueless. From the wb error message 404, meaning page not found.",
        "Googling" : "seraching the internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in computer keyboard.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "the act of shrinking electronics device to make it work.",
        "Uninstalled" : "being fired. Especially popular during the dot-bomb era."}



# Now check the following code in IDLE for using a key to retrieve a value
# geek["404"]
# geek["Link Rot"]


# Now check the following code in IDLE with the in operator before retrieving a value
# geek["Dancing Baloney"]
#if "Dancing Baloney" in geek:
#    print("I know what Dnacing Balony is.")
#else:
#   print("I have no idea what Dnacing Balony is.")


# Now check the following code in IDLE for using the get() Method to retrieve a value
# print(geek.get("Dancing Baloney" , "I have no idea"))
# print(geek.get("Dancing Baloney"))


# Displaying the menu
choice = None
while choice != 0:
    print(
    """
    Geek Translator

    0 - Quit
    1 - Look Up a Geek Term
    2 - Add  a Geek Term
    3 - Redifine a Geek Term
    4 - Delete  a Geek Term
    """
    )

    choice = input("Choice:")
    print()

    # Exit
    if choice == "0":
        print("Good-bye.")


    # Get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)


    # Get a term-definition pair
    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added")
        else:
            print("\nThat term already exists! Try redefining it.")


    # Redefine an existing term
    elif choice == "3":
        term = input("What term do you want me to redefine?: ")
        if term in geek:
            definition = input("\nWhat's the new definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefined")
        else:
            print("\nThat term doesn;t exist! Try adding it.")


    # Delete a term
    elif choice == "4":
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("\nOkay I deleted", term)
        else:
            print("\nI can't do that!", term, "doesn't exist in the dictionary.")

    # Some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice")

input("\n\nPress the enter key to exit.")


