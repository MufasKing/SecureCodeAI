public class SecureAtoi {
    
    // Custom atoi function for secure conversion of string to integer
    public static int atoi(String str) throws NumberFormatException {
        if (str == null || str.isEmpty()) {
            throw new NumberFormatException("Input string is null or empty.");
        }
        int result = 0;
        boolean isNegative = false;
        int i = 0;
        
        // Check for negative sign
        if (str.charAt(0) == '-') {
            isNegative = true;
            i++;
        }

        // Convert each character to digit and build the integer
        for (; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c < '0' || c > '9') {
                throw new NumberFormatException("Invalid character found: " + c);
            }
            result = result * 10 + (c - '0');

            // Check for integer overflow
            if (result < 0) {
                throw new NumberFormatException("Integer overflow occurred.");
            }
        }
        return isNegative ? -result : result;
    }
    
    public static void main(String[] args) {
        // Perform basic input validation
        if (args.length < 2) {
            System.err.println("Usage: java SecureAtoi <index> <other arguments>");
            System.exit(1);
        }

        try {
            // Parse the index safely using atoi
            int index = atoi(args[1]);
            
            // Validate the index within range
            if (index < 2 || index >= args.length) {
                System.err.println("Error: Index out of range.");
                System.exit(1);
            }

            // Print the argument at the specified index
            String result = args[index];
            System.out.println(result);
        } catch (NumberFormatException e) {
            // Handle parsing errors
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            // Catch any other unexpected errors
            System.err.println("Unexpected error: " + e.getMessage());
            System.exit(1);
        }
        
        // Exit program successfully
        System.exit(0);
    }
}
