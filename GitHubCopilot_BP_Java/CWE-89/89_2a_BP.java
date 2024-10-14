package GitHubCopilot_BP_Java.CWE_89;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Main {

    public static void main(String[] args) {
        // Example usage
        buy_stock("AAPL", 10);
    }

    public static void buy_stock(String stockName, int quantity) {
        // Input Validation
        if (stockName == null || stockName.isEmpty() || quantity <= 0) {
            throw new IllegalArgumentException("Invalid stock name or quantity");
        }

        Connection conn = null;
        PreparedStatement pstmt = null;

        try {
            // Secure Database Connection
            String url = "jdbc:mysql://localhost:3306/yourdatabase";
            String user = "yourusername";
            String password = "yourpassword";
            conn = DriverManager.getConnection(url, user, password);

            // Parameterized Query
            String sql = "INSERT INTO stocks (stock_name, quantity) VALUES (?, ?)";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, stockName);
            pstmt.setInt(2, quantity);

            // Execute the query
            pstmt.executeUpdate();

            // Call buy_function
            buy_function(stockName);

        } catch (SQLException e) {
            // Error Handling
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public static void buy_function(String stockName) {
        // Perform operations with the stock name
        System.out.println("Buying stock: " + stockName);
    }
}