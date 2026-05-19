import java.util.ArrayList;
import java.util.Scanner;

public class ToDoList {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> toDoList = new ArrayList<>();
        int choice;

        do {
            System.out.println("\nTo-Do List Menu");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. View Tasks");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String task = scanner.nextLine();
                    toDoList.add(task);
                    System.out.println("Task added.");
                    break;
                case 2:
                    System.out.print("Enter task index to remove: ");
                    int index = scanner.nextInt();
                    if (index >= 0 && index < toDoList.size()) {
                        toDoList.remove(index);
                        System.out.println("Task removed.");
                    } else {
                        System.out.println("Invalid task index.");
                    }
                    break;
                case 3:
                    System.out.println("\nTo-Do List:");
                    for (int i = 0; i < toDoList.size(); i++) {
                        System.out.println((i + 1) + ". " + toDoList.get(i));
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);

        scanner.close();
    }
}
