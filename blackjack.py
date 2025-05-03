from random import choice, shuffle
from os import system, name as os_name
from time import sleep


blackjack_logo = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P\""""
card_blueprint_templates = {
    "heart": """
     _______ 
    |{value:<2}_ _  |
    | ( v ) |
    |  \\ /  |
    |   v   |
    |_____{value:>2}|
    """,
    "spade": """
     _______ 
    |{value:<2} .   |
    |  / \  |
    | (_._) |
    |   |   |
    |_____{value:>2}|
    """,
    "club": """
     _______ 
    |{value:<2} _   |
    |  ( )  |
    | (_._) |
    |   |   |
    |_____{value:>2}|
    """,
    "diamond": """
     _______ 
    |{value:<2} ^   |
    |  / \\  |
    |  \\ /  |
    |   .   |
    |_____{value:>2}|
    """,
    "backside" : """
     _______ 
    |,',',',|
    |,',',',|
    |,',',',|
    |,',',',|
    |_'_'_'_|
    """
}
clean_deck = [("h","a"), ("h",2), ("h",3), ("h",4), ("h",5), ("h",6), ("h",7), ("h",8), ("h",9), ("h",10), ("h","j"), ("h","q"), ("h","k"),
             ("d","a"), ("d",2), ("d",3), ("d",4), ("d",5), ("d",6), ("d",7), ("d",8), ("d",9), ("d",10), ("d","j"), ("d","q"), ("d","k"),
             ("s","a"), ("s",2), ("s",3), ("s",4), ("s",5), ("s",6), ("s",7), ("s",8), ("s",9), ("s",10), ("s","j"), ("s","q"), ("s","k"),
             ("c","a"), ("c",2), ("c",3), ("c",4), ("c",5), ("c",6), ("c",7), ("c",8), ("c",9), ("c",10), ("c","j"), ("c","q"), ("c","k")]
card_value = {
    "a": 11,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "j": 10,
    "q": 10,
    "k": 10
}
card_suit = {
    "h": "heart",
    "d": "diamond",
    "s": "spade",
    "c": "club"
}


def clear_screen():
    system('cls' if os_name == 'nt' else 'clear')


def build_game_deck(deck):
    game_deck = deck.copy()
    shuffle(game_deck)
    return game_deck


def first_deal(game_deck):
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(game_deck.pop(0))
        dealer_hand.append(game_deck.pop(0))
    return player_hand, dealer_hand, game_deck


def print_main_screen():
    clear_screen()
    print(blackjack_logo)
    print()


def print_cards_side_by_side(cards, hide_first=False):
    card_lines = []
    for i, card in enumerate(cards):
        if hide_first and i == 0:
            art = card_blueprint_templates["backside"]
        else:
            suit = card_suit[card[0]]
            value = card_value[card[1]]
            art = card_blueprint_templates[suit].format(value=value)
        lines = art.strip("\n").split("\n")
        card_lines.append(lines)
    for i in range(len(card_lines[0])):
        for card in card_lines:
            print(card[i], end="   ")
        print()


def print_computer_hand(dealer_hand):
    print("Dealer's hand:")
    print_cards_side_by_side(dealer_hand, hide_first=True)
    print()


def print_player_hand(player_hand):
    print("Your hand:")
    print_cards_side_by_side(player_hand)
    print()


def print_game_screen(player_hand, dealer_hand):
    print_main_screen()
    print_computer_hand(dealer_hand)
    print_player_hand(player_hand)
    print()


def sum_hand(cards_in_hand):
    total = 0
    ace_count = 0
    for card in cards_in_hand:
        value = card_value[card[1]]
        total += value
        if card[1] == "a":
            ace_count += 1
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total


def check_cards(cards_in_hand):
    return sum_hand(cards_in_hand) <= 20


def prompt_for_card(player_hand, dealer_hand, game_deck):
    more_cards = input("Do you want to draw another card? (y/n): ").lower()
    if more_cards == "y":
        player_hand.append(game_deck.pop(0))
        print_game_screen(player_hand, dealer_hand)
        continue_playing = check_cards(player_hand)
        if continue_playing == True:
            return prompt_for_card(player_hand, dealer_hand, game_deck)
        else:
            return player_hand, game_deck
    elif more_cards == "n":
        return player_hand, game_deck
    else:
        return prompt_for_card(player_hand, dealer_hand, game_deck)


def player_state(hand):
    return sum_hand(hand) > 21


def computer_turn(player_hand, dealer_hand, game_deck):
    player_hand_sum = sum_hand(player_hand)
    dealer_hand_sum = sum_hand(dealer_hand)
    print_main_screen()
    print("Dealer's hand:")
    print_cards_side_by_side(dealer_hand, hide_first=False)
    print()
    print_player_hand(player_hand)
    sleep(1)
    dealer_lose = player_state(dealer_hand)
    if dealer_lose == True:
        return "Dealer bust - You win!"
    else:
        if dealer_hand_sum < player_hand_sum or (dealer_hand_sum == player_hand_sum and dealer_hand_sum < 21):
            dealer_hand.append(game_deck.pop(0))
            return computer_turn(player_hand, dealer_hand, game_deck)
        elif dealer_hand_sum > player_hand_sum:
            return "Dealer wins!"
        elif dealer_hand_sum == player_hand_sum and dealer_hand_sum == 21:
            return "Draw!"


def program_ending():
    if (input("Do you want to play again? (y/n): ").lower() == "y"):
        main()
    else:
        print("Thanks for playing!")
        exit()

def main():
    game_deck = build_game_deck(clean_deck)
    player_hand, dealer_hand, game_deck = first_deal(game_deck)
    print_game_screen(player_hand, dealer_hand)
    player_hand, game_deck = prompt_for_card(player_hand, dealer_hand, game_deck)
    print_game_screen(player_hand, dealer_hand)
    player_lose = player_state(player_hand)
    if player_lose == True:
        print_game_screen(player_hand, dealer_hand)
        print("Bust - You lose!")
    else:
        message = computer_turn(player_hand, dealer_hand, game_deck)
        print_main_screen()
        print("Dealer's hand:")
        print_cards_side_by_side(dealer_hand, hide_first=False)
        print()
        print_player_hand(player_hand)
        print(message)
        sleep(1)
    program_ending()
    

if __name__ == "__main__":
    main()