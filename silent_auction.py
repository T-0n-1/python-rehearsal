from getpass import getpass
from os import system, name as osName


bidder_list: dict[str, str] = {} 
ascii_gavel = """
   ___________
   \\         /
    )_______(
    |_______|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )_______(
    /_______\\
   / ------- \\
  -------------
/_______________\\"""


def clear_screen():
    system('cls' if osName == 'nt' else 'clear')


def get_bidder_name():
    name = input("What is your name? ")
    return name


def get_bidder_bid(name):
    while True:
        bid = getpass(f"What is your bid {name}? $")
        if bid.isdigit() and int(bid) > 0:
            return int(bid)
        else:
            print("Please enter a valid bid amount.")
            continue


def another_auction():
    bidder_list.clear()
    another_auction = input("Would you like to take a part in another auction? (Y/N): ").upper()
    if another_auction == "Y":
        main()
    else:
        print("Goodbye!")


def main():
    while True:
        clear_screen()
        print(ascii_gavel)
        print()
        print("Welcome to the Silent Auction!")
        name = get_bidder_name()
        bid = get_bidder_bid(name)
        print(f"Thank you {name}, your bid has been recorded.")
        bidder_list[name] = bid
        another_bidder = input("Is there another bidder? (Y/N): ").upper()
        if another_bidder == "Y":
            continue
        else:
            break
    clear_screen()
    print(ascii_gavel)
    print()
    print("Bidding has ended.")
    print("The winner is:")
    highest_bidder = max(bidder_list, key=bidder_list.get)
    print(f"{highest_bidder} with a bid of ${bidder_list[highest_bidder]}!")
    print()
    print("Thank you for participating in the Silent Auction!")
    another_auction()


if __name__ == "__main__":
    main()