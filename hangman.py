"""
Hangman file to hold the different stages of the the hangman as
tries decrease
"""


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
