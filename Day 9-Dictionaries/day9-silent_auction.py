from day9art import logo
print(logo)
bids = {}


def bidder():
    global bids
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    print("Kindly press clear all to save your bid")
    choice = input("Are there any bidders? Type 'yes' or 'no'.")
    if choice == 'yes':
        bidder()
    if choice == 'no':
        a = 0
        na = ""
        for i in bids:
            if bids[i] > a:
                na = i
                a = bids[i]
        print(f"The winner is {na} with a bid of {a}")


print("Welcome to the secret auction program.")
bidder()
