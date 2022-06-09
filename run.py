"""
Import the spreadsheet to retrieve the secret words
"""
from random import randrange
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


def get_secret_word():
    """
    Pulling a random word from the word column in the hangman_words google
    sheet to use as secret word
    """
    row_count = len(WORDS.col_values(1))
    row_ref_start = row_count + 1
    random_row = WORDS.row_values(randrange(1, row_ref_start))
    random_word = random_row[0]

    return random_word


def play_game():
    """
    Function to play game
    """
    secret_word = get_secret_word()
    letters_guessed = ""
    """
    Number of attempts before player fails
    """
    tries = 6

    """
    loop the game until the player fails and break when they win
    """
    while tries > 0:
        guess = input("\n Enter a letter: \n")

        if guess in secret_word:
            print(f"Well Done! The letter {guess} is in the word.")
        else:
            tries -= 1
            print(f"Sorry, the letter {guess} is not in the word.\n You have {tries} attempt(s) left.")

        """
        For loop to show correct letters guessed
        """
        letters_guessed = letters_guessed + guess
        incorrect_letter_count = 0

        for letter in secret_word:
            if letter in letters_guessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                incorrect_letter_count += 1


play_game()


def view_hangman(tries):
    """
    Create the hangman stages to be shown as the number of lives decrease
    """
    stages = [
                """
                +----------------+
                |   -------+     |
                |   |      |     |
                |   |      0     |
                |   |     /|\\   |
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
