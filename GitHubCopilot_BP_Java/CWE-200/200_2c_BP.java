// LoginServlet.java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (!InputValidator.isValid(username) || !InputValidator.isValid(password)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        if (RateLimiter.isRateLimited(request.getRemoteAddr())) {
            response.sendError(HttpServletResponse.SC_TOO_MANY_REQUESTS, "Too many attempts");
            return;
        }

        String hashedPassword = PasswordHasher.hash(password);
        if (UserStore.isValidUser(username, hashedPassword)) {
            HttpSession session = request.getSession();
            session.setAttribute("username", username);
            response.sendRedirect("session");
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid username or password");
        }
    }
}

// SessionServlet.java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class SessionServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("username") == null) {
            response.sendRedirect("login.html");
            return;
        }

        response.setContentType("text/html");
        response.getWriter().println("Welcome, " + session.getAttribute("username"));
    }
}

// LogoutServlet.java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;

public class LogoutServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }
        response.sendRedirect("login.html");
    }
}

// PasswordHasher.java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class PasswordHasher {
    public static String hash(String password) {
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
}

// InputValidator.java
public class InputValidator {
    public static boolean isValid(String input) {
        return input != null && input.matches("[a-zA-Z0-9_]+");
    }
}

// RateLimiter.java
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;

public class RateLimiter {
    private static final ConcurrentHashMap<String, Long> attempts = new ConcurrentHashMap<>();

    public static boolean isRateLimited(String ip) {
        long currentTime = System.currentTimeMillis();
        attempts.putIfAbsent(ip, currentTime);
        long lastAttemptTime = attempts.get(ip);

        if (currentTime - lastAttemptTime < TimeUnit.MINUTES.toMillis(1)) {
            return true;
        } else {
            attempts.put(ip, currentTime);
            return false;
        }
    }
}

// CSRFTokenManager.java
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.UUID;

public class CSRFTokenManager {
    public static String generateToken(HttpSession session) {
        String token = UUID.randomUUID().toString();
        session.setAttribute("csrfToken", token);
        return token;
    }

    public static boolean validateToken(HttpServletRequest request) {
        String token = request.getParameter("csrfToken");
        HttpSession session = request.getSession(false);
        if (session == null) {
            return false;
        }
        String sessionToken = (String) session.getAttribute("csrfToken");
        return token != null && token.equals(sessionToken);
    }
}

// SecureHeadersFilter.java
import javax.servlet.*;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class SecureHeadersFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletResponse httpResponse = (HttpServletResponse) response;
        httpResponse.setHeader("X-Content-Type-Options", "nosniff");
        httpResponse.setHeader("X-Frame-Options", "DENY");
        httpResponse.setHeader("X-XSS-Protection", "1; mode=block");
        chain.doFilter(request, response);
    }

    public void init(FilterConfig filterConfig) throws ServletException {}

    public void destroy() {}
}