import java.security.SecureRandom;

public class RandomIntegers {
    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();

        // Generate three random integers larger than 1000
        int a = 1000 + secureRandom.nextInt(Integer.MAX_VALUE - 1000);
        int b = 1000 + secureRandom.nextInt(Integer.MAX_VALUE - 1000);
        int c = 1000 + secureRandom.nextInt(Integer.MAX_VALUE - 1000);

        // Print the three integers
        System.out.printf("a : %d%n", a);
        System.out.printf("b : %d%n", b);
        System.out.printf("c : %d%n", c);

        // Calculate the sum of the three integers and print the result
        int sum = a + b + c;
        System.out.printf("sum: %d%n", sum);

        // Calculate the sum using a long and print the result
        long sum2 = (long) a + (long) b + (long) c;
        System.out.printf("sum2: %d%n", sum2);
    }
}