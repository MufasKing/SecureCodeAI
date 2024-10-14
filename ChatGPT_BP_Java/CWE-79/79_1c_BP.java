import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class HttpHelloPage {

    // Function to escape HTML characters
    public static String escape_html(String input) {
        if (input == null) {
            return "";
        }
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&apos;");
    }

    // Main function to handle the HTTP request
    public static void http_hello_page(BufferedReader request, BufferedWriter response) {
        try {
            // Read the username from the request
            String line = request.readLine();
            String username = extractUsername(line); // Extract username from the request
            
            // Validate the username
            if (username == null || username.isEmpty()) {
                writeResponse(response, "Username cannot be empty.");
                return;
            }

            // Escape the username to prevent HTML injection
            String safeUsername = escape_html(username);

            // Construct the response
            String responseMessage = "hello " + safeUsername;

            // Write the response
            writeResponse(response, responseMessage);
        } catch (IOException e) {
            writeResponse(response, "Internal Server Error: " + e.getMessage());
        }
    }

    // Function to extract username from the request
    private static String extractUsername(String requestLine) {
        if (requestLine != null && requestLine.startsWith("GET /hello?username=")) {
            String[] parts = requestLine.split("=");
            if (parts.length > 1) {
                return parts[1];
            }
        }
        return null;
    }

    // Function to write the response to the client
    private static void writeResponse(BufferedWriter response, String message) {
        try {
            response.write("HTTP/1.1 200 OK\r\n");
            response.write("Content-Type: text/plain\r\n");
            response.write("\r\n");
            response.write(message);
            response.flush();
        } catch (IOException e) {
            System.err.println("Error writing response: " + e.getMessage());
        }
    }

    // Example usage
    public static void main(String[] args) {
        // Example code to simulate request handling (not part of the main functionality)
        String simulatedRequest = "GET /hello?username=John%20Doe"; // URL encoded
        Path requestPath = Paths.get("request.txt");
        Path responsePath = Paths.get("response.txt");

        try (BufferedReader request = Files.newBufferedReader(requestPath);
             BufferedWriter response = Files.newBufferedWriter(responsePath)) {

            // Simulating writing a request to file (normally handled by the server)
            try (PrintWriter writer = new PrintWriter(new FileWriter(requestPath.toFile()))) {
                writer.println(simulatedRequest);
            }

            // Call the HTTP hello page function
            http_hello_page(request, response);
        } catch (IOException e) {
            System.err.println("Error handling request: " + e.getMessage());
        }
    }
}
