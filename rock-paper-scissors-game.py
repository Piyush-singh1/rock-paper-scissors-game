import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("Type 'exit' to stop playing.\n")

    options = ['rock', 'paper', 'scissors']

    while True:
        # Get user's choice
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("Thank you for playing! Goodbye!")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)
        print(f"Computer's choice: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        print()  # Blank line for better readability

# Run the game
play_game()
