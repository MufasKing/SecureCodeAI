import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.sql.*;
import java.util.regex.*;

public class StockOrderServlet extends HttpServlet {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/your_database";
    private static final String DB_USER = "your_username";
    private static final String DB_PASSWORD = "your_password";
    private static final String SECRET_KEY = "your_secret_key"; // Secure secret key for signing tokens
    private static final String INSERT_ORDER_SQL = "INSERT INTO stock_orders (stock_name, quantity, user_id) VALUES (?, ?, ?)";
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("/orderForm.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        String stockName = request.getParameter("stock_name");
        String quantityStr = request.getParameter("quantity");
        int quantity = 0;

        // Input validation
        if (stockName == null || stockName.trim().isEmpty() || !isValidStockName(stockName)) {
            request.setAttribute("errorMessage", "Invalid stock name.");
            request.getRequestDispatcher("/orderForm.jsp").forward(request, response);
            return;
        }
        
        try {
            quantity = Integer.parseInt(quantityStr);
            if (quantity <= 0) {
                throw new NumberFormatException("Quantity must be positive.");
            }
        } catch (NumberFormatException e) {
            request.setAttribute("errorMessage", "Invalid quantity.");
            request.getRequestDispatcher("/orderForm.jsp").forward(request, response);
            return;
        }

        // Insert into database
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement preparedStatement = connection.prepareStatement(INSERT_ORDER_SQL)) {
            
            preparedStatement.setString(1, stockName);
            preparedStatement.setInt(2, quantity);
            preparedStatement.setInt(3, (Integer) session.getAttribute("user_id")); // Assuming user_id is stored in session
            preparedStatement.executeUpdate();

        } catch (SQLException e) {
            request.setAttribute("errorMessage", "Database error: " + e.getMessage());
            request.getRequestDispatcher("/orderForm.jsp").forward(request, response);
            return;
        }

        response.sendRedirect("stock_view.jsp");
    }

    private boolean isValidStockName(String stockName) {
        // Basic validation: allow only letters and numbers
        String regex = "^[a-zA-Z0-9]+$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(stockName);
        return matcher.matches();
    }

    // Method for user authentication
    public boolean authenticateUser(String username, String password) {
        // Hash password and check with database (implement as needed)
        return true; // Placeholder
    }

    // Password hashing example (for demonstration only)
    public String hashPassword(String password) {
        // Implement your preferred hashing method (e.g., BCrypt)
        return password; // Placeholder
    }
}
