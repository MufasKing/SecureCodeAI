package GitHubCopilot_BP_Java.CWE-476;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        System.out.flush(); // Prompt flushing

        String input = null;
        try {
            input = scanner.nextLine();
            if (input.length() > 1023) {
                input = input.substring(0, 1023); // Ensure buffer limit
            }
        } catch (Exception e) {
            System.err.println("Error reading input: " + e.getMessage());
        }

        if (input != null) {
            System.out.println("You entered: " + input);
            System.out.println("Number of characters read: " + input.length());
        }
    }
}