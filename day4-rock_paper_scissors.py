import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
choice = int(input())
choices = {0: rock, 1: paper, 2: scissors}
print(choices[choice])
print("Computer chose: ")
a = random.randint(0, 2)
print(choices[a])
if choice == a:
    print("Draw")
if choice > a:
    print("You won")
if choice < a:
    print("The Computer Won")