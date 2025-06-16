bid_offers = {}
bidding_finished = False


def highest_bidder(current_auction):
    high_bid = 0
    winner = ''
    for bidder in current_auction:
        current_bid = int(current_auction[bidder])
        if current_bid > high_bid:
            high_bid = current_bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}")

while not bidding_finished:
    bidder_name = input("What is your name?:\n")
    bid = input("What is your bid?:\n")
    bid_offers[bidder_name] = bid

    more_bids = input("Does anyone else want to bid? Type 'yes' or 'no':\n")

    if more_bids == "no":
        bidding_finished = True
        print("\n" * 50)
        highest_bidder(bid_offers)
    else:
        print("\n" * 50)