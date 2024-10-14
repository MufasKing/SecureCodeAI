import java.security.SecureRandom;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();

        // Generate three random floats
        float randomFloat1 = secureRandom.nextFloat();
        float randomFloat2 = secureRandom.nextFloat();
        float randomFloat3 = secureRandom.nextFloat();

        // Convert floats to strings
        Optional<String> str_a = convertFloatToString(randomFloat1);
        Optional<String> str_b = convertFloatToString(randomFloat2);
        Optional<String> str_c = convertFloatToString(randomFloat3);

        // Print the results
        str_a.ifPresentOrElse(
            value -> System.out.println("str_a: " + value),
            () -> System.out.println("Error converting randomFloat1 to string")
        );
        str_b.ifPresentOrElse(
            value -> System.out.println("str_b: " + value),
            () -> System.out.println("Error converting randomFloat2 to string")
        );
        str_c.ifPresentOrElse(
            value -> System.out.println("str_c: " + value),
            () -> System.out.println("Error converting randomFloat3 to string")
        );
    }

    private static Optional<String> convertFloatToString(float value) {
        try {
            // Input validation
            if (Float.isNaN(value) || Float.isInfinite(value)) {
                throw new IllegalArgumentException("Invalid float value");
            }
            // Secure string conversion
            return Optional.of(Float.toString(value));
        } catch (Exception e) {
            // Error handling
            System.err.println("Error during float to string conversion: " + e.getMessage());
            return Optional.empty();
        }
    }
}