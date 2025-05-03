import random


art_gallery = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}


def drawRandomChoice():
    options = ['rock', 'paper', 'scissors']
    random_choice = random.choice(options)
    return random_choice


def getUserChoice():
    user_choice = input("What do you choose - rock, paper or scissors? Type [R / P / S]: ").lower()
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice == "s":
        user_choice = "scissors"
    else: 
        print("Invalid choice. Please try again.")
        return getUserChoice()
    return user_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play against the computer.")
    print("The rules are simple:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print()
    
    user_choice = getUserChoice()
    computer_choice = drawRandomChoice()

    print(f"You chose:\n{art_gallery[user_choice]}")
    print(f"Computer chose:\n{art_gallery[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()