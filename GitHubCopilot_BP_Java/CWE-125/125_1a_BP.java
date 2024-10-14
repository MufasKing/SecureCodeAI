import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] id_sequence = {10, 20, 30, 40, 50}; // Example array
        int size = id_sequence.length;
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter an index: ");
            int index = Integer.parseInt(scanner.nextLine().trim());

            int result = getValueFromArray(id_sequence, size, index);
            System.exit(result);
        } catch (NumberFormatException e) {
            System.err.println("Invalid input. Please enter a valid integer.");
            System.exit(-1);
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
            System.exit(-1);
        } finally {
            scanner.close();
        }
    }

    public static int getValueFromArray(int[] array, int size, int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        return array[index];
    }
}