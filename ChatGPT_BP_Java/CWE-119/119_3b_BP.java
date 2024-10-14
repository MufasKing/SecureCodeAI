public class AtoiProgram {

    public static void main(String[] args) {
        // Input Validation: Check if enough arguments are provided
        if (args.length < 2) {
            System.err.println("Error: No integer argument provided.");
            System.out.println("Usage: java AtoiProgram <number>");
            return;
        }

        // argv[0] is the name of the program
        System.out.println("Program name: " + args[0]);

        // Process the command-line argument at argv[1]
        String input = args[1];

        try {
            // Input Sanitization: Remove leading/trailing spaces
            input = input.trim();

            // Error Handling: Validate the input is a valid integer
            if (!isValidInteger(input)) {
                throw new IllegalArgumentException("Invalid integer format: " + input);
            }

            // Robust Integer Conversion: Convert the string to an integer safely
            int result = safeAtoi(input);

            // Output the result
            System.out.println("Converted integer: " + result);

        } catch (NumberFormatException e) {
            // Handle number format issues (e.g., overflow/underflow)
            System.err.println("Error: Integer overflow or underflow for input: " + input);
        } catch (IllegalArgumentException e) {
            // Handle invalid input
            System.err.println(e.getMessage());
        }
    }

    /**
     * Checks if a string is a valid integer format.
     * 
     * @param str the input string
     * @return true if the string is a valid integer, false otherwise
     */
    public static boolean isValidInteger(String str) {
        // Regular expression to validate a valid integer (with optional leading sign)
        return str.matches("[-+]?\\d+");
    }

    /**
     * Safely converts a string to an integer, throwing an exception if overflow/underflow occurs.
     * 
     * @param str the input string
     * @return the converted integer value
     * @throws NumberFormatException if the integer is out of bounds
     */
    public static int safeAtoi(String str) throws NumberFormatException {
        // Parse the string as a long to check for overflow/underflow
        long value = Long.parseLong(str);

        // Check for overflow and underflow
        if (value > Integer.MAX_VALUE || value < Integer.MIN_VALUE) {
            throw new NumberFormatException("Integer overflow/underflow for input: " + str);
        }

        // Safe to cast to int
        return (int) value;
    }
}
