from bjdata import * 
from os import system, name as os_name
from random import choice, shuffle
from time import sleep


def program_ending():
    if input("Do you want to play again? (y/n): ").lower() == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()


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
        if dealer_hand_sum < player_hand_sum or (
            dealer_hand_sum == player_hand_sum and dealer_hand_sum < 21
        ):
            dealer_hand.append(game_deck.pop(0))
            return computer_turn(player_hand, dealer_hand, game_deck)
        elif dealer_hand_sum > player_hand_sum:
            return "Dealer wins!"
        elif dealer_hand_sum == player_hand_sum and dealer_hand_sum == 21:
            return "Draw!"


def player_state(hand):
    return sum_hand(hand) > 21


def check_cards(cards_in_hand):
    return sum_hand(cards_in_hand) <= 20


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


def print_cards_side_by_side(cards, hide_first=False):
    card_lines = []
    for i, card in enumerate(cards):
        if hide_first and i == 0:
            art = card_blueprint_templates["backside"]
        else:
            suit = card_suit[card[0]]
            display = card_label[card[1]]
            art = card_blueprint_templates[suit].format(value=display)
        lines = art.strip("\n").split("\n")
        card_lines.append(lines)
    for i in range(len(card_lines[0])):
        for card in card_lines:
            print(card[i], end="   ")
        print()


def print_player_hand(player_hand):
    print("Your hand:")
    print_cards_side_by_side(player_hand)
    print()


def print_computer_hand(dealer_hand):
    print("Dealer's hand:")
    print_cards_side_by_side(dealer_hand, hide_first=True)
    print()


def clear_screen():
    system("cls" if os_name == "nt" else "clear")


def print_main_screen():
    clear_screen()
    print(blackjack_logo)
    print()


def print_game_screen(player_hand, dealer_hand):
    print_main_screen()
    print_computer_hand(dealer_hand)
    print_player_hand(player_hand)
    print()


def first_deal(game_deck):
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(game_deck.pop(0))
        dealer_hand.append(game_deck.pop(0))
    return player_hand, dealer_hand, game_deck


def build_game_deck(deck):
    game_deck = deck.copy()
    shuffle(game_deck)
    return game_deck


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
