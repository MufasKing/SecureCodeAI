import java.security.SecureRandom;

public class RandomDifference {
    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();

        // Generate random integers between 10 and 1000
        int num1 = 10 + random.nextInt(991);
        int num2 = 10 + random.nextInt(991);

        // Calculate the absolute difference
        int difference = Math.abs(num1 - num2);

        // Print the results
        System.out.printf("First number: %d%nSecond number: %d%nDifference: %d%n", num1, num2, difference);
    }
}