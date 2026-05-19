import java.util.Scanner;

public class ATMSystem {
    private static double balance = 1000;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nATM Menu");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    deposit(scanner);
                    break;
                case 2:
                    withdraw(scanner);
                    break;
                case 3:
                    checkBalance();
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

    public static void deposit(Scanner scanner) {
        System.out.print("Enter deposit amount: ");
        double amount = scanner.nextDouble();
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    public static void withdraw(Scanner scanner) {
        System.out.print("Enter withdraw amount: ");
        double amount = scanner.nextDouble();
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrew: " + amount);
        } else {
            System.out.println("Insufficient funds.");
        }
    }

    public static void checkBalance() {
        System.out.println("Current balance: " + balance);
    }
}
