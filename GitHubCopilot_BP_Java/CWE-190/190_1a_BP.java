public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Please provide exactly one integer argument.");
            System.exit(1);
        }

        try {
            String input = args[0];
            int number = Integer.parseInt(input);

            // Check for overflow/underflow before adding 1000
            if (number > Integer.MAX_VALUE - 1000 || number < Integer.MIN_VALUE + 1000) {
                throw new ArithmeticException("Integer overflow/underflow detected.");
            }

            int result = number + 1000;
            System.out.println("Result: " + result);
        } catch (NumberFormatException e) {
            System.err.println("Invalid input. Please provide a valid integer.");
        } catch (ArithmeticException e) {
            System.err.println(e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}