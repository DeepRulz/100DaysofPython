from day12art import logo
import random


def easy():
    tries = 10
    k = 0
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > a:
            print("Too high")
        elif guess < a:
            print("Too low")
        else:
            print(f"You got it! The answer was {a}")
            k = 1
            break
        tries -= 1
    if k == 0:
        print("You lost")
    elif k == 1:
        print("You won")


def hard():
    k = 0
    tries = 5
    while tries > 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > a:
            print("Too high")
        elif guess < a:
            print("Too low")
        elif guess == a:
            print(f"You got it! The answer was {a}")
            k = 1
            break
        tries -= 1
    if k == 0:
        print("You lost")
    elif k == 1:
        print("You won")


a = random.randint(0, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"The correct answer is {a}")
diff = input("Choose a difficulty. Type 'easy' or 'hard':")
if diff == "easy":
    easy()
if diff == "hard":
    hard()
