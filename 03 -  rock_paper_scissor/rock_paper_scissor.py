import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojies = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
choices = tuple(emojies.keys())
print(choices)


def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):
    print(f"You chose {emojies[user_choice]}")
    print(f"Computer chose {emojies[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")
    else:
        print("You lose")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_game = input("Contine? (y/n): ").lower()
        if continue_game == "n":
            break


play_game()
