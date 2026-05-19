def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("There are paths to the left and right.")

def choose_path():
    choice = input("Which path will you choose? (left/right): ").lower()
    return choice

def encounter(choice):
    if choice == "left":
        print("You encounter a friendly fairy. She grants you a wish!")
    elif choice == "right":
        print("You encounter a hungry wolf. You need to run!")
    else:
        print("Invalid choice. You wander aimlessly.")

def main():
    intro()
    choice = choose_path()
    encounter(choice)

if __name__ == "__main__":
    main()
