def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Added contact: {name} - {phone}")

def display_contacts(contacts):
    print("Contacts:")
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def main():
    contacts = {}
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(contacts, name, phone)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")

if __name__ == "__main__":
    main()
