import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of your password: "))
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")
    else:
        print("Failed to generate a password.")

if __name__ == "__main__":
    main()
