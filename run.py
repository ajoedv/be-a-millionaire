import random
import questions
from colorama import Fore, Back, Style


# text color style functions
def red_text():
    print(Fore.RED + '')


def green_text():
    print(Fore.GREEN + '')


def blue_text():
    print(Fore.BLUE + '')


def red_text_back():
    print(Back.RED + '')


def green_text_back():
    print(Back.GREEN + '')


def blue_text_back():
    print(Back.BLUE + '')


def color_rest():
    print(Style.RESET_ALL)


# Get player name
def get_player_name():
    try:
        blue_text()
        player_name = input("Enter your name: ")
        color_rest()
        if not (3 <= len(player_name) <= 10) or not player_name.isalpha():
            raise ValueError
        return player_name.capitalize()
    except ValueError:
        red_text()
        print("Invalid input! Please enter a valid name (between 3 to 10 alphabetic characters).")
        color_rest()
        return get_player_name()

player_name = get_player_name()


# welcoming
print("---------------------------------------------------")
blue_text()
print(f"Hello {player_name}! Welcome to Who Wants to Be a Millionaire!")
color_rest()
print("---------------------------------------------------")


# Game rules
print("---------------------------------------------------")
red_text()
print("Game Rules:")
color_rest()
print("1. You will be asked a series of multiple-choice questions.")
print("2. Choose the correct answer by"
      "entering the corresponding letter (a, b, c, d).")
print("3. If you answer a question correctly,"
      "you will win the corresponding amount of money.")
print("4. If you answer a question incorrectly,"
      "the game is over.")
print("5. If you reach the $1,000,000 question"
      "and answer it correctly, you will become a millionaire!")
print("---------------------------------------------------")
green_text()
input("Press Enter to start the game.")
color_rest()


# Game loop
def game_loop():
    # Initialize variables
    total_questions = len(questions.questions)
    current_question = 0
    money = 0

    # Shuffle the questions
    random.shuffle(questions.questions)

    # Define the money increment pattern
    money_increments = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    # Function for checking the answer
    def check_answer(question, user_answer):
        if user_answer.lower() == question["answer"]:
            nonlocal money
            money = money_increments[current_question]  # Update the money won
            print("---------------------------------------------------")
            green_text_back()
            print("Correct answer! You've won ", money, " $")
            color_rest()
            print("---------------------------------------------------")
            return True
        else:
            print("---------------------------------------------------")
            red_text_back()
            print("Wrong answer! Game Over!")
            color_rest()
            print("---------------------------------------------------")
            return False

    # Function for getting user's answer
    def get_user_answer():
        try:
            blue_text()
            user_answer = input("Enter your answer (a, b, c, d): ")
            color_rest()
            if user_answer.lower() not in ['a', 'b', 'c', 'd']:
                raise ValueError
            return user_answer.lower()
        except ValueError:
            print("---------------------------------------------------")
            red_text()
            print("Invalid input! Please enter a valid option (a, b, c, d).")
            color_rest()
            print("---------------------------------------------------")

    # Function for handling a single question
    def ask_question(question):
        print("---------------------------------------------------")
        blue_text()
        print(player_name, ":", question["question"])
        color_rest()
        print("---------------------------------------------------")
        for option in question["options"]:
            print(option)

        # Get user's answer
        user_answer = get_user_answer()
        while user_answer is None:
            user_answer = get_user_answer()

        # Check if the answer is correct
        return check_answer(question, user_answer)

    # Game loop
    while current_question < total_questions:
        question = questions.questions[current_question]
        if not ask_question(question):
            break

        current_question += 1

        # Check if the player becomes a millionaire
        if money >= 1000000:
            green_text_back()
            print("---------------------------------------------------")
            print("Congratulations,", player_name +
                  "! You become a millionaire!")
            print("---------------------------------------------------")
            color_rest()
            break

    # Game ended
    blue_text_back()
    print("---------------------------------------------------")
    print("Game Over!")
    print("Total winnings: ", money, " $")
    print("---------------------------------------------------")
    color_rest()

    # Ask if the player wants to play again
    while True:
        try:
            blue_text()
            play_again = input("Do you want to play again? (y/n): ")
            color_rest()
            play_again = play_again.lower()
            if play_again == "y":
                game_loop()
                break
            elif play_again == "n":
                blue_text()
                print("Thank you for playing Who Wants to Be a Millionaire!")
                color_rest()
                break
            elif play_again == 0:
                red_text()
                print("Invalid input. Please enter 'y' to play again or 'n' to quit.")
                color_rest()
            else:
                raise ValueError

        except ValueError:
            red_text()
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")
            color_rest()


game_loop()
