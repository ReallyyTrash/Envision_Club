# Number Guessing Game

A simple Python number guessing game where the computer picks a random number between 1 and 100, and the player tries to guess it with hints.

## Features

- **Interactive Menu System**: Easy-to-use menu with multiple options
- **Smart Hints**: Get "Too High" or "Too Low" feedback after each guess
- **Statistics Tracking**: Keep track of games played, best score, and average attempts
- **Error Handling**: Robust input validation and error messages
- **Encouragement System**: Motivational messages during gameplay
- **Quit Anytime**: Type 'quit' during any guess to exit gracefully

## How to Play

1. Run the game: `python main.py`
2. Choose "Play New Game" from the menu
3. Enter your guess (1-100) when prompted
4. Follow the hints until you guess correctly
5. View your statistics or play again!

## Game Options

1. **Play New Game** - Start a new guessing game
2. **View Statistics** - See your gaming performance
3. **Show Instructions** - Display game rules
4. **Quit Game** - Exit the application

## Requirements

- Python 3.x
- No additional libraries required (uses only built-in modules)

## Code Structure

The game is built with clean, modular functions:

- `display_welcome()` - Shows game instructions
- `get_valid_guess()` - Handles input validation
- `play_single_game()` - Core game logic
- `display_stats()` - Shows player statistics
- `main_menu()` - Menu system navigation
- `main()` - Main game loop

## Example Gameplay

```
==================================================
WELCOME TO THE NUMBER GUESSING GAME!
==================================================
I'm thinking of a number between 1 and 100.
Try to guess it in as few attempts as possible!
I'll give you hints: 'Too High' or 'Too Low'
==================================================

==============================
GAME MENU
==============================
1. Play New Game
2. View Statistics
3. Show Instructions
4. Quit Game
==============================
Choose an option (1-4): 1

I've picked a number! Let's see if you can guess it.
Tip: Type 'quit' anytime to exit the game.

Enter your guess (1-100): 50
Too High! Try a lower number.

Enter your guess (1-100): 25
Too Low! Try a higher number.

Enter your guess (1-100): 37
CONGRATULATIONS! You guessed it!
The number was 37
You did it in 3 attempts!
```

## License

This project is open source and available under the MIT License.