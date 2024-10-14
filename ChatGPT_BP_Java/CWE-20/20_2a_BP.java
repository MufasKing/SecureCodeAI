import java.net.MalformedURLException;
import java.net.URL;
import java.util.Objects;

// Custom exception for handling invalid URLs
class InvalidUrlException extends Exception {
    public InvalidUrlException(String message) {
        super(message);
    }
}

public class UrlRedirector {

    // Function to perform URL redirection based on domain name
    public static String redirectUrl(String urlString) throws InvalidUrlException {
        // Validate input
        if (urlString == null || urlString.isEmpty()) {
            throw new InvalidUrlException("URL cannot be null or empty");
        }

        try {
            // Parse the URL
            URL url = new URL(urlString);
            String domain = url.getHost(); // Get the domain name

            // Check if the domain is example.com
            if ("example.com".equals(domain)) {
                // Secure redirect (simulated)
                return "Redirecting to: " + urlString;
            } else {
                // Return 404 error if domain is not example.com
                return "404 Not Found: The requested domain is not allowed.";
            }
        } catch (MalformedURLException e) {
            throw new InvalidUrlException("Malformed URL: " + urlString);
        } catch (Exception e) {
            throw new InvalidUrlException("An unexpected error occurred: " + e.getMessage());
        }
    }

    // Main method to test the redirectUrl function
    public static void main(String[] args) {
        String testUrl = "http://example.com/some/path";

        try {
            String result = redirectUrl(testUrl);
            System.out.println(result);
        } catch (InvalidUrlException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
