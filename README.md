# CodeAlpha_Tasks
This repo consists of a task assigned by CodeAlpha for Python Programming.


# Task 1: Hangman Game 

## Description
This Python script implements a simple command-line Hangman game. The program randomly selects one of five predefined words and provides a hint about the chosen word. The player has 6 attempts to guess the word letter by letter.

## Key Features:
- Random word selection from 5 options
- Hints provided for each word category
- Visual feedback showing correctly guessed letters
- Attempt counter with remaining tries display
- Win/loss condition checking
- ASCII art for game branding

 ## How It Works:
1. Displays a stylized "HANGMAN" banner
2. Randomly selects a word (e.g., "pineapple") 
3. Provides a category hint (e.g., "a fruit")
4. Player guesses letters one at a time
5. System reveals correctly guessed letters
6. Player wins by guessing all letters before 6 incorrect guesses

 ## Code Structure:
- Uses while loops for game progression
- Maintains state with:
  - `guessed_correct` list to track letter positions
  - `wrong` counter for incorrect guesses
  - `tries_left` for remaining attempts
- Provides real-time feedback after each guess



 
