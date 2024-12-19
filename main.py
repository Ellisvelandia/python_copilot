# name = "Ellis"

# print(f"Hello, {name}!")

# # explain loops

# loops = ["for", "while"]

# for loop in loops:
#     print(f"{loop} loops are used to iterate over a sequence of elements.")

# # difference betweens for and while loops

# # for loop

# for i in range(5):
#     print(i)

# # while loop

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# let's see how we can use loops to iterate over a list of names

# names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# for name in names:
#     print(name)

# # lets see how we can use loops to iterate over a list of numbers

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# # lets see how we can use loops to iterate over a list of mixed data types

# mixed = ["Alice", 1, "Bob", 2, "Charlie", 3, "David", 4, "Eve", 5]

# for item in mixed:
#     print(item)

# # lets see how we can use loops to iterate over a list of dictionaries

# movies = [
#     {"title": "The Shawshank Redemption", "year": 1994},
#     {"title": "The Godfather", "year": 1972},
#     {"title": "The Dark Knight", "year": 2008},
#     {"title": "Forrest Gump", "year": 1994},
#     {"title": "Inception", "year": 2010},
# ]

# for movie in movies:
#     print(f"{movie['title']} ({movie['year']})")

# lets create a game of rock, paper, scissors

import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ")
    return user_choice


def check_win(user_choice, computer_choice):
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    outcome = "win" if wins_against[user_choice] == computer_choice else "lose" if wins_against[computer_choice] == user_choice else "tie"
    print("You " + outcome + "!")


def score(user_choice, computer_choice):
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    outcome = wins_against.get(user_choice) == computer_choice
    return 1 if outcome else -1 if wins_against.get(computer_choice) == user_choice else 0


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")
        check_win(user_choice, computer_choice)
        print(f"Score: {score(user_choice, computer_choice)}")
        play_again = input("Would you like to play again (yes/no)? ").strip().lower()
        if play_again != "yes":
            break


play_game()

