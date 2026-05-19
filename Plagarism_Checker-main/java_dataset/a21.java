import java.util.Scanner;

public class InventorySystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] products = {"Product1", "Product2", "Product3"};
        int[] stock = {10, 20, 15};

        int choice;
        do {
            System.out.println("\nInventory Menu");
            System.out.println("1. View Inventory");
            System.out.println("2. Update Stock");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    viewInventory(products, stock);
                    break;
                case 2:
                    updateStock(scanner, products, stock);
                    break;
                case 3:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 3);

        scanner.close();
    }

    public static void viewInventory(String[] products, int[] stock) {
        System.out.println("\nCurrent Inventory:");
        for (int i = 0; i < products.length; i++) {
            System.out.println(products[i] + ": " + stock[i]);
        }
    }

    public static void updateStock(Scanner scanner, String[] products, int[] stock) {
        System.out.print("Enter product index (0-2): ");
        int index = scanner.nextInt();
        System.out.print("Enter quantity to add: ");
        int quantity = scanner.nextInt();

        if (index >= 0 && index < products.length) {
            stock[index] += quantity;
            System.out.println("Updated stock for " + products[index] + ": " + stock[index]);
        } else {
            System.out.println("Invalid product index.");
        }
    }
}
