import random
import sys

from day14art import logo, vs
from day14gamedata import data

celeb1 = {}
celeb2 = {}
score = 0
z = 0
p = 0


def wrong():
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    sys.exit(0)


def chooser():
    global celeb1, celeb2, z
    if z == 0:
        a = random.randint(0, 49)
        celeb1 = data[a]
        print(celeb1)
        z = 1
    else:
        celeb1 = celeb2
    b = random.randint(0, 49)
    celeb2 = data[b]
    print(celeb2)


def display():
    global score, p
    chooser()
    print(logo)
    if p == 1:
        print(f"You're right! Current score : {score}")
    if p == 0:
        p = 1
    print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")
    print(vs)
    print(f"Compare B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B':")
    if choice == 'A' and celeb1['follower_count'] > celeb2['follower_count']:
        score += 1
    elif choice == 'B' and celeb1['follower_count'] < celeb2['follower_count']:
        score += 1
    else:
        wrong()


while True:
    display()
