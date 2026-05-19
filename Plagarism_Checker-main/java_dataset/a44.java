import java.util.ArrayList;
import java.util.Scanner;

class Student {
    String name;
    int age;
    char grade;

    public Student(String name, int age, char grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Age: " + age + ", Grade: " + grade;
    }
}

public class StudentManagementSystem {
    private static ArrayList<Student> students = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            System.out.println("\nStudent Management System");
            System.out.println("1. Add Student");
            System.out.println("2. View Students");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    viewStudents();
                    break;
                case 3:
                    updateStudent();
                    break;
                case 4:
                    deleteStudent();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 5);
    }

    private static void addStudent() {
        System.out.print("Enter student's name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student's age: ");
        int age = scanner.nextInt();
        System.out.print("Enter student's grade: ");
        char grade = scanner.next().charAt(0);
        scanner.nextLine(); // Consume newline character

        students.add(new Student(name, age, grade));
        System.out.println("Student added successfully.");
    }

    private static void viewStudents() {
        if (students.isEmpty()) {
            System.out.println("No students available.");
        } else {
            System.out.println("\nStudent Records:");
            for (int i = 0; i < students.size(); i++) {
                System.out.println((i + 1) + ". " + students.get(i));
            }
        }
    }

    private static void updateStudent() {
        System.out.print("Enter the student index to update: ");
        int index = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        if (index < 1 || index > students.size()) {
            System.out.println("Invalid student index.");
        } else {
            Student student = students.get(index - 1);
            System.out.print("Enter new name (" + student.name + "): ");
            String name = scanner.nextLine();
            System.out.print("Enter new age (" + student.age + "): ");
            int age = scanner.nextInt();
            System.out.print("Enter new grade (" + student.grade + "): ");
            char grade = scanner.next().charAt(0);
            scanner.nextLine(); // Consume newline character

            student.name = name;
            student.age = age;
            student.grade = grade;

            System.out.println("Student record updated successfully.");
        }
    }

    private static void deleteStudent() {
        System.out.print("Enter the student index to delete: ");
        int index = scanner.nextInt();

        if (index < 1 || index > students.size()) {
            System.out.println("Invalid student index.");
        } else {
            students.remove(index - 1);
            System.out.println("Student removed successfully.");
        }
    }
}
