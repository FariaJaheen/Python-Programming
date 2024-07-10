# Finicky Counter
# Demostrates the break and continue statements

count = 0
while True:
    count += 1

    # End loop if count greater than 10
    if count > 10:
        break

    # Skip
    if count == 5:
        continue
    print(count)


input("\n\nPress enter to exit.")
