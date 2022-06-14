# Hangman

[View live project](https://hangman-ed.herokuapp.com/)

![Responsive image](/hangman_readme_images/responsive_image.png)

# Table of contents
1. [User Experience](##user-experience(ux))
2. [Flowchart](##flowchart)
3. [Existing Features](existing-features)

## User Experience(UX)

* First Time User Goals:

  1. As a first time user, I want to have fun playing the game and feel nostalgia from having played the original game.
  2. As a first time user, I want to be able to understand clearly how to navigate through the game.
  3. As a first time user, I want to be able to play numerous times without coming across the same word.

* Returning Visitor Goals:

  1. As a returning visitor, I want to be able to play the game over and over without having repeated words.
  2. As a returning visitor, I want to be able to navigate through the game the same as the first time I played.
  3. As a returning visitor, I want to be familiar with the game and use hints to help me solve the secret words.

* Frequent User Goals:

  1. As a frequent user, I want to be able to continously play the game without coming across any words I have encountered before.

## Flowchart

![Flowchart](/hangman_readme_images/hangman-flowchart.png)

## Existing Features

- __Welcome screen__

An imported figlet library (pyfiglet) is used to create the text banner from standard characters. This large banner is clear and lets the user know what game they are playing. The image of the hangman (also made from characters), is instantly recognisable as the well know hangman game. The user is prompted to input their name on this screen.

![Welcome screen](/hangman_readme_images/homepage.png)

- __Username error message__

The username imput validates that the user has only used letters in there name, if false, prompts the user to only use letters.

![Username error message](/hangman_readme_images/only_letters_username.png)

- __Initial game screen__

The user is presented with the frame of hangman minus the man, signalling the start of the game and for a letter to be input, alternatively the user can type the word hint into the terminal to reveal a clue from the secret word.

![Initial game screen](/hangman_readme_images/initial_game_screen.png)

- __Error letters only__

If the user is to type a number or character into the terminal the validator function will print an error message letting the user know that only letters are valid.

![Error letters only](/hangman_readme_images/error_letters_only.png)

- __Error single letter only__

Similar to the error letters only, if the user is to type a number of characters into the terminal, the validator function will print an error message letting the player know that only one letter can be input at a time.

![Error single letter only](/hangman_readme_images/error_multiple_letter.png)

- __Correct letter__

If the player inputs a correct letter, it will be inserted into the underscored line in as many places as the letter exists, the user will be informed by name that the guess was correct. This letter will also be placed in the letters guessed line so they can keep track of what has already been guessed.

![Correct letter](/hangman_readme_images/correct_letter.png)

- __Incorrect letter__

If the letter input is incorrect the printed message informs the user that the letter is not in the word and that a life has been lost. This letter will then be printed into the letters guessed line to allow the user to see all the letters they have guessed. For each incorrect letter and life lost the hangman will gain a body part.ß

![Incorrect letter](/hangman_readme_images/incorrect_letter.png)

- __Hint__

The player can request a hint by typing hint into the guess a letter box. The validator has an exception which allows the word (even though more than character) to be input, when this is done , the definition of the word is shown to the user. The hint can be displayed at an point throughout the game.

![Hint](/hangman_readme_images/show_hint.png)

- __Player wins__

If the player guesses the word before the number of tries i.e number of incorrect answers equals 6, congratulations (player) is printed along with the option to play again. If the user types 'y' the game function is ran and a new secret word is selected. If the players types any other character they are taken back to the welcome screen.

![Player wins](/hangman_readme_images/winner.png)

- __Player loses__

If the player runs out of tries they lose and the secret word is printed. The option to play again is presented if the user types 'y' the game function is ran and a new secret word is selected. If the players types any other character they are taken back to the welcome screen.

![Player loses](/hangman_readme_images/loser.png)





