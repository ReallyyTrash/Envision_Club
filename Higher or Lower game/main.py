import random


def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 50)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!")
    print("I'll give you hints: 'Too High' or 'Too Low'")
    print("=" * 50)


def get_valid_guess():
    """Get a valid number guess from the player with error handling."""
    while True:
        try:
            guess = input("\nEnter your guess (1-100): ").strip()
            
            # Check for quit command
            if guess.lower() in ['quit', 'exit', 'q']:
                return None
                
            guess_num = int(guess)
            
            if 1 <= guess_num <= 100:
                return guess_num
            else:
                print("Please enter a number between 1 and 100!")
                
        except ValueError:
            print("Invalid input! Please enter a valid number or 'quit' to exit.")


def play_single_game():
    """Play one round of the guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("\nI've picked a number! Let's see if you can guess it.")
    print("Tip: Type 'quit' anytime to exit the game.")
    
    while True:
        guess = get_valid_guess()
        
        # Player wants to quit
        if guess is None:
            print(f"\nThanks for playing! The number was {secret_number}.")
            return None 
            
        attempts += 1
        
        if guess == secret_number:
            print(f"\nCONGRATULATIONS! You guessed it!")
            print(f"The number was {secret_number}")
            print(f"You did it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            return attempts
            
        elif guess < secret_number:
            print(f"Too Low! Try a higher number.")
            
        else:
            print(f"Too High! Try a lower number.")
        
        # Give encouragement based on attempts
        if attempts == 5:
            print("Keep going! You're getting warmer!")
        elif attempts == 10:
            print("Hmm, this is tricky! Don't give up!")


def display_stats(games_played, total_attempts, best_score):
    """Display player statistics."""
    if games_played == 0:
        print("\nNo games played yet!")
        return
        
    print(f"\nYOUR GAME STATISTICS:")
    print(f"Games Played: {games_played}")
    print(f"Best Score: {best_score} attempts")
    print(f"Average Attempts: {total_attempts / games_played:.1f}")


def main_menu():
    """Display main menu and handle user choice."""
    print("\n" + "=" * 30)
    print("GAME MENU")
    print("=" * 30)
    print("1. Play New Game")
    print("2. View Statistics") 
    print("3. Show Instructions")
    print("4. Quit Game")
    print("=" * 30)
    
    while True:
        choice = input("Choose an option (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice! Please enter 1, 2, 3, or 4.")


def main():
    """Main game loop with menu system."""
    games_played = 0
    total_attempts = 0
    best_score = float('inf')
    
    display_welcome()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            # Play new game
            attempts = play_single_game()
            
            if attempts is not None:  # Game completed (not quit)
                games_played += 1
                total_attempts += attempts
                
                if attempts < best_score:
                    best_score = attempts
                    print(f"NEW BEST SCORE! Only {attempts} attempts!")
                
                # Ask if they want to play again
                while True:
                    play_again = input("\nPlay another game? (y/n): ").strip().lower()
                    if play_again in ['y', 'yes']:
                        break
                    elif play_again in ['n', 'no']:
                        break
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                
                if play_again in ['n', 'no']:
                    continue  # Go back to main menu
                else:
                    continue  # This will show menu again, but user can choose to play
                    
        elif choice == '2':
            # View statistics
            display_stats(games_played, total_attempts, best_score if best_score != float('inf') else 0)
            
        elif choice == '3':
            # Show instructions
            display_welcome()
            
        elif choice == '4':
            # Quit game
            print("\n" + "=" * 40)
            print("Thanks for playing!")
            if games_played > 0:
                print(f"You played {games_played} game{'s' if games_played != 1 else ''}!")
                if best_score != float('inf'):
                    print(f"Your best score was {best_score} attempts!")
            print("See you next time!")
            print("=" * 40)
            break


if __name__ == "__main__":
    main()