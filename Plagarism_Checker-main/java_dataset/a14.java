import java.util.Scanner;

public class SimpleStopwatch {
    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Simple Stopwatch");
        System.out.println("Press Enter to start, and Enter again to stop.");

        scanner.nextLine();
        long startTime = System.currentTimeMillis();

        scanner.nextLine();
        long endTime = System.currentTimeMillis();

        long elapsedTime = (endTime - startTime) / 1000;
        System.out.println("Elapsed time: " + elapsedTime + " seconds");

        scanner.close();
    }
}
