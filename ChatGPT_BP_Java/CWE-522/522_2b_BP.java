import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.regex.Pattern;
import org.mindrot.jbcrypt.BCrypt;

public class RegistrationForm {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASSWORD = "yourpassword";
    
    // Regular expression for validating username and password strength
    private static final String USERNAME_REGEX = "^[a-zA-Z0-9]{3,20}$"; // Alphanumeric, 3-20 chars
    private static final String PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,20}$"; // At least 8 chars, 1 upper, 1 lower, 1 number

    public static void main(String[] args) {
        String username = "exampleUser"; // Example username input
        String password = "StrongP@ssw0rd"; // Example password input
        
        try {
            registerUser(username, password);
            System.out.println("User registered successfully.");
        } catch (Exception e) {
            System.out.println("Error during registration: " + e.getMessage());
        }
    }

    private static void registerUser(String username, String password) throws Exception {
        // Validate user input
        if (!isValidUsername(username)) {
            throw new Exception("Invalid username. Must be 3-20 alphanumeric characters.");
        }
        if (!isValidPassword(password)) {
            throw new Exception("Invalid password. Must be 8-20 characters long, contain at least one uppercase letter, one lowercase letter, and one digit.");
        }

        // Hash the password with a salt
        String hashedPassword = hashPassword(password);

        // Store the user in the database
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String sql = "INSERT INTO users (username, password) VALUES (?, ?)";
            try (PreparedStatement statement = connection.prepareStatement(sql)) {
                statement.setString(1, username);
                statement.setString(2, hashedPassword);
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            throw new Exception("Database error: " + e.getMessage());
        }
    }

    private static String hashPassword(String password) {
        // Hash the password with a salt using BCrypt
        return BCrypt.hashpw(password, BCrypt.gensalt());
    }

    private static boolean isValidUsername(String username) {
        return Pattern.matches(USERNAME_REGEX, username);
    }

    private static boolean isValidPassword(String password) {
        return Pattern.matches(PASSWORD_REGEX, password);
    }
}
