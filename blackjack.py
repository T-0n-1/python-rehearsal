from random import choice
from os import system, name as os_name


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
    "a": "ace",
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


def build_game_deck():
    game_deck = []
    for i in range(52):
        game_deck.append(choice(clean_deck))
        clean_deck.remove(game_deck[-1])
    return game_deck


def first_deal(game_deck):
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(game_deck.pop(0))
        dealer_hand.append(game_deck.pop(0))
    return player_hand, dealer_hand


def print_main_screen():
    clear_screen()
    print(blackjack_logo)
    print()


def print_computer_hand(dealer_hand):
    print("Dealer's hand:")
    for card in dealer_hand:
        if card == dealer_hand[0]:
            print(card_blueprint_templates[card_suit[card[0]]].format(value=card_value[card[1]]), end="   ")
        else:
            print(card_blueprint_templates["backside"], end="   ")
    print()


def print_player_hand(player_hand):
    print("Your hand:")
    for card in player_hand:
        print(card_blueprint_templates[card_suit[card[0]]].format(value=card_value[card[1]]), end="   ")
    print()
    
    
def main():
    game_deck = build_game_deck()
    player_hand, dealer_hand = first_deal(game_deck)
    print_main_screen()
    print_computer_hand(dealer_hand)
    print_player_hand(player_hand)
    print()


if __name__ == "__main__":
    main()