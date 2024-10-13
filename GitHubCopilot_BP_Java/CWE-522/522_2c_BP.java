package GitHubCopilot_BP_Java.CWE_522;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class User {
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

class Database {
    private Map<String, User> users = new HashMap<>();

    public void storeUser(User user) {
        users.put(user.getUsername(), user);
    }

    public User getUser(String username) {
        return users.get(username);
    }
}

public class RegistrationForm {
    private static final int SALT_LENGTH = 16;
    private Database database = new Database();

    public static void main(String[] args) {
        RegistrationForm form = new RegistrationForm();
        form.registerUser();
    }

    public void registerUser() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        try {
            if (validateInput(username, password)) {
                String salt = generateSalt();
                String hashedPassword = hashPassword(password, salt);
                String saltedHashedPassword = salt + hashedPassword;

                User user = new User(username, saltedHashedPassword);
                database.storeUser(user);

                System.out.println("User registered successfully!");
            } else {
                System.out.println("Invalid input. Please try again.");
            }
        } catch (NoSuchAlgorithmException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private boolean validateInput(String username, String password) {
        return username != null && !username.isEmpty() && password != null && !password.isEmpty();
    }

    private String generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[SALT_LENGTH];
        random.nextBytes(salt);
        return bytesToHex(salt);
    }

    private String hashPassword(String password, String salt) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update((salt + password).getBytes());
        byte[] hashedBytes = md.digest();
        return bytesToHex(hashedBytes);
    }

    private String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        return hexString.toString();
    }
}