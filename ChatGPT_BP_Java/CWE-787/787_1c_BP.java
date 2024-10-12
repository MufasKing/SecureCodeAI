import java.util.Random;

public class RandomFloatToString {
    public static void main(String[] args) {
        // Create a Random object
        Random rand = new Random();
        
        // Generate three random floats
        float randomFloat1 = rand.nextFloat() * 100; // Scale to a range if needed
        float randomFloat2 = rand.nextFloat() * 100;
        float randomFloat3 = rand.nextFloat() * 100;
        
        // Convert the random floats to strings
        String string1 = String.format("%.2f", randomFloat1); // Format to 2 decimal places
        String string2 = String.format("%.2f", randomFloat2);
        String string3 = String.format("%.2f", randomFloat3);
        
        // Print the results
        System.out.println("Random Float 1: " + string1);
        System.out.println("Random Float 2: " + string2);
        System.out.println("Random Float 3: " + string3);
        
        // Secret Module (Example: Concatenating the strings)
        String secretModule = string1 + string2 + string3; // Example operation
        System.out.println("Secret Module Result: " + secretModule);
    }
}
