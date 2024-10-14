import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class SimpleHttpServer {
    
    private static final int PORT = 8080;

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server is listening on port " + PORT);
            while (true) {
                Socket socket = serverSocket.accept();
                handleRequest(socket);
            }
        } catch (IOException e) {
            System.err.println("Server exception: " + e.getMessage());
        }
    }

    private static void handleRequest(Socket socket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true)) {
             
            String requestLine = in.readLine();
            if (requestLine == null || !requestLine.startsWith("POST /hello")) {
                sendErrorResponse(out, 400, "Bad Request");
                return;
            }

            // Read headers and request body
            String line;
            while (!(line = in.readLine()).isEmpty()) {
                // Handle headers if necessary
            }

            StringBuilder requestBody = new StringBuilder();
            String bodyLine;
            while ((bodyLine = in.readLine()) != null) {
                requestBody.append(bodyLine);
            }

            String username = sanitizeInput(requestBody.toString());

            // Validate username
            if (!isValidUsername(username)) {
                sendErrorResponse(out, 400, "Invalid Username");
                return;
            }

            String responseBody = constructResponse(username);
            sendResponse(out, responseBody);
        } catch (IOException e) {
            System.err.println("Request handling error: " + e.getMessage());
            sendErrorResponse(out, 500, "Internal Server Error");
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                System.err.println("Error closing socket: " + e.getMessage());
            }
        }
    }

    private static String sanitizeInput(String input) {
        return input.replaceAll("[<>]", ""); // Basic HTML sanitization
    }

    private static boolean isValidUsername(String username) {
        return username != null && !username.trim().isEmpty() && username.length() <= 20;
    }

    private static String constructResponse(String username) {
        return "<html><body><h1>Hello, " + username + "!</h1></body></html>";
    }

    private static void sendResponse(PrintWriter out, String responseBody) {
        out.println("HTTP/1.1 200 OK");
        out.println("Content-Type: text/html");
        out.println("Content-Length: " + responseBody.length());
        out.println();
        out.print(responseBody);
        out.flush();
    }

    private static void sendErrorResponse(PrintWriter out, int statusCode, String message) {
        out.println("HTTP/1.1 " + statusCode + " " + message);
        out.println("Content-Type: text/plain");
        out.println("Content-Length: " + message.length());
        out.println();
        out.print(message);
        out.flush();
    }
}
