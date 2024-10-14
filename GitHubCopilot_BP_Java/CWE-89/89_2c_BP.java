package GitHubCopilot_BP_Java.CWE_89;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebFilter;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import java.io.IOException;
import java.security.SecureRandom;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Base64;

public class Main {
    public static void main(String[] args) {
        // Main method can be used to start the server or for other purposes
    }
}

@WebServlet("/buy_order")
class BuyOrderServlet extends HttpServlet {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASSWORD = "yourpassword";

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        String csrfToken = request.getParameter("csrf_token");
        if (csrfToken == null || !csrfToken.equals(session.getAttribute("csrfToken"))) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "CSRF token mismatch");
            return;
        }

        String stockName = request.getParameter("stockName");
        String quantityStr = request.getParameter("quantity");

        if (stockName == null || stockName.isEmpty() || quantityStr == null || quantityStr.isEmpty()) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        int quantity;
        try {
            quantity = Integer.parseInt(quantityStr);
        } catch (NumberFormatException e) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid quantity");
            return;
        }

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String sql = "INSERT INTO orders (stock_name, quantity) VALUES (?, ?)";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, stockName);
                stmt.setInt(2, quantity);
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new ServletException("Database error", e);
        }

        response.sendRedirect("stock_view.jsp");
    }
}

@WebFilter("/*")
class SecurityFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        HttpServletResponse httpResponse = (HttpServletResponse) response;
        HttpSession session = httpRequest.getSession(true);

        if (session.isNew()) {
            SecureRandom secureRandom = new SecureRandom();
            byte[] token = new byte[32];
            secureRandom.nextBytes(token);
            String csrfToken = Base64.getEncoder().encodeToString(token);
            session.setAttribute("csrfToken", csrfToken);
        }

        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {
    }
}