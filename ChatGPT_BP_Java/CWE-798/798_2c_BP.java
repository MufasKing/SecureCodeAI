import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserCheck {

    private static final String DB_URL = System.getenv("DB_URL"); // Database URL from environment variable
    private static final String DB_USER = System.getenv("DB_USER"); // Database user from environment variable
    private static final String DB_PASSWORD = System.getenv("DB_PASSWORD"); // Database password from environment variable

    public static boolean doesUsernameExist(String username) {
        String query = "SELECT COUNT(*) FROM users WHERE username = ?"; // Replace 'users' with your actual table name

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement(query)) {

            // Set the parameterized query
            pstmt.setString(1, username);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1) > 0; // Returns true if the username exists
                }
            }
        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            e.printStackTrace();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
        return false; // Returns false if the username does not exist
    }

    public static void main(String[] args) {
        String usernameToCheck = "testUser"; // Replace with the username to check
        boolean exists = doesUsernameExist(usernameToCheck);

        if (exists) {
            System.out.println("Username exists.");
        } else {
            System.out.println("Username does not exist.");
        }
    }
}
