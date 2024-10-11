import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.validation.constraints.NotNull;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

// Import SSL (for HTTPS)
import javax.net.ssl.HttpsURLConnection;

// CSRF token protection library
import java.util.UUID;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Initialize database connection
    private static SessionFactory factory;

    @Override
    public void init() throws ServletException {
        try {
            factory = new Configuration().configure().buildSessionFactory();
        } catch (Exception ex) {
            throw new ServletException("Hibernate session initialization failed.", ex);
        }
    }

    // Validate user input
    private boolean validateInput(@NotNull String username, @NotNull String password) {
        return username != null && !username.trim().isEmpty() && password != null && !password.trim().isEmpty();
    }

    // Hash password with SHA-256
    private String hashPassword(String password) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(password.getBytes());
        byte[] digest = md.digest();
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    // Login function to check user in the database
    private boolean checkLogin(String username, String password) {
        Connection connection = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;
        try {
            // Get hashed password
            String hashedPassword = hashPassword(password);

            // SQLAlchemy-like session management using JDBC
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "password");
            String query = "SELECT * FROM users WHERE username = ? AND password = ?";
            stmt = connection.prepareStatement(query);
            stmt.setString(1, username);
            stmt.setString(2, hashedPassword);
            rs = stmt.executeQuery();

            return rs.next(); // true if a match is found
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (connection != null) connection.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        HttpSession session = request.getSession();
        
        // Input validation
        if (!validateInput(username, password)) {
            response.sendRedirect("login.html");
            return;
        }

        // CSRF Protection: Get CSRF token from the session
        String csrfToken = (String) session.getAttribute("csrfToken");
        String token = request.getParameter("csrfToken");

        if (csrfToken == null || !csrfToken.equals(token)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "Invalid CSRF token");
            return;
        }

        // Check login
        if (checkLogin(username, password)) {
            // Login successful, create session and redirect to home page
            session.setAttribute("username", username);
            response.sendRedirect("home.html");
        } else {
            // Login failed, redirect back to login page
            response.sendRedirect("login.html");
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Generate a new CSRF token for each request
        HttpSession session = request.getSession();
        String csrfToken = UUID.randomUUID().toString();
        session.setAttribute("csrfToken", csrfToken);

        // Redirect to login page
        response.sendRedirect("login.html");
    }

    @Override
    public void destroy() {
        if (factory != null) {
            factory.close();
        }
    }
}
