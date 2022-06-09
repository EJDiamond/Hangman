"""
Import the spreadsheet to retrieve the secret words
"""
import gspread
from google.oauth2.service_account import Credentials
from random import randrange

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


def secret_word():
    """
    Pulling a random word from the word column in the hangman_words google sheet to use as secret word
    """
    row_count = len(WORDS.col_values(1))
    row_ref_start = row_count +1
    random_row = WORDS.row_values(randrange(1, row_ref_start))
    random_word = random_row[0]
    

    print(random_word)

secret_word()


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
