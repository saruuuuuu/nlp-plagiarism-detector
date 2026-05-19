def add_item(inventory, item, quantity):
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"Added {quantity} of {item} to inventory.")

def remove_item(inventory, item, quantity):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]
        print(f"Removed {quantity} of {item} from inventory.")
    else:
        print(f"Insufficient quantity of {item}.")

def display_inventory(inventory):
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    inventory = {}
    
    while True:
        print("\nInventory Management Menu")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item, quantity)
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            remove_item(inventory, item, quantity)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Exiting inventory management system.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
