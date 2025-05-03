from getpass import getpass
import os


alphabets = "abcdefghijklmnopqrstuvwxyz"
logo = """
        d8b        888                     
        Y8P        888                     
                   888                     
 .d8888b88888888b. 88888b.  .d88b. 888d888 
d88P"   888888 "88b888 "88bd8P  Y8b888P"   
888     888888  888888  88888888888888     
Y88b.   888888 d88P888  888Y8b.    888     
 "Y8888P88888888P" 888  888 "Y8888 888     
           888                             
           888                             
           888                           
      """


def user_input_message():
    return input("Enter a message: ").lower()
        

def letter_shift():
    while True:
        letter_shift = input("Enter a letter shift (1-25): ")
        if letter_shift.isdigit() and 1 <= int(letter_shift) <= 25:
            return int(letter_shift)
        else:
            continue


def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char in alphabets:
            index = (alphabets.index(char) + shift) % len(alphabets)
            encoded_message += alphabets[index]
        else:
            encoded_message += char
    return encoded_message


def decode_message(message, shift):
    decoded_message = ""
    for char in message:
        if char in alphabets:
            index = (alphabets.index(char) - shift) % len(alphabets)
            decoded_message += alphabets[index]
        else:
            decoded_message += char
    return decoded_message


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{logo}")
        print()
        choice = input("Would You like to [E]ncode or [D]ecode a message or [Q]uit? ").lower()
        if choice == "e":
            print(f"Encoded message: {encode_message(user_input_message(), letter_shift())}")
            getpass("Press Enter to continue...")
        elif choice == "d":
            print(f"Decoded message: {decode_message(user_input_message(), letter_shift())}")
            getpass("Press Enter to continue...")
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            continue


if __name__ == "__main__":
    main()