def string_manipulations(string):
    print(f"Original String: {string}")
    print(f"Reversed String: {string[::-1]}")
    print(f"Uppercase: {string.upper()}")
    print(f"Lowercase: {string.lower()}")
    print(f"Length: {len(string)}")

def main():
    while True:
        string = input("Enter a string to manipulate (or 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the string manipulation tool.")
            break
        string_manipulations(string)

if __name__ == "__main__":
    main()
