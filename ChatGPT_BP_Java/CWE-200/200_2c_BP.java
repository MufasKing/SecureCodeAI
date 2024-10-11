import java.io.IOException;
import java.io.PrintWriter;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    // Mocked user database with hashed password (password is "password123")
    private Map<String, String> userDb = new HashMap<>();
    
    // For rate limiting (3 attempts per minute)
    private Map<String, AtomicInteger> loginAttempts = new ConcurrentHashMap<>();
    private Map<String, Instant> blockTime = new ConcurrentHashMap<>();

    @Override
    public void init() throws ServletException {
        // Simulating stored hash of "password123" using SHA-256
        userDb.put("admin", hashPassword("password123"));
    }

    // Password hashing using SHA-256
    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // Secure headers to prevent Clickjacking and XSS
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("X-Content-Type-Options", "nosniff");
        response.setHeader("X-XSS-Protection", "1; mode=block");
        
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String csrfToken = request.getParameter("csrfToken");
        
        // Validate input (preventing SQL Injection and XSS)
        if (!isValidInput(username) || !isValidInput(password)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input.");
            return;
        }

        HttpSession session = request.getSession(false);
        if (session != null && csrfToken.equals(session.getAttribute("csrfToken"))) {
            response.sendRedirect("SessionServlet");
            return;
        }

        // Rate limiting: 3 attempts per minute
        String clientIp = request.getRemoteAddr();
        AtomicInteger attempts = loginAttempts.computeIfAbsent(clientIp, k -> new AtomicInteger(0));
        Instant blockedUntil = blockTime.get(clientIp);
        if (blockedUntil != null && blockedUntil.isAfter(Instant.now())) {
            response.getWriter().println("You are temporarily blocked due to too many failed attempts.");
            return;
        }

        if (attempts.incrementAndGet() > 3) {
            blockTime.put(clientIp, Instant.now().plusSeconds(60));
            response.getWriter().println("Too many failed attempts. You are blocked for 1 minute.");
            return;
        }

        // Password hash checking
        if (userDb.containsKey(username) && userDb.get(username).equals(hashPassword(password))) {
            // Reset login attempts on successful login
            loginAttempts.remove(clientIp);

            // Create session and set CSRF token
            session = request.getSession(true);
            session.setAttribute("username", username);
            String newCsrfToken = generateCSRFToken();
            session.setAttribute("csrfToken", newCsrfToken);

            // Secure cookie (HttpOnly and Secure flags)
            Cookie sessionCookie = new Cookie("JSESSIONID", session.getId());
            sessionCookie.setHttpOnly(true);
            sessionCookie.setSecure(true);
            response.addCookie(sessionCookie);

            response.sendRedirect("SessionServlet"); // Redirect to session page securely
        } else {
            response.getWriter().println("Invalid username or password.");
        }
    }

    private boolean isValidInput(String input) {
        return input != null && input.matches("^[a-zA-Z0-9_]+$");
    }

    private String generateCSRFToken() {
        return Long.toHexString(Double.doubleToLongBits(Math.random()));
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Display login form with CSRF protection token
        HttpSession session = request.getSession(true);
        String csrfToken = generateCSRFToken();
        session.setAttribute("csrfToken", csrfToken);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<form method='POST' action='LoginServlet'>");
        out.println("Username: <input type='text' name='username'><br>");
        out.println("Password: <input type='password' name='password'><br>");
        out.println("<input type='hidden' name='csrfToken' value='" + csrfToken + "'>");
        out.println("<input type='submit' value='Login'>");
        out.println("</form>");
        out.println("</body></html>");
    }
}

@WebServlet("/SessionServlet")
class SessionServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null && session.getAttribute("username") != null) {
            response.getWriter().println("Welcome, " + session.getAttribute("username"));
            response.getWriter().println("<form method='POST' action='LogoutServlet'>");
            response.getWriter().println("<input type='submit' value='Logout'>");
            response.getWriter().println("</form>");
        } else {
            response.sendRedirect("LoginServlet");
        }
    }
}

@WebServlet("/LogoutServlet")
class LogoutServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate(); // Destroy session
        }
        response.sendRedirect("LoginServlet"); // Redirect to login page after logout
    }
}
