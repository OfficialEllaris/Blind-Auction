from art import logo
from replit import clear

print(logo)
print("Welcome to the secret auction program.")

auction_db = {}

def store_bidder(name, amount):
    auction_db[name] = amount

auction_finished = False

while not auction_finished:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $"))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    store_bidder(name, amount)

    if continue_auction == "no":
        clear()
        auction_finished = True
    else:
        clear()
        print("Welcome to the secret auction program.")

def auction_result(auction_db):
    highest_bid = 0
    auction_winner = ""

    for bidder in auction_db:
        if auction_db[bidder] > highest_bid:
            auction_winner = bidder
            highest_bid = auction_db[bidder]
    print(f"The winner is {auction_winner} with a bid of ${highest_bid}")
    
auction_result(auction_db)