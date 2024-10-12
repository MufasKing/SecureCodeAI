import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

class User {
    private String username;
    private String email;
    private String hashedPassword;

    public User(String username, String email, String password) {
        this.username = username;
        this.email = email;
        this.hashedPassword = hashPassword(password);
    }

    public String getEmail() {
        return email;
    }

    public boolean verifyPassword(String password) {
        return hashedPassword.equals(hashPassword(password));
    }

    public void changeEmail(String newEmail) {
        this.email = newEmail;
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

class LoginSystem {
    private Map<String, User> users = new HashMap<>();
    private User loggedInUser = null;
    private String sessionToken = null;
    private int loginAttempts = 0;

    public void registerUser(String username, String email, String password) {
        users.put(username, new User(username, email, password));
    }

    public boolean login(String username, String password) {
        rateLimit();
        User user = users.get(username);
        if (user != null && user.verifyPassword(password)) {
            loggedInUser = user;
            sessionToken = generateSessionToken();
            return true;
        }
        return false;
    }

    public void logout() {
        loggedInUser = null;
        sessionToken = null;
    }

    public boolean changeEmail(String oldEmail, String password, String newEmail) {
        if (loggedInUser != null && loggedInUser.getEmail().equals(oldEmail) && loggedInUser.verifyPassword(password)) {
            loggedInUser.changeEmail(newEmail);
            return true;
        }
        return false;
    }

    private String generateSessionToken() {
        return UUID.randomUUID().toString();
    }

    public boolean validateSessionToken(String token) {
        return sessionToken != null && sessionToken.equals(token);
    }

    private void rateLimit() {
        loginAttempts++;
        if (loginAttempts > 5) {
            throw new RuntimeException("Too many login attempts. Please try again later.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        LoginSystem loginSystem = new LoginSystem();
        loginSystem.registerUser("user1", "user1@example.com", "password123");

        if (loginSystem.login("user1", "password123")) {
            System.out.println("Login successful!");

            if (loginSystem.changeEmail("user1@example.com", "password123", "newemail@example.com")) {
                System.out.println("Email changed successfully!");
            } else {
                System.out.println("Failed to change email.");
            }

            loginSystem.logout();
        } else {
            System.out.println("Login failed.");
        }
    }
}