def add_note(notes, note):
    notes.append(note)
    print("Note added!")

def display_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        print("Your Notes:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. {note}")

def main():
    notes = []
    
    while True:
        print("\nNote-Taking Menu")
        print("1. Add Note")
        print("2. Display Notes")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            note = input("Enter your note: ")
            add_note(notes, note)
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            print("Exiting the note-taking application.")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")

if __name__ == "__main__":
    main()
