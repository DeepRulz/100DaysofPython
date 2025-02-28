import random
from day11art import logo

print(logo)
player = []
computer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    abc = random.randint(0, 12)
    card = cards[abc]
    return card


player.append(deal_card())
player.append(deal_card())
computer.append(deal_card())
computer.append(deal_card())


def calculate_score(x):
    abcd = sum(x)
    for i in range(0, len(x)):
        if x[i] == 11:
            if abcd >= 21:
                x[i] = 1
    abcd = sum(x)
    if abcd == 21:
        return 0
    else:
        return abcd


while calculate_score(computer) < 17:
    computer.append(deal_card())
while True:
    play = calculate_score(player)
    comp = calculate_score(computer)
    print(f"Your cards: {player}, current score: {play}")
    print(f"Computer's first card: {computer[0]}")
    if comp > 21:
        print("You Won")
        print(f"Computer's final hand: {computer}, Computer's score: {comp}")
        break
    if comp == 0:
        print("The computer won")
        print(f"Computer's final hand: {computer}, Computer's score: {comp}")
        break
    if play == 0:
        print("The player won")
        print(f"Computer's final hand: {computer}, Computer's score: {comp}")
        break
    if play > 21:
        print("You lost")
        print(f"Computer's final hand: {computer}, Computer's score: {comp}")
        break
    if play < 21:
        a = input("Do you want another card? ")
        if a == "yes":
            player.append(deal_card())
        if a == "no":
            if play > comp:
                print("You won")
                print(f"Computer's final hand: {computer}, Computer's score: {comp}")
                break
            if play < comp:
                print("You lost")
                print(f"Computer's final hand: {computer}, Computer's score: {comp}")
                break
            if play == comp:
                print("It's a draw")
                print(f"Computer's final hand: {computer}, Computer's score: {comp}")
                break
