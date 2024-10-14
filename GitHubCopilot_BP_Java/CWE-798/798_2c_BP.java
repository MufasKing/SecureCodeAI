package GitHubCopilot_BP_Java.CWE-798;

import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String usernameToCheck = "exampleUsername"; // Replace with the actual username to check
        boolean userExists = checkIfUserExists(usernameToCheck);
        System.out.println("User exists: " + userExists);
    }

    public static boolean checkIfUserExists(String username) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        boolean exists = false;

        try {
            // Load environment variables
            String dbUrl = System.getenv("DB_URL");
            String dbUser = System.getenv("DB_USER");
            String dbPassword = System.getenv("DB_PASSWORD");

            // Establish a secure database connection
            conn = DriverManager.getConnection(dbUrl, dbUser, dbPassword);

            // Create a parameterized query
            String query = "SELECT 1 FROM users WHERE username = ?";
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, username);

            // Execute the query
            rs = pstmt.executeQuery();
            exists = rs.next();

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close the database connection
            try {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        return exists;
    }
}