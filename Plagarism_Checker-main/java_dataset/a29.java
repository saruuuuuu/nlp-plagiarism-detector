import java.util.Scanner;
import java.util.HashMap;

public class CharacterFrequency {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : input.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        System.out.println("Character frequencies:");
        for (char key : frequencyMap.keySet()) {
            System.out.println(key + ": " + frequencyMap.get(key));
        }

        scanner.close();
    }
}
