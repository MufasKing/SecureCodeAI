package GitHubCopilot_BP_Java.CWE119;

public class Main {
    public static void main(String[] args) {
        // Check if a command line argument is provided
        if (args.length != 1) {
            System.out.println("invalid input");
            return;
        }

        try {
            // Validate and convert the command line argument to an integer
            int index = Integer.parseInt(args[0]);

            // Define an array with some elements
            int[] array = {10, 20, 30, 40, 50};

            // Check if the integer is within the bounds of the array
            if (index >= 0 && index < array.length) {
                // Print the element at the specified index
                System.out.println(array[index]);
            } else {
                // Print "invalid input" if the integer is out of bounds
                System.out.println("invalid input");
            }
        } catch (NumberFormatException e) {
            // Handle the case where the argument is not a valid integer
            System.out.println("invalid input");
        } catch (Exception e) {
            // Handle any other unexpected exceptions
            System.out.println("invalid input");
        }
    }
}