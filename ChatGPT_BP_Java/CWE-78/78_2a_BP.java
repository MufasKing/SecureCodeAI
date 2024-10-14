import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.regex.Pattern;

public class PingDecorator {

    // Regular expression to validate the URL
    private static final String URL_REGEX = "^(http://|https://)?(www\\.)?[a-zA-Z0-9-]+\\.[a-zA-Z]{2,6}(/[a-zA-Z0-9-./?%&=]*)?$";
    private static final Pattern URL_PATTERN = Pattern.compile(URL_REGEX);

    public static void main(String[] args) {
        PingDecorator pingDecorator = new PingDecorator();
        
        // Example usage
        String testUrl = "http://www.example.com";
        String result = pingDecorator.ping(testUrl);
        System.out.println(result);
    }

    // Decorator method
    public String ping(String urlString) {
        // Validate the URL
        if (!isValidURL(urlString)) {
            return "Invalid URL format.";
        }

        String output;
        try {
            // Extract the hostname from the URL
            URL url = new URL(urlString);
            String host = url.getHost();

            // Execute the ping command
            output = executePingCommand(host);
        } catch (MalformedURLException e) {
            return "Malformed URL: " + e.getMessage();
        } catch (IOException e) {
            return "I/O error while executing ping: " + e.getMessage();
        }

        // Return escaped output
        return escapeOutput(output);
    }

    // Validate the URL format
    private boolean isValidURL(String urlString) {
        return URL_PATTERN.matcher(urlString).matches();
    }

    // Execute the ping command
    private String executePingCommand(String host) throws IOException {
        StringBuilder output = new StringBuilder();
        ProcessBuilder processBuilder = new ProcessBuilder("ping", "-c", "4", host); // Use "-c" for Unix/Linux/Mac, use "-n" for Windows
        Process process = processBuilder.start();

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
        }

        return output.toString();
    }

    // Escape output for safety
    private String escapeOutput(String output) {
        // Basic escaping for HTML output
        return output.replace("&", "&amp;")
                     .replace("<", "&lt;")
                     .replace(">", "&gt;")
                     .replace("\"", "&quot;")
                     .replace("'", "&#39;");
    }
}
