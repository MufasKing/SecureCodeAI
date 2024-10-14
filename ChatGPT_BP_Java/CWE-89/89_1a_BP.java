import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;
import java.util.regex.Pattern;

public class UnsubscribeService {
    // Database connection parameters
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database"; // Update with your database URL
    private static final String DB_USER = "your_user"; // Update with your database user
    private static final String DB_PASSWORD = "your_password"; // Update with your database password

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your email address to unsubscribe: ");
        String email = scanner.nextLine().trim();

        // Input validation
        if (!isValidEmail(email)) {
            System.out.println("Invalid email format.");
            return;
        }

        // Data sanitization: escaping SQL input is handled by PreparedStatement
        unsubscribe(email);
    }

    private static boolean isValidEmail(String email) {
        // Simple regex for email validation
        String emailRegex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        Pattern pattern = Pattern.compile(emailRegex);
        return pattern.matcher(email).matches();
    }

    private static void unsubscribe(String email) {
        String selectQuery = "SELECT email FROM subscribers WHERE email = ?";
        String deleteQuery = "DELETE FROM subscribers WHERE email = ?";

        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement selectStatement = connection.prepareStatement(selectQuery);
             PreparedStatement deleteStatement = connection.prepareStatement(deleteQuery)) {

            // Set parameters for select query
            selectStatement.setString(1, email);
            ResultSet resultSet = selectStatement.executeQuery();

            // Check if the email exists
            if (resultSet.next()) {
                // Email exists, proceed to delete
                deleteStatement.setString(1, email);
                deleteStatement.executeUpdate();
                System.out.println("You have been successfully unsubscribed.");
            } else {
                // Email does not exist
                System.out.println("Your email address is not found in our database.");
            }

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            // Log error (consider logging to a file or monitoring system)
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
