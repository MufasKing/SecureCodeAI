import java.security.SecureRandom;
import java.math.BigInteger;

public class SecureRandomIntegers {

    public static void main(String[] args) {
        // Cryptographically secure random number generation
        SecureRandom secureRandom = new SecureRandom();

        // Generate three random integers larger than 1000
        int a = 1001 + secureRandom.nextInt(Integer.MAX_VALUE - 1001);
        int b = 1001 + secureRandom.nextInt(Integer.MAX_VALUE - 1001);
        int c = 1001 + secureRandom.nextInt(Integer.MAX_VALUE - 1001);

        // Print the three integers
        System.out.println(String.format("a : %d", a));
        System.out.println(String.format("b : %d", b));
        System.out.println(String.format("c : %d", c));

        // Sum the three integers and print the result
        int sum = a + b + c;
        System.out.println(String.format("sum: %d", sum));

        // Add the three integers using BigInteger to handle overflow
        BigInteger sum2 = BigInteger.valueOf(a).add(BigInteger.valueOf(b)).add(BigInteger.valueOf(c));
        System.out.println(String.format("sum2: %d", sum2));
    }
}
