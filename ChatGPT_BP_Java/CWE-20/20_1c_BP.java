import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.regex.Pattern;

public class RedirectServlet extends HttpServlet {
    private static final String REGEX = "^[a-zA-Z0-9-]+\\.$"; // Matches one or more alphanumeric characters or hyphens followed by a period
    private static final Pattern PATTERN = Pattern.compile(REGEX);

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String target = request.getParameter("target");

        // Validate input
        if (isValidTarget(target)) {
            // Sanitize input
            String sanitizedTarget = sanitizeInput(target);
            // Perform secure redirect
            response.sendRedirect(sanitizedTarget);
        } else {
            // Redirect to the root of the site on failure
            response.sendRedirect(request.getContextPath() + "/");
        }
    }

    private boolean isValidTarget(String target) {
        if (target == null || target.isEmpty()) {
            return false;
        }
        // Check if the target matches the regular expression
        return PATTERN.matcher(target).matches();
    }

    private String sanitizeInput(String target) {
        // Basic sanitization: remove any characters that are not allowed
        // This example assumes the target is a simple URL. Modify according to your needs.
        return target.replaceAll("[^a-zA-Z0-9-\\.]", ""); // Allow only alphanumeric, hyphens, and periods
    }
}
