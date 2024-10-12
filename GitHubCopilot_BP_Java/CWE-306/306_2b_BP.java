import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import org.mindrot.jbcrypt.BCrypt;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private static final Map<String, String> userDatabase = new HashMap<>();
    private static final String CSRF_TOKEN = "csrf_token";

    static {
        // Simulate a user database with hashed passwords
        userDatabase.put("user1", BCrypt.hashpw("password123", BCrypt.gensalt()));
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        String csrfToken = generateCSRFToken();
        session.setAttribute(CSRF_TOKEN, csrfToken);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<form method='POST' action='login'>");
        out.println("Username: <input type='text' name='username' required><br>");
        out.println("Password: <input type='password' name='password' required><br>");
        out.println("<input type='hidden' name='csrf_token' value='" + csrfToken + "'>");
        out.println("<input type='submit' value='Login'>");
        out.println("</form>");
        out.println("</body></html>");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = sanitizeInput(request.getParameter("username"));
        String password = sanitizeInput(request.getParameter("password"));
        String csrfToken = request.getParameter("csrf_token");

        HttpSession session = request.getSession();
        String sessionCsrfToken = (String) session.getAttribute(CSRF_TOKEN);

        if (csrfToken == null || !csrfToken.equals(sessionCsrfToken)) {
            response.sendError(HttpServletResponse.SC_FORBIDDEN, "CSRF token mismatch");
            return;
        }

        if (username == null || password == null) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        String hashedPassword = userDatabase.get(username);
        if (hashedPassword != null && BCrypt.checkpw(password, hashedPassword)) {
            session.setAttribute("user", username);
            response.sendRedirect("user_page");
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid username or password");
        }
    }

    private String generateCSRFToken() {
        return Long.toHexString(Double.doubleToLongBits(Math.random()));
    }

    private String sanitizeInput(String input) {
        return input == null ? null : input.replaceAll("[^a-zA-Z0-9]", "");
    }
}