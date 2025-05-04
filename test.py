"""
name: str = input("What is your name? ")

def greet(name: str) -> None:
    print(f"Hello {name}!")

greet(name)

print(f"Your age is {input('What is your age? ')}!")

print(f"Your name has {len(name)} characters.")
"""

"""
list = ["Hello", 1, 1.23, True]

for item in list:
    print(type(item))
"""

"""
from typing import Literal

def calculate_tip(total_bill: float, tip_percentage: Literal[10, 12, 15], people: int) -> float:
    tip_percentage = float(tip_percentage/100)
    total_bill_with_tip = total_bill * (1 + tip_percentage)
    amount_per_person = total_bill_with_tip / people

    return round(amount_per_person, 2)

total_bill = float(input("What was the total bill? "))
tip_precentage = int(input("What was the tip percentage? (10/12/15) "))
people = int(input("How many people to split the bill? "))

print(f"Each person will pay {calculate_tip(total_bill, tip_precentage, people):.2f}")
"""

"""
if (int(input("Enter a number: ")) % 2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")
"""

"""
total_cost = 0
height = float(input("Enter your height in cm: "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        total_cost += 5
    elif age <= 18:
        total_cost += 7
    else:
        total_cost += 12
    if input("Do you want a photo taken? Y or N: ").upper() == "Y":
        total_cost += 3
    print(f"Your total cost is {total_cost}")       
else:
    print("Sorry, you have to grow taller before you can ride.")
"""

"""
print("Welcome to Python Pizza Deliveries!")
price = 0
size = ""
while not size:
    choose_size = input("What size pizza do you want? S, M, or L: ").upper()
    if choose_size == "S":
        price += 15
        size = choose_size
    elif choose_size == "M":
        price += 20
        size = choose_size
    elif choose_size == "L":
        price += 25
        size = choose_size
    else:
        print("Please select a valid pizza size.")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()
if extra_cheese == "Y":
    price += 1
print(f"Your final bill is: ${price}")
"""

"""
import random

friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
print(random.choice(friends))

print(friends[random.randint(0, len(friends) - 1)])
"""

"""
scores = [123, 45, 67, 89, 101, 23, 45, 67, 89, 101, 23, 45, 67, 89, 101, 23, 45, 67, 89, 101, 65, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]

max_score = 0

for score in scores:
    if score < max_score:
        continue
    max_score = score

print(f"The maximum score is: {max_score}")
"""

"""
sum = 0
for number in range(1, 101):
    sum += number
print(f"The sum of numbers from 1 to 100 is: {sum}")
"""

"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else: 
        print(number)
"""

"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if "d" in letters:
    print(letters.index("d"))
"""

"""
name1 = "Angela Yu"
name2 = "Jack Bauer"


def count_occurances(names, text):
    total = 0
    for char in text:
        total += int(names.count(char))
    return total


def calculate_love_score(name1, name2):
    names_together = name1 + name2
    names_cleaned = names_together.replace(" ", "").upper() 
    print(count_occurances(names_cleaned, "TRUE"), end = "")
    print(count_occurances(names_cleaned, "LOVE"))
"""


student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

# LIST COMPREHENSION
# {key_expression: value_expression for item in iterable}

student_grades = {
    name: (
        "Outstanding"
        if score > 90
        else (
            "Exceeds Expectations"
            if score > 80
            else "Acceptable" if score > 70 else "Fail"
        )
    )
    for name, score in student_scores.items()
}
print(student_grades)
