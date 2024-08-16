def clear_screen():
    print("\n" * 100)


bids = {}
other_users_exist = 'yes'

while other_users_exist == 'yes':
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    other_users_exist = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if other_users_exist == 'yes':
        clear_screen()

highest_bidder = max(bids, key=bids.get)
print(f"The winner is {highest_bidder} with a bid of {bids[highest_bidder]}")
