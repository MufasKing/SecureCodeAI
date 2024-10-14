import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class MessageServlet extends HttpServlet {
    
    // Method to handle POST request
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // Validate session and CSRF token
        HttpSession session = request.getSession(false);
        if (session == null || !isCsrfTokenValid(request)) {
            response.sendRedirect("error.jsp"); // Redirect on error
            return;
        }

        // Retrieve user input
        String username = request.getParameter("username");
        String message = request.getParameter("message");

        // Input validation
        if (isInputValid(username, message)) {
            // Output encoding
            String safeUsername = encodeOutput(username);
            String safeMessage = encodeOutput(message);
            
            // Insert message into database
            try {
                insertUserMessageInDb(safeUsername, safeMessage);
            } catch (SQLException e) {
                e.printStackTrace(); // Log error (consider logging to a file)
                response.sendRedirect("error.jsp"); // Redirect on error
                return;
            }
            
            // Redirect to main page
            response.sendRedirect("main.jsp");
        } else {
            response.sendRedirect("error.jsp"); // Redirect on validation failure
        }
    }

    private boolean isInputValid(String username, String message) {
        return username != null && !username.trim().isEmpty() && 
               message != null && !message.trim().isEmpty() &&
               username.length() <= 50 && message.length() <= 500; // Example length validation
    }

    private String encodeOutput(String input) {
        // Basic output encoding (implement a library or a more robust encoding mechanism as needed)
        return input.replaceAll("&", "&amp;")
                    .replaceAll("<", "&lt;")
                    .replaceAll(">", "&gt;")
                    .replaceAll("\"", "&quot;")
                    .replaceAll("'", "&#x27;");
    }

    private void insertUserMessageInDb(String username, String message) throws SQLException {
        Connection connection = null; // Obtain connection from your connection pool
        PreparedStatement preparedStatement = null;
        
        try {
            String sql = "INSERT INTO messages (username, message) VALUES (?, ?)";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, message);
            preparedStatement.executeUpdate();
        } finally {
            if (preparedStatement != null) preparedStatement.close();
            if (connection != null) connection.close(); // Ensure connection is closed
        }
    }

    private boolean isCsrfTokenValid(HttpServletRequest request) {
        // Implement your CSRF token validation logic here
        return true; // Placeholder, implement your logic
    }
}
