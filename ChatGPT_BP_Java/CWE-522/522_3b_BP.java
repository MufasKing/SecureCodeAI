import org.mindrot.jbcrypt.BCrypt;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class UserAuthentication {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database";
    private static final String DB_USER = "your_username";
    private static final String DB_PASSWORD = "your_password";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // User Registration
        System.out.print("Enter username for registration: ");
        String username = scanner.nextLine();
        
        System.out.print("Enter password for registration: ");
        String password = scanner.nextLine();
        
        try {
            registerUser(username, password);
        } catch (SQLException e) {
            System.out.println("Registration failed: " + e.getMessage());
        }

        // User Login
        System.out.print("Enter username for login: ");
        String loginUsername = scanner.nextLine();
        
        System.out.print("Enter password for login: ");
        String loginPassword = scanner.nextLine();

        try {
            if (validateUser(loginUsername, loginPassword)) {
                System.out.println("Login successful!");
            } else {
                System.out.println("Invalid username or password.");
            }
        } catch (SQLException e) {
            System.out.println("Login failed: " + e.getMessage());
        }

        scanner.close();
    }

    private static void registerUser(String username, String password) throws SQLException {
        String hashedPassword = hashPassword(password);

        String sql = "INSERT INTO users (username, password) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, username);
            pstmt.setString(2, hashedPassword);
            pstmt.executeUpdate();
            System.out.println("User registered successfully.");
        }
    }

    private static String hashPassword(String password) {
        return BCrypt.hashpw(password, BCrypt.gensalt());
    }

    private static boolean validateUser(String username, String password) throws SQLException {
        String sql = "SELECT password FROM users WHERE username = ?";
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, username);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                String storedHashedPassword = rs.getString("password");
                return BCrypt.checkpw(password, storedHashedPassword);
            }
        }
        return false;
    }
}
