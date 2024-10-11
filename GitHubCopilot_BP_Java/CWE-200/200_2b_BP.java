// User.java
public class User {
    private String username;
    private String passwordHash;

    public User(String username, String passwordHash) {
        this.username = username;
        this.passwordHash = passwordHash;
    }

    public String getUsername() {
        return username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }
}

// Database.java
import java.util.HashMap;
import java.util.Map;

public class Database {
    private static Map<String, User> users = new HashMap<>();

    static {
        // Example user
        users.put("user1", new User("user1", BCrypt.hashpw("password", BCrypt.gensalt())));
    }

    public static User getUserByUsername(String username) {
        return users.get(username);
    }
}

// LoginService.java
import org.mindrot.jbcrypt.BCrypt;

public class LoginService {
    private static final int MAX_ATTEMPTS = 5;
    private static Map<String, Integer> loginAttempts = new HashMap<>();

    public static boolean login(String username, String password) {
        User user = Database.getUserByUsername(username);
        if (user == null) {
            return false;
        }

        if (loginAttempts.getOrDefault(username, 0) >= MAX_ATTEMPTS) {
            return false; // Account locked
        }

        if (BCrypt.checkpw(password, user.getPasswordHash())) {
            loginAttempts.put(username, 0); // Reset attempts on successful login
            return true;
        } else {
            loginAttempts.put(username, loginAttempts.getOrDefault(username, 0) + 1);
            return false;
        }
    }
}

// SessionManager.java
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

public class SessionManager {
    public static void createSession(HttpServletRequest request, User user) {
        HttpSession session = request.getSession(true);
        session.setAttribute("user", user);
    }

    public static void invalidateSession(HttpServletRequest request) {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }
    }
}

// LoginController.java
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class LoginController extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (username == null || password == null || !isValidInput(username, password)) {
            response.sendRedirect("login.jsp?error=Invalid input");
            return;
        }

        if (LoginService.login(username, password)) {
            User user = Database.getUserByUsername(username);
            SessionManager.createSession(request, user);
            response.sendRedirect("dashboard.jsp");
        } else {
            response.sendRedirect("login.jsp?error=Invalid username or password");
        }
    }

    private boolean isValidInput(String username, String password) {
        return username.matches("[a-zA-Z0-9_]+") && password.length() >= 8;
    }
}