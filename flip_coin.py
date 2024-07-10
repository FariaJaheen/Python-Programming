
# Demonstrates Flipping a coin 100 Times Program 
import random

heads_count = 0
tails_count = 0

for i in range(100):
    flip = random.choice(['heads', 'tails'])
    if flip == 'heads':
        heads_count += 1
    else:
        tails_count += 1

print("Number of heads:", heads_count)
print("Number of tails:", tails_count)

input("\nPress the enter key to exit.")


