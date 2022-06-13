"""
Import the spreadsheet to retrieve the secret words
"""
from random import randrange
import os
from pyfiglet import Figlet
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
HIGHSCORES = SHEET.worksheet('highscores')

scores = HIGHSCORES.get_all_records()
# results = {}

# Global variable to hold the random_row
RANDOM_ROW = None
USERNAME = None


def welcome_screen():
    """
    Hangman banner on home screen
    """
    result = Figlet(font='big', justify="center")
    print("")
    print(result.renderText("HANGMAN"))
    tries = 0
    print(view_hangman(tries))


def get_username():
    """
    User enters their name, letters only
    """
    global USERNAME
    USERNAME = input("\nEnter a username:").capitalize()
    while True:
        if USERNAME.isalpha():
            break
        else:
            print("Please enter only letters")


def clear_terminal():
    """
    Function to clear the terminal after selections
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
    global RANDOM_ROW
    RANDOM_ROW = WORDS.row_values(randrange(1, len(WORDS.col_values(1))))


def get_secret_word():
    """
    Uses index 0 from random row to pull the random word
    """
    global RANDOM_ROW
    return RANDOM_ROW[0].upper()


def get_secret_hint():
    """
    Uses index 1 from random row to pull the random word's hint
    """
    global RANDOM_ROW
    return RANDOM_ROW[1].capitalize()


def play_game():
    """
    Function to play game
    """
    current_player_score = 0
    get_random_row()
    secret_word = get_secret_word()
    hint = get_secret_hint()
    letters_guessed = ""
    # Number of attempts before player fails
    tries = 6
    print(view_hangman(tries))

    for letter in secret_word:
        print("_ ", end="")

    # Loop the game until the player fails, and break when they win
    while tries > 0:
        print('')
        guess = input("\nEnter a letter: \n\n"
                      "For the hint type: hint\n").upper()

        # Validates the guess and then checks if it is in the secret word.
        # If the letter is incorrect, tries increments by 1.
        if guess == "hint".upper():
            print(hint)
        else:
            if validate_guess(guess, letters_guessed):
                if guess in secret_word:
                    print("")
                    print(f"Well Done {USERNAME}! The letter {guess} is "
                          "in the word.")
                    print("")
                    print(view_hangman(tries))
                    print('\n' * 2)
                else:
                    tries -= 1
                    print("")
                    print(f"Sorry {USERNAME},"
                          " the letter {guess} is not in the word.\n")
                    print(f"You have {tries} attempt(s) left.\n")
                    print(view_hangman(tries))
                    print('')

                # Letters guessed variable adds each guess, so the user can see
                # what they have already tried.
                letters_guessed = letters_guessed + guess
                incorrect_letter_count = 0

                # Adds the letter to the word if it correct and prints an
                # underscore if it is incorrect.
                for letter in secret_word:
                    if letter in letters_guessed:
                        print(f"{letter} ", end="")
                    else:
                        print("_ ", end="")
                        incorrect_letter_count += 1

                # Prints letters guessed each time a new letter is guessed.
                print("")
                print(f"\nLetters guessed: {letters_guessed}")

                # If incorrect letter count = 0 after the loop runs, the player
                # has guessed the whole word correctly and the loop breaks.
                if incorrect_letter_count == 0:
                    current_player_score += 1
                    clear_terminal()
                    update_highscores_sheet()
                    print(f"Congratulations {USERNAME} you won!"
                          " The word was {secret_word}")
                    winner_play_again = input("\nWould you like to "
                                              "play again? y/n")
                    if winner_play_again == "y":
                        clear_terminal()
                        play_game()
                    else:
                        clear_terminal()
                        main()
                    break
    # If the incorrect letter count = 6 the player loses.
    else:
        clear_terminal()
        print(f"Sorry {USERNAME} you lose! The word was {secret_word}")
        loser_play_again = input("\nWould you like to play again? / y/n")

        if loser_play_again == "y":
            clear_terminal()
            play_game()
        else:
            clear_terminal()
            main()


def update_highscores_sheet():
    global HIGHSCORES, scores

    if len(scores) > 0:
        keys = [str(eachvalue) for eachvalue in scores[0].keys()]
        values = [str(eachvalue) for eachvalue in scores[0].values()]
        update_results = [
            {'range': 'A1:Z1', 'values': [keys]},
            {'range': 'A2:Z2', 'values': [values]}
        ]
    else:
        scores.append(dict(['Key', 'Value']))
        scores.append(dict(['em', '']))
        update_results = {[scores]}
    print(update_results)
    HIGHSCORES.update(update_results)


def view_hangman(tries):
    """
    The hangman stages to be shown as the number of lives decrease
    """
    stages = [
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |     /|\    |
                              |   |     / \    |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |     /|\    |
                              |   |     /      |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |     /|\    |
                              |   |            |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |     /|     |
                              |   |            |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |      |     |
                              |   |            |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
                              +----------------+
                              |   -------+     |
                              |   |      |     |
                              |   |      0     |
                              |   |            |
                              |   |            |
                              |   |            |
                              |   ----------   |
                              +----------------+""",
        r"""
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


def main():
    """
    Main function to call all functions
    """
    welcome_screen()
    get_username()
    clear_terminal()
    play_game()


if __name__ == '__main__':
    main()
