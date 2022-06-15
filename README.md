# Hangman

[View live project](https://hangman-ed.herokuapp.com/)

![Responsive image](/hangman_readme_images/responsive_image.png)

# Table of contents
1. [User experience](#user-experience(ux))
2. [Flowchart](#flowchart)
3. [Existing features](#existing-features)
    - [Welcome screen](#welcome-screen)
    - [Username error message](#username-error-message)
    - [Initial game screen](#initial-game-screen)
    - [Error letters only](#error-letters-only)
    - [Error single letter only](#error-single-letter-only)
    - [Correct letter](#correct-letter)
    - [Incorrect letter](#incorrect-letter)
    - [Hint](#hint)
    - [Player wins](#player-wins)
    - [Player loses](#player-loses)
4. [Future features](#future-features)
5. [Technology used](#technology-used)
    - [Languages](#languages)
    - [Frameworks, libraries and programs used](#frameworks-libraries-and-programs-used)
6. [Testing](#testing)
    - [Validator testing](#validator-testing)
    - [User experience testing](#testing-user-experience)

# User Experience(UX)

## User Stories

### - __First Time User Goals:__

  1. As a first time user, I want to have fun playing the game and feel nostalgia from having played the original game.
  2. As a first time user, I want to be able to understand clearly how to navigate through the game.
  3. As a first time user, I want to be able to play numerous times without coming across the same word.

### -__Returning Visitor Goals:__

  1. As a returning visitor, I want to be able to play the game over and over without having repeated words.
  2. As a returning visitor, I want to be able to navigate through the game the same as the first time I played.
  3. As a returning visitor, I want to be familiar with the game and use hints to help me solve the secret words.

### -__Frequent User Goals__

  1. As a frequent user, I want to be able to continously play the game without coming across any words I have encountered before.

# Flowchart

![Flowchart](/hangman_readme_images/hangman-flowchart.png)

# Existing Features

### - __Welcome screen__

An imported figlet library (pyfiglet) is used to create the text banner from standard characters. This large banner is clear and lets the user know what game they are playing. The image of the hangman (also made from characters), is instantly recognisable as the well know hangman game. The user is prompted to input their name on this screen.

![Welcome screen](/hangman_readme_images/homepage.png)

### - __Username error message__

The username input validates that the user has only used letters in there name, if false, prompts the user to only use letters.

![Username error message](/hangman_readme_images/only_letters_username.png)

### - __Initial game screen__

The user is presented with the frame of hangman minus the man, signalling the start of the game and for a letter to be input, alternatively the user can type the word hint into the terminal to reveal a clue from the secret word.

![Initial game screen](/hangman_readme_images/initial_game_screen.png)

### - __Error letters only__

If the user is to type a number or character into the terminal the validator function will print an error message letting the user know that only letters are valid.

![Error letters only](/hangman_readme_images/error_letters_only.png)

### - __Error single letter only__

Similar to the error letters only, if the user is to type a number of characters into the terminal, the validator function will print an error message letting the player know that only one letter can be input at a time.

![Error single letter only](/hangman_readme_images/error_multiple_letter.png)

### - __Correct letter__

If the player inputs a correct letter, it will be inserted into the underscored line in as many places as the letter exists, the user will be informed by name that the guess was correct. This letter will also be placed in the letters guessed line so they can keep track of what has already been guessed.

![Correct letter](/hangman_readme_images/correct_letter.png)

### - __Incorrect letter__

If the letter input is incorrect the printed message informs the user that the letter is not in the word and that a life has been lost. This letter will then be printed into the letters guessed line to allow the user to see all the letters they have guessed. For each incorrect letter and life lost the hangman will gain a body part.ß

![Incorrect letter](/hangman_readme_images/incorrect_letter.png)

### - __Hint__

The player can request a hint by typing hint into the guess a letter box. The validator has an exception which allows the word (even though more than character) to be input, when this is done , the definition of the word is shown to the user. The hint can be displayed at an point throughout the game.

![Hint](/hangman_readme_images/show_hint.png)

### - __Player wins__

If the player guesses the word before the number of tries i.e number of incorrect answers equals 6, congratulations (player) is printed along with the option to play again. If the user types 'y' the game function is ran and a new secret word is selected. If the players types any other character they are taken back to the welcome screen.

![Player wins](/hangman_readme_images/winner.png)

### - __Player loses__

If the player runs out of tries they lose and the secret word is printed. The option to play again is presented if the user types 'y' the game function is ran and a new secret word is selected. If the players types any other character they are taken back to the welcome screen.

![Player loses](/hangman_readme_images/loser.png)


# Future features

- An option to add a player two to the game i.e playing against the computer, to give the player more of a challenge.
- A leaderboard so the user can see where they are ranking against other users.
- A difiiculty levels option, so the player has choice perhaps of length of word they want to guess.
- A life removed when a hint is requested.


# Technology used

## Languages

- [Python](https://www.python.org/)


## Frameworks, libraries and programs used

- [Github](https://github.com/)
  - Used to save project code from Git.

- [Lucid](https://lucid.co/)
  - USed to build the flow chart to plan the hangman game.

- [Heroku](https://www.heroku.com)
  - Platform used to buidl, run and operate game.

- [Google Sheets](https://docs.google.com/spreadsheets)
  - Linked via API to retrieve secret words and hints.


# Testing

## Validator testing

- Checked that the random hints givem correspond to the random secret word pulled from the google sheet.
- If the player enters a character other than a letter that the validator returns an error message to the user.
- Checked the code in the github terminal and once deployed to Heroku, had no errors and worked as planned.
- When passed through the [PEP8 Validator for Python](http://pep8online.com), no errors where returned.

![PEP8 Validator for Python](/hangman_readme_images/Validator_result.png)

## User experience testing

### - __First Time User Goals:__

  1. As a first time user, I want to have fun playing the game and feel nostalgia from having played the original game.
      - The game closely resembles the orignal hangman game that most know and enjoy, it is almost identical aside from the automation.

  2. As a first time user, I want to be able to understand clearly how to navigate through the game.
      - The user is greeted with the welcome screen and a clear instruction to input their name, as the users proceeds to play the game the instructions and comments returned are clear     and concise making it easy to understand.

  3. As a first time user, I want to be able to play numerous times without coming across the same word.
      - The google sheet the random words are pulled from contains over 300 possible words and hints meaning they are unlikely to come across the same word twice.

### -__Returning Visitor Goals:__

  1. As a returning visitor, I want to be able to play the game over and over without having repeated words.
      - The words pulled from the google sheet are randomised so it is unlikey the user will come across a word they have encountered before.

  2. As a returning visitor, I want to be able to navigate through the game the same as the first time I played.
      - The game is a simple structure and the user will play without changes to the layout, the same as the first time they played

  3. As a returning visitor, I want to be familiar with the game and use hints to help me solve the secret words.
      - The google sheet the randoms words are pulled from also contains the corresponding hint to the word. The user can type 'hint' in the terminal at any time during game play to receive the hint.

### -__Frequent User Goals__

  1. As a frequent user, I want to be able to continously play the game without coming across any words I have encountered before.
      - The database the random secret word is pulled from has over 300 words which are randomly pulled to the game, therefore the user would have to play for a long time to come across the same word, and if they did the characters they input would most likely be in a different order so the user wouldn't recognise it as the same word.


