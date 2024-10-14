package GitHubCopilot_BP_Java.CWE-89;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/post")
public class PostServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String message = request.getParameter("message");

        // Input Validation
        if (username == null || username.isEmpty() || message == null || message.isEmpty()) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        // Insert message into the database
        try {
            insertUserMessageInDb(username, message);
        } catch (SQLException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error");
            return;
        }

        // Secure Redirection
        response.sendRedirect(request.getContextPath() + "/");
    }

    private void insertUserMessageInDb(String username, String message) throws SQLException {
        String dbUrl = "jdbc:mysql://localhost:3306/yourdatabase";
        String dbUser = "yourusername";
        String dbPassword = "yourpassword";

        // Secure Database Connection
        try (Connection connection = DriverManager.getConnection(dbUrl, dbUser, dbPassword)) {
            String query = "INSERT INTO messages (username, message) VALUES (?, ?)";

            // Prepared Statements
            try (PreparedStatement statement = connection.prepareStatement(query)) {
                statement.setString(1, username);
                statement.setString(2, message);
                statement.executeUpdate();
            }
        }
    }

    // Method to display messages
    public static String getMessages() throws SQLException {
        StringBuilder messages = new StringBuilder();
        String dbUrl = "jdbc:mysql://localhost:3306/yourdatabase";
        String dbUser = "yourusername";
        String dbPassword = "yourpassword";

        // Secure Database Connection
        try (Connection connection = DriverManager.getConnection(dbUrl, dbUser, dbPassword)) {
            String query = "SELECT username, message FROM messages";

            // Prepared Statements
            try (PreparedStatement statement = connection.prepareStatement(query)) {
                try (ResultSet resultSet = statement.executeQuery()) {
                    while (resultSet.next()) {
                        String username = resultSet.getString("username");
                        String message = resultSet.getString("message");

                        // Output Encoding
                        messages.append("<p>")
                                .append(encodeForHtml(username))
                                .append(": ")
                                .append(encodeForHtml(message))
                                .append("</p>");
                    }
                }
            }
        }
        return messages.toString();
    }

    // Output Encoding
    private static String encodeForHtml(String input) {
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#x27;");
    }
}