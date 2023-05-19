# Who Wants to Be a Millionaire Game

This is a Python program that simulates the game "Who Wants to Be a Millionaire." It presents a series of multiple-choice questions to the player and allows them to answer in order to win money. The game ends if the player answers a question incorrectly or if they reach the $1,000,000 question and answer it correctly.

## Table of Contents


## UX
# Strategy:
   - The code implements the game "Who Wants to Be a Millionaire" and focuses on engaging the player by presenting multiple-choice questions and offering the opportunity to win money.
   - The strategy includes defining the game rules, presenting questions in an intuitive manner, and providing feedback on the player's answers.

# User Stories:
   - The code aims to cater to the user's needs and desires by providing an interactive and enjoyable game experience.
   - User stories may include scenarios like "As a player, I want to be able to enter my name to personalize the game" or "As a player, I want to receive feedback on whether my answer is correct or incorrect."

# Scope:
   - The scope of the code is to simulate the "Who Wants to Be a Millionaire" game, allowing users to play, answer questions, accumulate winnings, and potentially become a millionaire.
   - The code's scope may involve defining the number of questions, the money increment pattern, and the end condition.

# Structure:
   - The code follows a structured approach to ensure the flow of the game. It includes functions for getting the player's name, displaying game rules, asking questions, checking answers, and handling game progression.
   - The code organizes these functions within the `game_loop` function, which serves as the main structure of the game.

# App Logic:
   - The code's logic revolves around presenting questions, validating user input, checking answers, updating the player's winnings, and determining game outcomes.
   - It ensures that the game follows the logic of the "Who Wants to Be a Millionaire" TV show, where players progress through questions, earn money for correct answers, and face potential game-ending scenarios.

# Skeleton and Surface:
   - The code provides the basic structure (skeleton) for the game, including functions and logical flow.
   - The code's surface represents the user interface, which includes displaying the game title, prompts for user input, presenting questions, and showing feedback messages.

# Text Layouts:
   - The code utilizes text layouts to present information clearly and legibly to the player.
   - It includes the presentation of the game title, player name, questions, answer options, feedback messages, and total winnings.

# Chromatics:
   - While the code doesn't explicitly involve visual design elements, chromatics can be applied to enhance the user experience through the selection of appropriate colors, fonts, and text formatting.
   - The code can benefit from using color or font variations to distinguish different sections of the game or to emphasize important messages.

By considering these UX concepts, the code can provide a more engaging and user-friendly experience for players interacting with the "Who Wants to Be a Millionaire" game.


## Features

- Multiple-choice questions: The game presents a series of questions to the player, each with four options (labeled as a, b, c, d).
- User input: The player can enter their answer by selecting the corresponding letter (a, b, c, d).
- Correct answer validation: The program checks if the user's answer is correct and provides appropriate feedback.
- Money winnings: The player wins a specific amount of money for each correct answer. The amount increases progressively for each question.
- Game over: If the player answers a question incorrectly, the game ends, and their total winnings are displayed.
- Play again option: After the game ends, the player is asked if they want to play again. If they choose to do so, the game restarts.

## Usage

1. Run the Python program using a Python interpreter.
2. The program will display the welcome message and ask for the player's name.
3. Enter the player's name (up to 10 characters) and press Enter.
4. The program will display the game rules.
5. Press Enter to start the game.
6. The program will present a series of questions and ask the player to choose the correct answer by entering the corresponding letter (a, b, c, d).
7. After each question, the program will indicate if the answer is correct and display the amount of money won.
8. If the player answers a question incorrectly, the game ends, and their total winnings are displayed.
9. If the player answers the $1,000,000 question correctly, they become a millionaire, and the game ends.
10. After the game ends, the player is asked if they want to play again. Enter "y" to play again or any other key to exit the game.

## Customization

- Questions: The questions for the game are imported from a separate module named `questions.py`. You can modify the questions and options in that module to customize the game content.
- Money increments: The amount of money won for each question is defined in the `money_increments` list. You can modify the values in this list to change the progression of winnings.

**Note:** This program assumes that the `questions.py` module is present and contains a list of questions in the specified format. Ensure that the `questions.py` module is available and correctly formatted for the game to function properly.

Enjoy playing "Who Wants to Be a Millionaire"!