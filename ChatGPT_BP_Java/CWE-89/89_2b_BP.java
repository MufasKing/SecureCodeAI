import javax.servlet.*;
import javax.servlet.http.*;
import javax.sql.DataSource;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class BuyStockServlet extends HttpServlet {
    
    private DataSource dataSource; // Assume this is configured and injected.

    @Override
    public void init() throws ServletException {
        // Initialize the data source for database connection
        // This would usually be done via JNDI or some dependency injection mechanism.
        //dataSource = // Obtain your data source here.
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Step 1: Authenticate User
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("username") == null) {
            response.sendRedirect("login.jsp");
            return;
        }
        String username = (String) session.getAttribute("username");
        
        // Step 2: Get Input Data
        String stockName = request.getParameter("stock_name");
        String stockQuantityStr = request.getParameter("stock_quantity");
        
        // Step 3: Input Validation
        if (stockName == null || stockName.isEmpty() || stockQuantityStr == null || !isNumeric(stockQuantityStr)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        int stockQuantity = Integer.parseInt(stockQuantityStr);

        // Step 4: Input Sanitization (optional, depending on requirements)
        stockName = sanitizeInput(stockName);

        // Step 5: Insert Order into Database
        try (Connection connection = dataSource.getConnection()) {
            String sql = "INSERT INTO stock_orders (username, stock_name, stock_quantity) VALUES (?, ?, ?)";
            try (PreparedStatement statement = connection.prepareStatement(sql)) {
                statement.setString(1, username);
                statement.setString(2, stockName);
                statement.setInt(3, stockQuantity);
                statement.executeUpdate();
            }
        } catch (SQLException e) {
            // Log error and send error response
            e.printStackTrace();
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error");
            return;
        }

        // Step 6: Secure Redirection to Profile Page
        response.sendRedirect("profile.jsp");
    }

    private boolean isNumeric(String str) {
        return str != null && str.matches("\\d+");
    }

    private String sanitizeInput(String input) {
        // Sanitize input to prevent XSS and other injections
        return input.replaceAll("[^a-zA-Z0-9 ]", "");
    }

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "GET method is not supported.");
    }

    @Override
    public void destroy() {
        // Clean up resources if needed
    }
}
