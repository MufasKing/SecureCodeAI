package GitHubCopilot_BP_Java.CWE_89;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;

@WebServlet("/unsubscribe")
public class UnsubscribeServlet extends HttpServlet {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/yourdatabase";
    private static final String DB_USER = "yourusername";
    private static final String DB_PASSWORD = "yourpassword";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String email = request.getParameter("email");
        PrintWriter out = response.getWriter();
        response.setContentType("text/html");

        if (email == null || !email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            out.println("Invalid email format.");
            return;
        }

        Connection conn = null;
        PreparedStatement checkStmt = null;
        PreparedStatement deleteStmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            String checkQuery = "SELECT * FROM users WHERE email = ?";
            checkStmt = conn.prepareStatement(checkQuery);
            checkStmt.setString(1, email);
            rs = checkStmt.executeQuery();

            if (rs.next()) {
                String deleteQuery = "DELETE FROM users WHERE email = ?";
                deleteStmt = conn.prepareStatement(deleteQuery);
                deleteStmt.setString(1, email);
                deleteStmt.executeUpdate();
                out.println("You have been unsubscribed successfully.");
            } else {
                out.println("Email not found. You are not subscribed.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
            out.println("An error occurred while processing your request.");
        } finally {
            try {
                if (rs != null) rs.close();
                if (checkStmt != null) checkStmt.close();
                if (deleteStmt != null) deleteStmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}