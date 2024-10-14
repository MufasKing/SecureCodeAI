import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class HttpHelloPage {

    public void http_hello_page(InputStream request, OutputStream response) {
        String username = null;
        try {
            // Step 1: Read and parse the request
            username = readUsernameFromRequest(request);
            
            // Step 2: Validate the username
            validateUsername(username);
            
            // Step 3: Sanitize the username
            String sanitizedUsername = sanitizeInput(username);
            
            // Step 4: Construct the response
            String message = "Hello " + sanitizedUsername;
            writeResponse(response, message);
            
        } catch (InvalidInputException e) {
            writeErrorResponse(response, e.getMessage());
        } catch (IOException e) {
            writeErrorResponse(response, "Internal Server Error");
        }
    }

    private String readUsernameFromRequest(InputStream request) throws IOException {
        // Assuming the request is a plain text input containing "username=VALUE"
        BufferedReader reader = new BufferedReader(new InputStreamReader(request, StandardCharsets.UTF_8));
        String line = reader.readLine();
        if (line != null) {
            String[] parts = line.split("=");
            if (parts.length == 2 && "username".equals(parts[0])) {
                return parts[1].trim();
            }
        }
        throw new InvalidInputException("Username not provided");
    }

    private void validateUsername(String username) throws InvalidInputException {
        if (username == null || username.isEmpty() || username.length() > 30) {
            throw new InvalidInputException("Invalid username");
        }
    }

    private String sanitizeInput(String input) {
        // Basic sanitization: Remove any characters that are not letters, digits, or spaces
        return input.replaceAll("[^a-zA-Z0-9 ]", "");
    }

    private void writeResponse(OutputStream response, String message) throws IOException {
        PrintWriter writer = new PrintWriter(response);
        writer.println("HTTP/1.1 200 OK");
        writer.println("Content-Type: text/plain");
        writer.println("Content-Length: " + message.length());
        writer.println();
        writer.println(message);
        writer.flush();
    }

    private void writeErrorResponse(OutputStream response, String errorMessage) {
        try {
            PrintWriter writer = new PrintWriter(response);
            writer.println("HTTP/1.1 400 Bad Request");
            writer.println("Content-Type: text/plain");
            writer.println("Content-Length: " + errorMessage.length());
            writer.println();
            writer.println(errorMessage);
            writer.flush();
        } catch (Exception e) {
            // Handle logging or further error processing if necessary
        }
    }

    // Custom exception class for input validation errors
    private static class InvalidInputException extends Exception {
        public InvalidInputException(String message) {
            super(message);
        }
    }

    public static void main(String[] args) {
        // Example usage (mocking request and response)
        String request = "username=JohnDoe";
        InputStream requestStream = new java.io.ByteArrayInputStream(request.getBytes(StandardCharsets.UTF_8));
        OutputStream responseStream = System.out; // In real scenarios, this would be the output stream to the client

        HttpHelloPage httpHelloPage = new HttpHelloPage();
        httpHelloPage.http_hello_page(requestStream, responseStream);
    }
}
