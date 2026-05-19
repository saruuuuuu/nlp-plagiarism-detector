def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print("Task not found.")

def display_tasks(tasks):
    print("Your To-Do List:")
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

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
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
