import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of subjects: ");
        int subjects = scanner.nextInt();
        double totalMarks = 0;

        for (int i = 1; i <= subjects; i++) {
            System.out.print("Enter marks for subject " + i + ": ");
            totalMarks += scanner.nextDouble();
        }

        double average = totalMarks / subjects;
        System.out.println("Average marks: " + average);

        if (average >= 90) {
            System.out.println("Grade: A");
        } else if (average >= 80) {
            System.out.println("Grade: B");
        } else if (average >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }

        scanner.close();
    }
}
