import java.security.SecureRandom;

public class RandomDifference {
    public static void main(String[] args) {
        // Create a SecureRandom object
        SecureRandom secureRandom = new SecureRandom();

        // Generate two random integers between 10 and 1000
        int num1 = 10 + secureRandom.nextInt(991);  // 991 = 1000 - 10 + 1
        int num2 = 10 + secureRandom.nextInt(991);

        // Calculate the absolute difference
        int difference = Math.abs(num1 - num2);

        // Print the results using formatted string (f-string equivalent in Java)
        System.out.printf("First number: %d%nSecond number: %d%nDifference: %d%n", num1, num2, difference);
    }
}
