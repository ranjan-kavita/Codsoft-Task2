import random

def get_computer_choice():
    """Randomly select between 'rock', 'paper', and 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Get the user's choice and ensure it's valid."""
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user and computer's choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    
    # Get the user's and computer's choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
