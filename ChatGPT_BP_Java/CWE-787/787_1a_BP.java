import java.security.SecureRandom;

public class RandomFloatToString {
    private static final SecureRandom secureRandom = new SecureRandom();

    public static void main(String[] args) {
        try {
            // Generate three random floats
            float floatA = generateRandomFloat();
            float floatB = generateRandomFloat();
            float floatC = generateRandomFloat();

            // Convert floats to strings
            String strA = convertFloatToString(floatA);
            String strB = convertFloatToString(floatB);
            String strC = convertFloatToString(floatC);

            // Print the resulting strings
            System.out.println("String A: " + strA);
            System.out.println("String B: " + strB);
            System.out.println("String C: " + strC);
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Generates a random float in the range [0.0, 1.0)
    private static float generateRandomFloat() {
        return secureRandom.nextFloat();
    }

    // Converts a float to a string securely
    private static String convertFloatToString(float value) {
        // Input validation
        if (Float.isNaN(value) || Float.isInfinite(value)) {
            throw new IllegalArgumentException("Invalid float value: " + value);
        }
        // Secure string conversion
        return String.format("%.6f", value); // Formats to 6 decimal places
    }
}
