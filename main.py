import re
from urllib import response


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


response1 = input("You come to a fork in the road. Which way will you go? Type 'left' or 'right': ").casefold()
if response1 == 'left':
    response2 = input("You come to a river. Choose to 'swim' or 'wait' for a boat: ").casefold()
    if response2 == 'wait':
        response3 = input("You come to three doors. Choose 'red', 'green' or 'blue': ").casefold()
        if response3 == 'green':
            print("Well done! You got the treasure.")
        elif response3 == 'red':
            print("Hulk Hogan is behind this door and elbow drops you. Game over.")
        else:
            print("You are electrocuted and can no longer get the treasure. Game over.")
    else:
        print("You forget how to swim and are drowned to death. Game over")
else:
    print("An Ork has eaten you and you are dead. Game over.")