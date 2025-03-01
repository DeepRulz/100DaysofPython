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
print("You are at a cross road. Where do you want to go?")
d = input("left or right?")
if d == "left":
    print("You have reached a lake. There is an island in the middle of the lake")
    print("You can swim through the lake or wait for a boat to come")
    s = input("What do you do? swim or wait?")
    if s == "wait":
        print("The boat arrives and takes you to the island")
        print("There are 3 doors on the island.")
        do = input("Which one do you choose? red,yellow or blue")
        if do == "red":
            print("You got burned by fire")
            print("Game Over")
        elif do == "blue":
            print("You got eaten by beasts")
            print("Game Over")
        elif do == "yellow":
            print("You Win")
        else:
            print("Game Over.")
    else:
        print("You got attacked by trouts")
        print("Game Over")
else:
    print("You fell into a hole")
    print("Game Over")