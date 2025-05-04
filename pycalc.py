from os import system, name as osName


line1 = "PyCalc"
line2 = "2025"
calculator = """
 _____________________
|  _________________  |
| | {line1:<15} | |
| | {line2:>15} | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def clear_screen():
    system("cls" if osName == "nt" else "clear")


def print_calculator(line1, line2):
    clear_screen()
    print(calculator.format(line1=line1, line2=line2))
    print()


def program_exit():
    print("Thank you for using PyCalc!")
    print("Exiting the program - Goodbye")
    exit()


def get_number():
    while True:
        number = input("Enter a number: ")
        if number.replace(".", "", 1).isdigit():
            return float(number)
        elif number.lower() == "q":
            program_exit()
        else:
            print("Please enter a valid number.")
            continue


def get_operator():
    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            return operator
        elif operator.lower() == "q":
            program_exit()
        else:
            print("Please enter a valid operator.")
            continue


def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 != 0:
            return number1 / number2
        else:
            return "zero div.error"


def display_number(number, line1):
    line1 += str(number)
    return line1


def display_operator(operator, line1):
    line1 += f" {operator} "
    return line1


def display_result(result, line2):
    if type(result) == str:
        line2 = result
        return line2
    result = round(result, 5)
    line2 += f" {result} "
    return line2


def main(line1, line2):
    while True:
        clear_screen()
        print_calculator(line1, line2)
        print("Welcome to PyCalc!")
        print("Enter 'q' to quit the program.")
        print()
        number1 = get_number()
        line1 = ""
        line2 = ""
        line1 = display_number(number1, line1)
        print_calculator(line1, line2)
        operator = get_operator()
        line1 = display_operator(operator, line1)
        print_calculator(line1, line2)
        number2 = get_number()
        line1 = display_number(number2, line1)
        print_calculator(line1, line2)
        result = calculate(number1, operator, number2)
        line2 = display_result(result, line2)
        print_calculator(line1, line2)


if __name__ == "__main__":
    main(line1, line2)
