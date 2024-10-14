package GitHubCopilot_BP_Java.CWE-89;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/post")
public class Main extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // CSRF Protection
        String csrfToken = request.getParameter("csrfToken");
        HttpSession session = request.getSession();
        String sessionCsrfToken = (String) session.getAttribute("csrfToken");
        if (sessionCsrfToken == null || !sessionCsrfToken.equals(csrfToken)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "CSRF token mismatch");
            return;
        }

        // Input Validation
        String username = request.getParameter("username");
        String message = request.getParameter("message");
        if (username == null || username.isEmpty() || message == null || message.isEmpty()) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        // Insert message into the database
        try {
            insert_user_message_in_db(username, message);
        } catch (SQLException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error");
            return;
        }

        // Secure Redirect
        response.sendRedirect(response.encodeRedirectURL(request.getContextPath() + "/main"));
    }

    private void insert_user_message_in_db(String username, String message) throws SQLException {
        String url = "jdbc:mysql://localhost:3306/yourdatabase";
        String dbUser = "yourusername";
        String dbPassword = "yourpassword";
        try (Connection conn = DriverManager.getConnection(url, dbUser, dbPassword)) {
            String sql = "INSERT INTO messages (username, message) VALUES (?, ?)";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, username);
                stmt.setString(2, message);
                stmt.executeUpdate();
            }
        }
    }
}