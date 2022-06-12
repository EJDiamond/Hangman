"""
Import the spreadsheet to retrieve the secret words
"""
from random import randrange
import os
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread. authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')
WORDS = SHEET.worksheet('words')

# Global variable to hold the random_row
random_row = None


def welcome_screen():
    """
    Hangman banner on home screen
    """
    result = pyfiglet.figlet_format("HANGMAN")
    print(result)


welcome_screen()


def clear_terminal():
    """
    Function to tclear the terminal after selections
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_guess(guess, letters_guessed):
    """
    Validating that the guess is a letter and hasn't already been guessed
    """
    if (guess not in letters_guessed) and guess.isalpha() and (len(guess) == 1):
        return True
    else:
        if guess in letters_guessed:
            print(f"{guess} has already been guessed")
        if guess.isalpha() is False:
            print("Only letters are valid")
        if len(guess) != 1:
            print("Only one letter can be guessed at a time")     
        return False


def get_random_row():
    """
    Pulls a random row from the google sheet for word and hint
    """
    global random_row
    random_row = WORDS.row_values(randrange(1, len(WORDS.col_values(1))))


def get_secret_word():
    """
    Uses index 0 from random row to pull the random word
    """
    global random_row
    return random_row[0]


def get_secret_hint():
    """
    Uses index 1 from random row to pull the random word's hint
    """
    global random_row
    return random_row[1]


def play_game():
    """
    Function to play game
    """
    get_random_row()
    secret_word = get_secret_word()
    hint = get_secret_hint()
    letters_guessed = ""

    # Number of attempts before player fails
    tries = 6
    print(view_hangman(tries))

    # Loop the game until the player fails, and break when they win
    while tries > 0:

        guess = input("  " * 10 + "\nEnter a letter: \nFor the hint type: hint \n")

        # Validates the guess and then checks if it is in the secret word.
        # If the letter is incorrect, tries increments by 1.
        if guess == "hint":
            print(hint)
        else:
            if validate_guess(guess, letters_guessed):  
                if guess in secret_word:
                    print("")
                    print(f"Well Done! The letter {guess} is in the word.")
                    print("")
                    print(view_hangman(tries))
                else:
                    tries -= 1
                    print("")
                    print(f"Sorry, the letter {guess} is not in the word.\n")
                    print(f"You have {tries} attempt(s) left.\n")
                    print("")
                    print(view_hangman(tries))
        
                # Letters guessed variable adds each guess, so the user can see 
                # what they have already tried.
                letters_guessed = letters_guessed + guess
                incorrect_letter_count = 0

                # Adds the letter to the word if it correct and prints an
                # underscore if it is incorrect.
                for letter in secret_word:
                    if letter in letters_guessed:
                        print(f"{letter}", end="")
                    else:
                        print("_", end="")
                        incorrect_letter_count += 1

                # Prints letters guessed each time a new letter is guessed.
                print("")
                print(f"\nLetters guessed: {letters_guessed}")

                # If incorrect letter count = 0 after the loop runs, the player
                # has guessed the whole word correctly and the loop breaks.
                if incorrect_letter_count == 0:
                    print("")
                    print(f"Congratulations! The word was {secret_word}")
                    break
                
        
    # If the incorrect letter count = 6 the player loses.
    else:
        print("")
        print(f"Sorry you lose! The word was {secret_word}")
        loser_play_again = input("\nWould you like to play again? / Y\n")

        if loser_play_again == "Y":
            play_game()


def view_hangman(tries):
    """
    The hangman stages to be shown as the number of lives decrease
    """
    stages = [
                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |     /|\    |
                |   |     / \    |
                |   |            |
                |   ----------   |
                +----------------+""",

                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |     /|\    |
                |   |     /      |
                |   |            |
                |   ----------   |
                +----------------+""",

                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |     /|\    |
                |   |            |
                |   |            |
                |   ----------   |
                +----------------+""",

                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |     /|     |
                |   |            |
                |   |            |
                |   ----------   |
                +----------------+""",
                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |      |     |
                |   |            |
                |   |            |
                |   ----------   |
                +----------------+""",
                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |            |
                |   |            |
                |   |            |
                |   ----------   |
                +----------------+""",
                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |            |
                |   |            |
                |   |            |
                |   |            |
                |   ----------   |
                +----------------+""",
            ]
    return stages[tries]


play_game()
