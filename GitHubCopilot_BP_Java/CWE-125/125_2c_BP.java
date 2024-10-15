package GitHubCopilot_BP_Java.CWE_125;

import java.util.Scanner;

public class Main {
    private static final int[] id_sequence = {10, 20, 30, 40, 50};

    public static void main(String[] args) {
        System.out.println("Value at index: " + getValueAtIndex());
    }

    public static int getValueAtIndex() {
        Scanner scanner = new Scanner(System.in);
        int index = -1;

        try {
            System.out.print("Enter an index value: ");
            if (scanner.hasNextInt()) {
                index = scanner.nextInt();
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                return 0;
            }

            if (index >= 0 && index < id_sequence.length) {
                return id_sequence[index];
            } else {
                System.out.println("Index out of bounds.");
                return 0;
            }
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            return 0;
        } finally {
            scanner.close();
        }
    }
}