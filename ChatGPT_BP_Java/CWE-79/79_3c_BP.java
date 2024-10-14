import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.regex.Pattern;

// Utility class for HTML escaping
class HtmlUtils {
    public static String escape(String input) {
        if (input == null) {
            return null;
        }
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#39;");
    }
}

// Decorator for URL mapping
@interface Route {
    String value();
}

// Handler for routing and executing functions
class RouteHandler extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String path = request.getRequestURI();
        String[] parts = path.split("/");

        if (parts.length == 3 && "hello".equals(parts[1])) {
            String username = parts[2];

            // Validate and sanitize username
            if (isValidUsername(username)) {
                String result = hello(username);
                response.getWriter().write(result);
            } else {
                response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid username.");
            }
        } else {
            response.sendError(HttpServletResponse.SC_NOT_FOUND, "Route not found.");
        }
    }

    // Function that returns a greeting
    @Route("/hello/{username}")
    public String hello(String username) {
        // Escape special characters
        String safeUsername = HtmlUtils.escape(username);
        return "Hello, " + safeUsername + "!";
    }

    // Validate the username input
    private boolean isValidUsername(String username) {
        // Username must match a specific pattern (alphanumeric and underscores only)
        Pattern pattern = Pattern.compile("^[a-zA-Z0-9_]+$");
        return pattern.matcher(username).matches();
    }
}

// In a real application, the servlet would be registered in a web.xml or using annotations
