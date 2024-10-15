import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

class User {
    private String username;
    private String hashedPassword;

    public User(String username, String hashedPassword) {
        this.username = username;
        this.hashedPassword = hashedPassword;
    }

    public String getUsername() {
        return username;
    }

    public String getHashedPassword() {
        return hashedPassword;
    }
}

class LoginService {
    private Map<String, User> users = new HashMap<>();

    public LoginService() {
        // Predefined user for demonstration
        users.put("user1", new User("user1", hashPassword("password123")));
    }

    public boolean validateUser(String username, String password) {
        User user = users.get(username);
        if (user != null) {
            return user.getHashedPassword().equals(hashPassword(password));
        }
        return false;
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}

class SessionManager {
    private Map<String, HttpSession> sessions = new HashMap<>();

    public void createSession(HttpServletRequest request, String username) {
        HttpSession session = request.getSession(true);
        session.setAttribute("username", username);
        sessions.put(session.getId(), session);
    }

    public void invalidateSession(HttpServletRequest request) {
        HttpSession session = request.getSession(false);
        if (session != null) {
            sessions.remove(session.getId());
            session.invalidate();
        }
    }

    public boolean isAuthenticated(HttpServletRequest request) {
        HttpSession session = request.getSession(false);
        return session != null && sessions.containsKey(session.getId());
    }
}

class RateLimiter {
    private Map<String, Integer> attempts = new HashMap<>();
    private static final int MAX_ATTEMPTS = 5;

    public boolean isAllowed(String ip) {
        int attemptCount = attempts.getOrDefault(ip, 0);
        if (attemptCount >= MAX_ATTEMPTS) {
            return false;
        }
        attempts.put(ip, attemptCount + 1);
        return true;
    }

    public void resetAttempts(String ip) {
        attempts.remove(ip);
    }
}

class CSRFTokenManager {
    private Map<String, String> tokens = new HashMap<>();

    public String generateToken(HttpSession session) {
        String token = UUID.randomUUID().toString();
        tokens.put(session.getId(), token);
        return token;
    }

    public boolean validateToken(HttpSession session, String token) {
        return token != null && token.equals(tokens.get(session.getId()));
    }
}

class LoginController {
    private LoginService loginService = new LoginService();
    private SessionManager sessionManager = new SessionManager();
    private RateLimiter rateLimiter = new RateLimiter();
    private CSRFTokenManager csrfTokenManager = new CSRFTokenManager();

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String ip = request.getRemoteAddr();
        if (!rateLimiter.isAllowed(ip)) {
            response.sendError(HttpServletResponse.SC_TOO_MANY_REQUESTS, "Too many login attempts");
            return;
        }

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (username == null || password == null || !username.matches("\\w+") || !password.matches("\\w+")) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        if (loginService.validateUser(username, password)) {
            sessionManager.createSession(request, username);
            rateLimiter.resetAttempts(ip);
            response.setHeader("Location", "/session");
            response.setStatus(HttpServletResponse.SC_FOUND);
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Incorrect username or password");
        }
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        if (sessionManager.isAuthenticated(request)) {
            String csrfToken = csrfTokenManager.generateToken(request.getSession());
            response.setHeader("X-CSRF-Token", csrfToken);
            response.getWriter().write("Welcome to the session page");
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Please log in first");
        }
    }

    public void doLogout(HttpServletRequest request, HttpServletResponse response) throws IOException {
        sessionManager.invalidateSession(request);
        response.setHeader("Location", "/login");
        response.setStatus(HttpServletResponse.SC_FOUND);
    }
}

public class Main {
    public static void main(String[] args) {
        // This is a placeholder for the main method.
        // In a real application, you would set up your web server and route requests to the LoginController.
    }
}