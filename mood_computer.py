# The Mood Computer Program
# Demonstrate the elis clause

import random

print("I sense your energy. Your true emotions are coming across my screen.")

mood = random.randint(1,3)
if mood == 1:
    # Happy mood   
    print("""
You are _ _ _

        -----------
       |           |
       |   0    0  |      
       |     <     |
       |           |
       |  .     .  |
       |   '...'   |
        -----------
        """)

elif mood == 2:
    # Neutral mood   
    print("""
You are _ _ _

        -----------
       |           |
       |   0    0  |      
       |     <     |
       |           |
       |-----------|
       |           |
        -----------
        """)


elif mood == 3:
    # Sad mood   
    print("""
You are _ _ _

        -----------
       |           |
       |   0    0  |      
       |     <     |
       |           |
       |    ...    |
       |  .'   '.  | 
        -----------
        """)

else:
    print("Illegal mood value! (You must be in a really bad mood).")

print("- - - today")

input("\n\nPress the enter key to exit.")
    
