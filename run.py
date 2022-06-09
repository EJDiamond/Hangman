"""
Import the spreadsheet to retrieve the secret words
"""
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

words = SHEET.worksheet('words')

data = words.get_all_values()

print(data)


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
                |   |     /|\\    |
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
