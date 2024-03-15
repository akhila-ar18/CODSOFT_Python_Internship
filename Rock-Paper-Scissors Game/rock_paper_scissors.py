import random

# Getting the user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter 'r' for rock , 'p' for paper, or 's' for scissors: ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'r' for rock , 'p' for paper, or 's' for scissors.")

# Fetching computer's random choice
def get_computer_choice():
    return random.choice(['r', 'p', 's'])

# Determining the winner based on the user's choice & computer's random choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        return 'user'
    else:
        return 'computer'

# Displaying the result based on the user's choice & computer's random choice
def display_result(user_choice, computer_choice, winner):
    print(f"User's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!!")
    elif winner == 'user':
        print("Congratulations :)  You win!!")
    else:
        print("Sorry :(  You lose!!")

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("*************************************************************")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nUser Score: {user_score}  Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (1/0): ").lower()
        if play_again != '1':
            print("Thanks for playing!!")
            break
        print("*************************************************************")

if __name__ == "__main__":
    main()
