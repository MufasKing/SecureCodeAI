import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class UrlPingDecorator {

    // Regex pattern for URL validation
    private static final Pattern URL_PATTERN = 
        Pattern.compile("^(https?://)?(www\\.)?[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}(:[0-9]{1,5})?(/.*)?$");

    public static void main(String[] args) {
        String urlToPing = "http://example.com"; // Example URL; replace with actual input as needed
        
        // Validate and sanitize URL
        if (!isValidUrl(urlToPing)) {
            System.out.println("Invalid URL provided.");
            return;
        }

        // Call the ping function with the URL
        String pong = ping(urlToPing);
        System.out.println(pong);
    }

    // URL validation method
    private static boolean isValidUrl(String url) {
        return url != null && URL_PATTERN.matcher(url).matches();
    }

    // Method to ping the URL
    private static String ping(String url) {
        StringBuilder output = new StringBuilder();
        ProcessBuilder processBuilder = new ProcessBuilder("ping", "-c", "4", sanitizeUrl(url)); // For UNIX/Linux
        // For Windows use: ProcessBuilder processBuilder = new ProcessBuilder("ping", "-n", "4", sanitizeUrl(url));

        try {
            Process process = processBuilder.start();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append("\n");
                }
            }

            // Wait for the process to complete and check the exit value
            int exitCode = process.waitFor();
            if (exitCode == 0) {
                return "The URL " + url + " is alive:\n" + output.toString();
            } else {
                return "The URL " + url + " is not alive:\n" + output.toString();
            }
        } catch (IOException e) {
            return "Error executing ping command: " + e.getMessage();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Restore interrupted status
            return "Ping operation was interrupted.";
        }
    }

    // Method to sanitize the URL to avoid command injection
    private static String sanitizeUrl(String url) {
        // In this example, we're just returning the URL as is, since we validate it earlier.
        // Additional sanitization can be performed as needed.
        return url;
    }
}