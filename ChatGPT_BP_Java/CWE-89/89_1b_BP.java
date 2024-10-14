import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.*;
import java.util.regex.Pattern;

public class UnsubscribeServlet extends HttpServlet {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdb"; // Update with your DB URL
    private static final String DB_USER = "yourUser"; // Update with your DB User
    private static final String DB_PASSWORD = "yourPassword"; // Update with your DB Password
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String email = request.getParameter("email");

        // Input Validation
        if (email == null || email.isEmpty() || !EMAIL_PATTERN.matcher(email).matches()) {
            response.getWriter().write("Invalid email format.");
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            return;
        }

        // Using try-with-resources for automatic resource management
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement checkEmailStmt = connection.prepareStatement("SELECT COUNT(*) FROM users WHERE email = ?");
             PreparedStatement deleteUserStmt = connection.prepareStatement("DELETE FROM users WHERE email = ?")) {

            // Check if the email is in the database
            checkEmailStmt.setString(1, email);
            ResultSet rs = checkEmailStmt.executeQuery();

            if (rs.next() && rs.getInt(1) > 0) {
                // Email found, proceed to delete
                deleteUserStmt.setString(1, email);
                int rowsAffected = deleteUserStmt.executeUpdate();

                if (rowsAffected > 0) {
                    response.getWriter().write("You have been unsubscribed successfully.");
                } else {
                    response.getWriter().write("Error occurred while unsubscribing.");
                    response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
                }
            } else {
                // Email not found
                response.getWriter().write("You are not subscribed.");
                response.setStatus(HttpServletResponse.SC_NOT_FOUND);
            }
        } catch (SQLException e) {
            // Handle SQL exceptions
            e.printStackTrace();
            response.getWriter().write("Database error: " + e.getMessage());
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
    }
}
