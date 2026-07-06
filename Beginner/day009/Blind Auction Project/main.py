def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a highest bid of ${highest_bid} ")


from art import logo

print(logo)
bids = {}
status = True
while status:
    name = input("Enter your name\n")
    bid_price = int(input("Enter the bid price"))
    bids[name] = bid_price

    user_status = input("Are there any more users that are participating?").lower()
    if user_status == "yes":
        print("\n" * 100)
    else:
        status = False
        highest_bidder(bids)


# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
