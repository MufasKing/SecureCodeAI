import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

@WebServlet("/post")
public class MessageServlet extends HttpServlet {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase"; // Change to your database URL
    private static final String DB_USER = "yourusername"; // Change to your database username
    private static final String DB_PASSWORD = "yourpassword"; // Change to your database password

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String message = request.getParameter("message");

        // Input Validation
        if (username == null || message == null || username.isEmpty() || message.isEmpty()) {
            response.sendRedirect("error.jsp"); // Redirect to an error page
            return;
        }

        // Input Sanitization
        username = sanitizeInput(username);
        message = sanitizeInput(message);

        // Secure Database Interaction
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement stmt = conn.prepareStatement("INSERT INTO messages (username, message) VALUES (?, ?)")) {
            stmt.setString(1, username);
            stmt.setString(2, message);
            stmt.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("error.jsp"); // Redirect to an error page
            return;
        }

        // URL Redirection to main page
        response.sendRedirect("main.jsp");
    }

    private String sanitizeInput(String input) {
        // Basic sanitization to prevent XSS
        return input.replaceAll("[<>]", "");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Message> messages = new ArrayList<>();

        // Fetch messages from the database
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement stmt = conn.prepareStatement("SELECT username, message FROM messages");
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                String username = rs.getString("username");
                String message = rs.getString("message");
                messages.add(new Message(username, message));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // HTML Rendering
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><head><title>Messages</title></head><body>");
        out.println("<h1>Messages</h1>");
        for (Message msg : messages) {
            out.println("<p><strong>" + msg.getUsername() + ":</strong> " + msg.getMessage() + "</p>");
        }
        out.println("</body></html>");
    }

    private static class Message {
        private final String username;
        private final String message;

        public Message(String username, String message) {
            this.username = username;
            this.message = message;
        }

        public String getUsername() {
            return username;
        }

        public String getMessage() {
            return message;
        }
    }
}
