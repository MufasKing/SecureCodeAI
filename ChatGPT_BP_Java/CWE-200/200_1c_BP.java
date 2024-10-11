import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import org.mindrot.jbcrypt.BCrypt;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    // Secret key for session management
    private static final String SECRET_KEY = "someSecretKey";

    // Login function
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        // Input validation
        if (username == null || username.isEmpty() || password == null || password.isEmpty()) {
            request.setAttribute("errorMessage", "Username or password cannot be empty.");
            request.getRequestDispatcher("login.jsp").forward(request, response);
            return;
        }

        try (Connection conn = DatabaseConnection.getConnection()) {
            // Query database for user
            String query = "SELECT username, password FROM users WHERE username = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, username);

            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                String storedHash = rs.getString("password");

                // Verify password
                if (BCrypt.checkpw(password, storedHash)) {
                    // Successful login, create session
                    HttpSession session = request.getSession();
                    session.setAttribute("username", username);
                    session.setAttribute("secretKey", SECRET_KEY);

                    // Redirect to home page
                    response.sendRedirect("home.jsp");
                } else {
                    // Incorrect password
                    request.setAttribute("errorMessage", "Invalid username or password.");
                    request.getRequestDispatcher("login.jsp").forward(request, response);
                }
            } else {
                // Username doesn't exist
                request.setAttribute("errorMessage", "Invalid username or password.");
                request.getRequestDispatcher("login.jsp").forward(request, response);
            }
        } catch (SQLException e) {
            e.printStackTrace();
            request.setAttribute("errorMessage", "An error occurred. Please try again.");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }
}

// Utility class to hash passwords
public class PasswordUtils {

    // Hash the password
    public static String hashPassword(String password) {
        return BCrypt.hashpw(password, BCrypt.gensalt());
    }

    // Verify the password
    public static boolean checkPassword(String password, String hash) {
        return BCrypt.checkpw(password, hash);
    }
}

// Servlet for logout functionality
@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false); // False if there's no current session

        if (session != null) {
            // Invalidate session
            session.invalidate();
        }

        // Redirect to login page
        response.sendRedirect("login.jsp");
    }
}
