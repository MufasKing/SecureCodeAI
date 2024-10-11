public class Main {
    private static final int OFFSET = 1000;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java Main <number>");
            System.exit(1);
        }

        try {
            String input = args[0];
            int value = Integer.parseInt(input);

            // Check for potential overflow/underflow
            if (value > Integer.MAX_VALUE - OFFSET || value < Integer.MIN_VALUE + OFFSET) {
                throw new ArithmeticException("Integer overflow/underflow detected");
            }

            int result = value + OFFSET;
            System.out.println("Result: " + result);
        } catch (NumberFormatException e) {
            System.err.println("Error: Input is not a valid integer.");
            System.exit(1);
        } catch (ArithmeticException e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
            System.exit(1);
        }
    }
}