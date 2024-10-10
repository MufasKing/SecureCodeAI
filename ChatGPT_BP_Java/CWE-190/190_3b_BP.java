import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

public class SalesCalculator {

    // Function to simulate fetching monthly sales
    public static int getMonthlySales(int month) {
        // Logic to fetch monthly sales for the given month (e.g., from a database)
        // For simplicity, we'll return a random number for now.
        SecureRandom random = new SecureRandom();
        return random.nextInt(10000); // Random sales number between 0 and 9999
    }

    // Function to calculate the total sales for the first quarter
    public static int calculateFirstQuarterSales() {
        int sum = 0;
        // Iterate over the first 3 months (0 to 2)
        for (int i = 0; i < 3; i++) {
            int sales = getMonthlySales(i);
            sum += sales; // Add the monthly sales to sum
        }
        return sum;
    }

    // Function to hash the total sales securely using SHA-256
    public static String hashTotalSales(int totalSales) throws NoSuchAlgorithmException {
        // Convert the totalSales integer to bytes
        byte[] totalSalesBytes = Integer.toString(totalSales).getBytes();
        
        // Create MessageDigest instance for SHA-256
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = md.digest(totalSalesBytes);
        
        // Convert the hash bytes to a hexadecimal string
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            hexString.append(String.format("%02x", b));
        }
        
        return hexString.toString();
    }

    public static void main(String[] args) {
        try {
            // Calculate the total sales for the first quarter
            int totalSales = calculateFirstQuarterSales();
            System.out.println("Total Sales for the First Quarter: " + totalSales);
            
            // Hash the total sales securely
            String hashedSales = hashTotalSales(totalSales);
            System.out.println("Hashed Total Sales: " + hashedSales);
            
        } catch (NoSuchAlgorithmException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
