import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ModeratorCheck {

    // Method to check if the user is a moderator
    public static boolean isUserModerator(String username) {
        // Get database credentials from environment variables
        String url = System.getenv("DB_URL");
        String user = System.getenv("DB_USER");
        String password = System.getenv("DB_PASSWORD");

        // Validate the database credentials
        if (url == null || user == null || password == null) {
            System.err.println("Database credentials are not set in the environment variables.");
            return false;
        }

        // Database connection object
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;

        try {
            // Establish the database connection
            connection = DriverManager.getConnection(url, user, password);

            // Prepare the SQL query to check if the user is a moderator
            String sql = "SELECT is_moderator FROM users WHERE username = ?";
            preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, username);

            // Execute the query
            resultSet = preparedStatement.executeQuery();

            // Check if the user is a moderator
            if (resultSet.next()) {
                return resultSet.getBoolean("is_moderator");
            } else {
                System.out.println("User not found.");
                return false;
            }

        } catch (SQLException e) {
            // Handle SQL exceptions
            System.err.println("SQL error: " + e.getMessage());
            return false;
        } finally {
            // Close the resources
            try {
                if (resultSet != null) resultSet.close();
                if (preparedStatement != null) preparedStatement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                System.err.println("Error closing resources: " + e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        // Example usage
        String username = "exampleUser";
        boolean isModerator = isUserModerator(username);
        System.out.println("Is the user a moderator? " + isModerator);
    }
}
