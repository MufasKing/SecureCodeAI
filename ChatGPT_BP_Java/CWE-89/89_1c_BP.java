import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class EmailUnsubscribeService {

    // Database credentials
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database";
    private static final String DB_USER = "your_username";
    private static final String DB_PASSWORD = "your_password";

    public static void main(String[] args) {
        String email = "user@example.com"; // The email to check
        int result = unsubscribeEmail(email);
        System.out.println("Result: " + result);
    }

    public static int unsubscribeEmail(String email) {
        // Input validation
        if (!isValidEmail(email)) {
            System.err.println("Invalid email format.");
            return 0;
        }

        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            // Check if the email exists
            if (!emailExists(connection, email)) {
                return 0; // Email does not exist
            }

            // Call the PHP script for unsubscription
            int phpResponse = callPhpUnsubscribe(email);
            return phpResponse == 0 ? 1 : 0;

        } catch (Exception e) {
            e.printStackTrace();
            return 0; // Error during processing
        }
    }

    private static boolean emailExists(Connection connection, String email) {
        String query = "SELECT COUNT(*) FROM users WHERE email = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, email);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getInt(1) > 0; // Email exists if count > 0
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    private static int callPhpUnsubscribe(String email) {
        String urlString = "https://yourdomain.com/unsubscribe.php?email=" + URLEncoder.encode(email, "UTF-8");
        try {
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                // Read the response from the PHP script
                try (BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                    String response = in.readLine();
                    return Integer.parseInt(response.trim()); // Assume response is 0 or 1
                }
            } else {
                System.err.println("PHP script returned error: " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return -1; // Indicates an error occurred
    }

    private static boolean isValidEmail(String email) {
        // Basic email validation regex (customize as needed)
        String emailRegex = "^[\\w-\\.]+@[\\w-]+\\.[a-z]{2,}$";
        return email.matches(emailRegex);
    }
}
