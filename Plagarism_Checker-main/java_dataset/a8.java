import java.util.ArrayList;
import java.util.Scanner;

class Student {
    private String name;
    private int id;
    private double grade;

    public Student(int id, String name, double grade) {
        this.id = id;
        this.name = name;
        this.grade = grade;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getGrade() {
        return grade;
    }

    public void display() {
        System.out.println("ID: " + id + " | Name: " + name + " | Grade: " + grade);
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
            System.out.println("2. View All Students");
            System.out.println("3. Search Student by ID");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    viewAllStudents();
                    break;
                case 3:
                    searchStudentById();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);
    }

    private static void addStudent() {
        System.out.print("Enter student ID: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter student name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student grade: ");
        double grade = scanner.nextDouble();
        
        Student student = new Student(id, name, grade);
        students.add(student);
        System.out.println("Student added successfully.");
    }

    private static void viewAllStudents() {
        System.out.println("\nList of all students:");
        for (Student student : students) {
            student.display();
        }
    }

    private static void searchStudentById() {
        System.out.print("Enter student ID to search: ");
        int id = scanner.nextInt();
        boolean found = false;
        for (Student student : students) {
            if (student.getId() == id) {
                student.display();
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Student with ID " + id + " not found.");
        }
    }
}
