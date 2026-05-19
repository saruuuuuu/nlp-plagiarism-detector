import java.util.Scanner;

public class FibonacciGenerator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of Fibonacci terms to generate: ");
        int terms = scanner.nextInt();

        System.out.println("Fibonacci Sequence:");
        for (int i = 0; i < terms; i++) {
            System.out.print(fibonacci(i) + " ");
        }

        scanner.close();
    }

    public static int fibonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
