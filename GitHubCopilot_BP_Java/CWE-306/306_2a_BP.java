import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

class User {
    private String username;
    private String passwordHash;
    private String role;

    public User(String username, String passwordHash, String role) {
        this.username = username;
        this.passwordHash = passwordHash;
        this.role = role;
    }

    public String getUsername() {
        return username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public String getRole() {
        return role;
    }
}

class UserManager {
    private Map<String, User> users = new HashMap<>();

    public void addUser(String username, String password, String role) {
        String passwordHash = hashPassword(password);
        users.put(username, new User(username, passwordHash, role));
    }

    public User getUser(String username) {
        return users.get(username);
    }

    private String hashPassword(String password) {
        // Implement a secure password hashing mechanism
        return Integer.toHexString(password.hashCode());
    }
}

class SessionManager {
    private Map<String, String> sessions = new HashMap<>();

    public String createSession(String username) {
        String sessionId = UUID.randomUUID().toString();
        sessions.put(sessionId, username);
        return sessionId;
    }

    public String getUsername(String sessionId) {
        return sessions.get(sessionId);
    }

    public void invalidateSession(String sessionId) {
        sessions.remove(sessionId);
    }
}

class AuthService {
    private UserManager userManager;
    private SessionManager sessionManager;

    public AuthService(UserManager userManager, SessionManager sessionManager) {
        this.userManager = userManager;
        this.sessionManager = sessionManager;
    }

    public String login(String username, String password) {
        User user = userManager.getUser(username);
        if (user != null && user.getPasswordHash().equals(hashPassword(password))) {
            return sessionManager.createSession(username);
        }
        return null;
    }

    public void logout(String sessionId) {
        sessionManager.invalidateSession(sessionId);
    }

    public String authorize(String sessionId) {
        String username = sessionManager.getUsername(sessionId);
        if (username == null) {
            return "redirect:/login";
        }
        User user = userManager.getUser(username);
        if (user.getRole().equals("admin")) {
            return "redirect:/admin";
        } else {
            return "redirect:/user";
        }
    }

    private String hashPassword(String password) {
        // Implement a secure password hashing mechanism
        return Integer.toHexString(password.hashCode());
    }
}

public class Main {
    public static void main(String[] args) {
        UserManager userManager = new UserManager();
        SessionManager sessionManager = new SessionManager();
        AuthService authService = new AuthService(userManager, sessionManager);

        // Add users
        userManager.addUser("admin", "adminpass", "admin");
        userManager.addUser("user", "userpass", "user");

        // Simulate login
        String sessionId = authService.login("admin", "adminpass");
        if (sessionId != null) {
            System.out.println(authService.authorize(sessionId)); // Should redirect to /admin
        }

        sessionId = authService.login("user", "userpass");
        if (sessionId != null) {
            System.out.println(authService.authorize(sessionId)); // Should redirect to /user
        }

        sessionId = authService.login("unknown", "wrongpass");
        if (sessionId == null) {
            System.out.println("redirect:/login"); // Should redirect to /login
        }
    }
}