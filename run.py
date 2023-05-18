import random
import questions

# Get player name
def get_player_name():
    try:
        player_name = input("Enter your name: ")
        if len(player_name) == 0 or len(player_name) > 10 or len(player_name) < 3:
            raise ValueError
        if not player_name.isalpha():
            print("Invalid input! Please enter a valid name (letters only).")
            return get_player_name()
        else:
            return player_name.capitalize()
    except ValueError:
        print("Invalid input! Please enter a valid name (Between 3 to 10 characters).")
        return get_player_name()

player_name = get_player_name()


# welcoming
print("---------------------------------------------------")
print(f"Hello {player_name}! Welcome to Who Wants to Be a Millionaire!")
print("---------------------------------------------------")


# Game rules


# Game loop
def game_loop():
    # Initialize variables


    # Shuffle the questions


    # Define the money increment pattern


    # Function for checking the answer


    # Function for getting user's answer


    # Function for handling a single question


        # Get user's answer


        # Check if the answer is correct


    # Game loop


    # Game ended


    # Ask if the player wants to play again



game_loop()
