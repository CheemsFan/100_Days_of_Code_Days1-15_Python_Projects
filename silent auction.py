import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

should_continue = True

contestants = {}
while should_continue:

    identification = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    contestants[identification] = price
    more_bidding = input("Is there anyone else bidding? 'Yes' or 'No'?").lower()
    if more_bidding == "no":
        should_continue = False
        find_highest_bidder(contestants)
    elif more_bidding == "yes":
        print("\n" * 20)

