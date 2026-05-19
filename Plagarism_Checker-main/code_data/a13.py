def add_contact(contacts, name, number):
    contacts[name] = number
    print(f"Contact {name} added successfully.")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts(contacts):
    if contacts:
        print("Current contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts available.")

def main():
    contacts = {}
    while True:
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(contacts, name, number)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            remove_contact(contacts, name)
        elif choice == '3':
            display_contacts(contacts)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
