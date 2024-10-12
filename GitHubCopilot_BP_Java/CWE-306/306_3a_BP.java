import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.util.regex.Pattern;
import java.util.logging.Logger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

class User {
    private String username;
    private String email;
    private String hashedPassword;

    public User(String username, String email, String hashedPassword) {
        this.username = username;
        this.email = email;
        this.hashedPassword = hashedPassword;
    }

    public boolean validatePassword(String password) {
        return SecurityService.validatePassword(password, this.hashedPassword);
    }

    public void changeEmail(String newEmail) {
        this.email = newEmail;
    }

    public String getEmail() {
        return email;
    }
}

class AuthService {
    public static boolean login(String username, String password) {
        // Dummy user for demonstration
        User user = new User("user", "user@example.com", SecurityService.hashPassword("password"));
        if (user.validatePassword(password)) {
            HttpSession session = getSession();
            session.setAttribute("user", user);
            return true;
        }
        return false;
    }

    public static boolean isLoggedIn() {
        HttpSession session = getSession();
        return session.getAttribute("user") != null;
    }

    public static User getCurrentUser() {
        HttpSession session = getSession();
        return (User) session.getAttribute("user");
    }

    private static HttpSession getSession() {
        // Placeholder for session retrieval logic
        return null;
    }
}

class EmailService {
    public static boolean changeEmail(User user, String oldEmail, String newEmail, String password) {
        if (!user.getEmail().equals(oldEmail)) {
            return false;
        }
        if (!user.validatePassword(password)) {
            return false;
        }
        if (oldEmail.equals(newEmail)) {
            return false;
        }
        user.changeEmail(newEmail);
        return true;
    }
}

class SecurityService {
    private static final Logger logger = Logger.getLogger(SecurityService.class.getName());

    public static String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            return Base64.getEncoder().encodeToString(hash);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static boolean validatePassword(String password, String hashedPassword) {
        return hashPassword(password).equals(hashedPassword);
    }

    public static void rateLimit() {
        // Implement rate limiting logic
    }

    public static void logSecurityEvent(String event) {
        logger.info(event);
    }
}

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (AuthService.login(username, password)) {
            response.sendRedirect("dashboard.jsp");
        } else {
            response.sendRedirect("login.jsp?error=Invalid credentials");
        }
    }
}

@WebServlet("/change-email")
public class ChangeEmailServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        if (!AuthService.isLoggedIn()) {
            response.sendRedirect("login.jsp");
            return;
        }

        User user = AuthService.getCurrentUser();
        String oldEmail = request.getParameter("oldEmail");
        String newEmail = request.getParameter("newEmail");
        String password = request.getParameter("password");

        if (EmailService.changeEmail(user, oldEmail, newEmail, password)) {
            response.sendRedirect("profile.jsp?success=Email changed successfully");
        } else {
            response.sendRedirect("change-email.jsp?error=Failed to change email");
        }
    }
}