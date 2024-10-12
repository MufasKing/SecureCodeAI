import java.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.mindrot.jbcrypt.BCrypt;

@WebServlet("/database")
public class DatabaseServlet extends HttpServlet {

    // Database configuration
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database_name";
    private static final String DB_USER = "your_database_user";
    private static final String DB_PASSWORD = "your_database_password";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Example usage
        try {
            Connection connection = getDatabaseConnection();
            // Your logic here (querying, etc.)
            response.getWriter().println("Database connection successful.");
        } catch (SQLException e) {
            handleError(response, "Database connection error: " + e.getMessage());
        }
    }

    // Function to get a database connection
    private Connection getDatabaseConnection() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
    }

    // Function to return server name
    private String getServerName() {
        return "localhost"; // Change as needed
    }

    // Function to return database name
    private String getDatabaseName() {
        return "your_database_name"; // Change as needed
    }

    // Function to return database user
    private String getDatabaseUser() {
        return DB_USER;
    }

    // Function to return database password (for demonstration purposes only)
    private String getDatabasePassword() {
        return DB_PASSWORD;
    }

    // Password hashing example
    public String hashPassword(String plainPassword) {
        return BCrypt.hashpw(plainPassword, BCrypt.gensalt());
    }

    // Method to handle errors
    private void handleError(HttpServletResponse response, String message) throws IOException {
        response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        response.getWriter().println(message);
    }

    // Example of secure SQL execution to prevent SQL Injection
    public void executeSecureQuery(String userInput) {
        String query = "SELECT * FROM users WHERE username = ?";
        try (Connection connection = getDatabaseConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, userInput);
            ResultSet resultSet = preparedStatement.executeQuery();
            // Process resultSet as needed
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
