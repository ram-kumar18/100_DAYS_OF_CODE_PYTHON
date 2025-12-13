print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

cross_road = input('''You're at a cross road. Where do you want to go?
Type "left" or "right"\n''')

if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('''Type "wait" to wait for a boat. Type "swim" to swim across.\n''')

    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door_choice = input("One red, one yellow and one blue. Which colour do you choose?\n")

        if door_choice == "yellow":
            print("You found the treasure! Congratulations!")
        elif door_choice == "red":
            print("Game over. You chose the red door. The room was full of fire.")
        else:
            print("Game over. You chose the blue door. It was full of water.")
        
    else:
        print("You were eaten by an alligator")

else:
    print("You should have choosed left you fall in a hole and died")

