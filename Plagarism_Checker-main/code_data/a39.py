import random

def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
        if choice in ["Rock", "Paper", "Scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "Draw":
            print("It's a draw!")
        else:
            print(f"{winner} wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
