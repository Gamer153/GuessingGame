import java.io.File;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    private static Map<String, Object> options = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    private static int inputValidInt(String prompt) {
        int input = -1530251052;
        while(input == -1530251052) {
            try {
                System.out.print(prompt);
                input = Integer.valueOf(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Please input a valid number!");
            }
        }
        return input;
    }

    public static void main(String[] args) throws Exception {
        int number = 0;
        File optsFile = new File("options.dat");
        if (!optsFile.exists()) {
            Files.writeString(optsFile.toPath(), "lower=1\nupper=1000");
        }
        Files.readAllLines(optsFile.toPath()).forEach((line) -> {
            String[] splitLine = line.split("=");
            if (Arrays.asList("lower", "upper").contains(splitLine[0]))
                options.put(splitLine[0], Integer.valueOf(splitLine[1]));
            else options.put(splitLine[0], splitLine[1]);
        });
        final int upper = (int) options.get("upper");
        final int lower = (int) options.get("lower");
        while (number == 0) {
            number = new Random().nextInt(lower + upper) + 1 - lower;
        }
        int input = 0;
        while (input != number) {
            input = inputValidInt("Guess a number between " + String.valueOf(lower) + " and " + String.valueOf(upper) + ": ");
            if (input < number) System.out.println("Your guess is too small.");
            if (input > number) System.out.println("Your guess is too high.");
        }
        System.out.println("You guessed right!");
    }
}