def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do List is empty.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
