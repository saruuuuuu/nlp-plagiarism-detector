import random

def get_random_word():
    words = ["python", "java", "swift", "javascript", "ruby"]
    return random.choice(words)

def display_board(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print(display_board(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}'.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    main()
