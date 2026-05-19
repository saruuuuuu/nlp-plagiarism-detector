def is_palindrome(string):
    return string == string[::-1]

def main():
    print("Welcome to the Palindrome Checker!")
    
    while True:
        string = input("Enter a string to check if it's a palindrome (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the palindrome checker.")
            break
        
        if is_palindrome(string):
            print(f"{string} is a palindrome.")
        else:
            print(f"{string} is not a palindrome.")

if __name__ == "__main__":
    main()
