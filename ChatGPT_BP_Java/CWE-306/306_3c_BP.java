import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class SimpleLoginSystem {

    // In-memory user storage
    private static Map<String, User> users = new HashMap<>();
    private static String currentUser;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int attempts = 0;
        
        // Pre-populate with a test user (username: user, password: password123, email: user@example.com)
        users.put("user", new User("user", hashPassword("password123"), "user@example.com"));

        while (true) {
            System.out.println("1. Login\n2. Change Email\n3. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine();  // consume newline

            switch (choice) {
                case 1:
                    if (login(scanner)) {
                        System.out.println("Login successful!");
                    } else {
                        System.out.println("Login failed!");
                        attempts++;
                        if (attempts >= 3) {
                            System.out.println("Too many failed attempts. Exiting.");
                            return;
                        }
                    }
                    break;
                case 2:
                    if (currentUser != null) {
                        changeEmail(scanner);
                    } else {
                        System.out.println("You must be logged in to change your email.");
                    }
                    break;
                case 3:
                    System.out.println("Exiting.");
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    private static boolean login(Scanner scanner) {
        System.out.print("Username: ");
        String username = scanner.nextLine();
        System.out.print("Password: ");
        String password = scanner.nextLine();

        User user = users.get(username);
        if (user != null && verifyPassword(password, user.getPasswordHash())) {
            currentUser = username;
            return true;
        }
        return false;
    }

    private static void changeEmail(Scanner scanner) {
        System.out.print("Enter your old email: ");
        String oldEmail = scanner.nextLine();
        System.out.print("Confirm your password: ");
        String password = scanner.nextLine();

        User user = users.get(currentUser);
        if (user.getEmail().equals(oldEmail) && verifyPassword(password, user.getPasswordHash())) {
            System.out.print("Enter your new email: ");
            String newEmail = scanner.nextLine();
            if (isValidEmail(newEmail)) {
                user.setEmail(newEmail);
                System.out.println("Email changed successfully!");
            } else {
                System.out.println("Invalid email format.");
            }
        } else {
            System.out.println("Old email or password is incorrect. Email change failed.");
        }
    }

    private static boolean isValidEmail(String email) {
        return email != null && email.contains("@") && email.contains(".");
    }

    private static String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedPassword = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : hashedPassword) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    private static boolean verifyPassword(String password, String hashedPassword) {
        return hashPassword(password).equals(hashedPassword);
    }

    private static class User {
        private String username;
        private String passwordHash;
        private String email;

        public User(String username, String passwordHash, String email) {
            this.username = username;
            this.passwordHash = passwordHash;
            this.email = email;
        }

        public String getPasswordHash() {
            return passwordHash;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }
    }
}
