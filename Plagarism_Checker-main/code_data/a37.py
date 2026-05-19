import random

def main():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
