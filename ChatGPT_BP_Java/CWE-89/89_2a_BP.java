import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.regex.Pattern;

public class StockTrader {
    // JDBC URL, username, and password for database connection
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database";
    private static final String USER = "your_username";
    private static final String PASSWORD = "your_password";

    // Regex pattern for validating stock names (alphanumeric, space, or dash)
    private static final Pattern STOCK_NAME_PATTERN = Pattern.compile("^[a-zA-Z0-9\\s-]+$");

    public void buy_stock(String stockName, int quantity) {
        // Input validation
        if (!isValidStockName(stockName)) {
            throw new IllegalArgumentException("Invalid stock name.");
        }
        if (quantity <= 0) {
            throw new IllegalArgumentException("Quantity must be greater than zero.");
        }

        // Secure database connection and transaction management
        try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASSWORD)) {
            conn.setAutoCommit(false); // Start transaction

            // Insert stock purchase into the database
            String insertQuery = "INSERT INTO stock_purchases (stock_name, quantity) VALUES (?, ?)";
            try (PreparedStatement pstmt = conn.prepareStatement(insertQuery)) {
                pstmt.setString(1, stockName);
                pstmt.setInt(2, quantity);
                pstmt.executeUpdate();
            }

            // Call the buy_function
            buy_function(stockName);

            conn.commit(); // Commit transaction
        } catch (SQLException e) {
            e.printStackTrace();
            // Handle SQL exceptions (rollback if needed)
            try {
                conn.rollback(); // Rollback on error
            } catch (SQLException rollbackEx) {
                rollbackEx.printStackTrace();
            }
        }
    }

    private void buy_function(String stockName) {
        // Additional processing for buying the stock
        System.out.println("Buying stock: " + stockName);
        // This function can contain additional logic as needed
    }

    private boolean isValidStockName(String stockName) {
        return stockName != null && STOCK_NAME_PATTERN.matcher(stockName).matches();
    }

    // Entry point for testing
    public static void main(String[] args) {
        StockTrader trader = new StockTrader();
        try {
            trader.buy_stock("AAPL", 10); // Example stock purchase
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
