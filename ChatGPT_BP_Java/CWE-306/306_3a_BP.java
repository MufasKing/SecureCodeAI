import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/changeEmail")
public class ChangeEmailServlet extends HttpServlet {
    // Dummy user data store
    private static final String USER_PASSWORD = "hashed_password"; // Hash your password properly
    private static final String USER_EMAIL = "user@example.com";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Ensure user is logged in
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp"); // Redirect to login if not authenticated
            return;
        }

        // Forward to change email page
        request.getRequestDispatcher("/changeEmail.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp"); // Redirect to login if not authenticated
            return;
        }

        String oldEmail = request.getParameter("oldEmail");
        String newEmail = request.getParameter("newEmail");
        String password = request.getParameter("password");

        // Basic input validation
        if (oldEmail == null || newEmail == null || password == null ||
            oldEmail.isEmpty() || newEmail.isEmpty() || password.isEmpty()) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "All fields are required.");
            return;
        }

        // Ensure new email is different from the old one
        if (oldEmail.equals(newEmail)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "New email must be different from the old email.");
            return;
        }

        // Hash the entered password and check it against the stored password
        String hashedPassword = hashPassword(password);
        if (!hashedPassword.equals(USER_PASSWORD)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "Invalid password.");
            return;
        }

        // Update email (here just printing it for demonstration)
        System.out.println("Email changed from " + USER_EMAIL + " to " + newEmail);

        // In a real application, you would update the user email in your database here

        response.sendRedirect("success.jsp"); // Redirect to success page
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : hashedBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}

