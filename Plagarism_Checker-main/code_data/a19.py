def add_student(grades, name, grade):
    grades[name] = grade
    print(f"Student {name} added with grade {grade}.")

def remove_student(grades, name):
    if name in grades:
        del grades[name]
        print(f"Student {name} removed.")
    else:
        print(f"Student {name} not found.")

def display_grades(grades):
    if grades:
        print("Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    grades = {}
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Grades")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(grades, name, grade)
        elif choice == '2':
            name = input("Enter student name to remove: ")
            remove_student(grades, name)
        elif choice == '3':
            display_grades(grades)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select from 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
