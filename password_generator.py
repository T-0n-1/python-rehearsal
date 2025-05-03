import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']


def collectChars(number_of_letters, number_of_numbers, number_of_symbols):
    password_list = []
    for char in range(1, int(number_of_letters) + 1):
        password_list.append(random.choice(letters))
    for char in range(1, int(number_of_numbers) + 1):
        password_list.append(random.choice(numbers))
    for char in range(1, int(number_of_symbols) + 1):
        password_list.append(random.choice(symbols))
    return password_list


def shufflePassword(password_list):
    random.shuffle(password_list)
    return password_list


def listToString(list) -> str:
    return "".join(list)


print("\nWelcome to the PyPassword Generator!")
number_of_letters = input("\nHow many letters would you like in your password? ")
number_of_numbers = input("How many numbers would you like in your password? ")
number_of_symbols = input("How many symbols would you like in your password? ")
password_list = collectChars(number_of_letters, number_of_numbers, number_of_symbols)
shufflePassword(password_list)
new_password = listToString(password_list)
print(f"\nYour new password is: {new_password}")