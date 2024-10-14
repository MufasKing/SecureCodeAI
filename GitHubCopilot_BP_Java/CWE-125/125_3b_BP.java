package GitHubCopilot_BP_Java.CWE-125;

import java.util.Scanner;

public class Main {
    private int[] array;

    public Main(int[] array) {
        this.array = array;
    }

    public int getValueAtIndex(int index) {
        if (index < 0 || index >= array.length) {
            return -1;
        }
        return array[index];
    }

    public static void main(String[] args) {
        int[] array = {10, 20, 30, 40, 50}; // Example array
        Main mainInstance = new Main(array);
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter an index: ");
        try {
            String input = scanner.nextLine();
            int index = Integer.parseInt(input.trim());

            int value = mainInstance.getValueAtIndex(index);
            if (value == -1) {
                System.out.println("Index out of bounds.");
            } else {
                System.out.println("Value at index " + index + ": " + value);
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        } finally {
            scanner.close();
        }
    }
}