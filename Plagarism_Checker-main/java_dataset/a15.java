import java.util.Scanner;

public class PrimeFactorization {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number to find its prime factors: ");
        int num = scanner.nextInt();

        System.out.print("Prime factors of " + num + " are: ");
        primeFactors(num);

        scanner.close();
    }

    public static void primeFactors(int num) {
        for (int i = 2; i <= Math.sqrt(num); i++) {
            while (num % i == 0) {
                System.out.print(i + " ");
                num /= i;
            }
        }
        if (num > 1) {
            System.out.print(num);
        }
        System.out.println();
    }
}
