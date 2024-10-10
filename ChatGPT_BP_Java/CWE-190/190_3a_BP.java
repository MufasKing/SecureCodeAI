import java.security.SecureRandom;

public class SalesReport {
    
    // SecureRandom for generating random sales figures
    private static SecureRandom secureRandom = new SecureRandom();
    
    // Simulated "secrets" for future extension where you might retrieve data from external systems
    private static String API_KEY = "your-api-key"; // Example secret (not used here but placeholder for Secrets module)
    
    public static void main(String[] args) {
        double[] monthlySales = new double[12];
        double[] quarterlySales = new double[4]; // Array for quarterly totals
        
        // Populate monthly sales with random values
        for (int month = 0; month < 12; month++) {
            monthlySales[month] = getMonthlySales(); // Separation of concerns: getMonthlySales is a dedicated method
        }

        // Calculate and print quarterly sales
        calculateQuarterlySales(monthlySales, quarterlySales);

        // Print results
        printQuarterlyResults(quarterlySales);
    }
    
    // Function to get monthly sales (returns a random number between 0 and 100000)
    private static double getMonthlySales() {
        // Input validation could go here if needed for other params in real-life situations
        return secureRandom.nextInt(100001); // Returns a random number between 0 and 100000
    }

    // Separation of concerns: Calculate quarterly sales from monthly sales
    private static void calculateQuarterlySales(double[] monthlySales, double[] quarterlySales) {
        for (int quarter = 0; quarter < 4; quarter++) {
            quarterlySales[quarter] = monthlySales[quarter * 3] + monthlySales[quarter * 3 + 1] + monthlySales[quarter * 3 + 2];
        }
    }

    // Separation of concerns: Print quarterly results
    private static void printQuarterlyResults(double[] quarterlySales) {
        for (int quarter = 0; quarter < 4; quarter++) {
            String result = String.format("Sales for Q%d: %.2f", quarter + 1, quarterlySales[quarter]);
            System.out.println(result);
        }
    }

    // Future function to safely retrieve secrets (Placeholder for Secrets module)
    // In real-world applications, this would retrieve the secret securely
    private static String getApiKey() {
        // This could handle encrypted storage retrieval
        return API_KEY;
    }
}
