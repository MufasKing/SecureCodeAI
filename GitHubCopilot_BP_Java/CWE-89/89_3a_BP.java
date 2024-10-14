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

@WebServlet("/postMessage")
public class Main extends HttpServlet {
    
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String message = request.getParameter("message");

        // Input Validation
        if (username == null || username.isEmpty() || message == null || message.isEmpty()) {
            response.sendRedirect("errorPage.jsp");
            return;
        }

        // Input Sanitization
        username = sanitizeInput(username);
        message = sanitizeInput(message);

        // Insert message into the database
        insert_user_message_in_db(username, message);

        // Redirect to the main page
        response.sendRedirect("mainPage.jsp");
    }

    private String sanitizeInput(String input) {
        return input.replaceAll("[^a-zA-Z0-9\\s]", "");
    }

    private void insert_user_message_in_db(String username, String message) {
        String url = "jdbc:mysql://localhost:3306/yourDatabase";
        String user = "yourUsername";
        String password = "yourPassword";

        String query = "INSERT INTO messages (username, message) VALUES (?, ?)";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, username);
            stmt.setString(2, message);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        try {
            displayMessages(response);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void displayMessages(HttpServletResponse response) throws SQLException, IOException {
        String url = "jdbc:mysql://localhost:3306/yourDatabase";
        String user = "yourUsername";
        String password = "yourPassword";

        String query = "SELECT username, message FROM messages";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {

            StringBuilder htmlOutput = new StringBuilder("<html><body>");
            while (rs.next()) {
                String username = rs.getString("username");
                String message = rs.getString("message");
                htmlOutput.append("<p><strong>").append(username).append(":</strong> ").append(message).append("</p>");
            }
            htmlOutput.append("</body></html>");
            response.getWriter().write(htmlOutput.toString());
        }
    }
}