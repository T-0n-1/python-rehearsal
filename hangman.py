import random
import os


words = ["python", "hangman", "programming", "challenge",
        "computer", "science", "artificial", "intelligence",
        "machine", "learning", "data", "analysis",
        "visualization", "statistics", "algorithm", "function",
        "variable", "loop", "condition", "array",
        "string", "object", "class", "inheritance",
        "encapsulation", "polymorphism", "recursion", "debugging",
        "exception", "syntax", "semantic", "compiler", 
        "interpreter", "framework", "library", "module",
        "repository", "version", "control", "git",
        "github", "collaboration", "deployment", "integration",
        "testing", "automation", "continuous", "delivery",
        "devops", "agile", "scrum", "kanban",
        "sprint", "backlog", "standup", "retrospective",
        "user", "story", "requirement", "specification",
        "design", "architecture", "database", "sql",
        "nosql", "mongodb", "postgresql", "mysql",
        "redis"]


visuals = [
        """
           -----
           
        """,
        """
           -----
           |   |
           |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """
    ]


def get_random_word():
    return random.choice(words)


def print_visuals(number):
    return visuals[number]


def play_hangman():
    word = get_random_word()
    guessed_letters = []
    wrong_guesses = 0
    guessed_word = ["_"] * len(word)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Hangman!")
    print(print_visuals(wrong_guesses))
    print("Word: " + " ".join(guessed_word))

    while wrong_guesses < 5 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        os.system('cls' if os.name == 'nt' else 'clear')
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            wrong_guesses += 1
            print(f"Wrong guess. You have {5 - wrong_guesses} tries left.")

        print(print_visuals(wrong_guesses))
        print("Word: " + " ".join(guessed_word))

    if "_" not in guessed_word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Sorry, you've run out of tries. The word was: {word}")


def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()