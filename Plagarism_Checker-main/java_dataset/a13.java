import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double num1, num2;
        int choice;

        do {
            System.out.println("\nSimple Calculator");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            if (choice != 5) {
                System.out.print("Enter first number: ");
                num1 = scanner.nextDouble();
                System.out.print("Enter second number: ");
                num2 = scanner.nextDouble();
            }

            switch (choice) {
                case 1:
                    System.out.println("Result: " + (num1 + num2));
                    break;
                case 2:
                    System.out.println("Result: " + (num1 - num2));
                    break;
                case 3:
                    System.out.println("Result: " + (num1 * num2));
                    break;
                case 4:
                    if (num2 != 0) {
                        System.out.println("Result: " + (num1 / num2));
                    } else {
                        System.out.println("Error: Cannot divide by zero.");
                    }
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 5);

        scanner.close();
    }
}
