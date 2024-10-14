import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.regex.Pattern;

public class UnsubscribeService {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "least_privilege_user";
    private static final String DB_PASSWORD = "password";

    public String unsubscribe(String email) {
        if (!isValidEmail(email)) {
            return "Invalid email format.";
        }

        String sanitizedEmail = sanitizeEmail(email);

        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            if (isEmailInDatabase(connection, sanitizedEmail)) {
                removeEmailFromDatabase(connection, sanitizedEmail);
                return "You have been successfully unsubscribed.";
            } else {
                return "Email address not found in the database.";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return "An error occurred while processing your request.";
        }
    }

    private boolean isValidEmail(String email) {
        String emailRegex = "^[A-Za-z0-9+_.-]+@(.+)$";
        Pattern pattern = Pattern.compile(emailRegex);
        return pattern.matcher(email).matches();
    }

    private String sanitizeEmail(String email) {
        return email.trim().toLowerCase();
    }

    private boolean isEmailInDatabase(Connection connection, String email) throws SQLException {
        String query = "SELECT COUNT(*) FROM subscribers WHERE email = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, email);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return resultSet.getInt(1) > 0;
                }
            }
        }
        return false;
    }

    private void removeEmailFromDatabase(Connection connection, String email) throws SQLException {
        String query = "DELETE FROM subscribers WHERE email = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, email);
            statement.executeUpdate();
        }
    }

    public static void main(String[] args) {
        UnsubscribeService service = new UnsubscribeService();
        String result = service.unsubscribe("user@example.com");
        System.out.println(result);
    }
}