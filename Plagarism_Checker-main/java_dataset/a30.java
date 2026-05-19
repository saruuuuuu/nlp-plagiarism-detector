import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nTemperature Converter");
            System.out.println("1. Celsius to Fahrenheit");
            System.out.println("2. Fahrenheit to Celsius");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter temperature in Celsius: ");
                    double celsius = scanner.nextDouble();
                    System.out.println(celsius + " Celsius = " + celsiusToFahrenheit(celsius) + " Fahrenheit");
                    break;
                case 2:
                    System.out.print("Enter temperature in Fahrenheit: ");
                    double fahrenheit = scanner.nextDouble();
                    System.out.println(fahrenheit + " Fahrenheit = " + fahrenheitToCelsius(fahrenheit) + " Celsius");
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

    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }
}
