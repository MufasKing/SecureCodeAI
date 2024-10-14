package GitHubCopilot_BP_Java.CWE-20;

import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MainServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private static final String REGEX = "^[a-zA-Z0-9-]+\\.$";
    private static final Pattern PATTERN = Pattern.compile(REGEX);

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String target = request.getParameter("target");
        if (target != null) {
            target = sanitizeInput(target);
            Matcher matcher = PATTERN.matcher(target);
            if (matcher.matches()) {
                response.sendRedirect(target);
            } else {
                response.sendRedirect("/");
            }
        } else {
            response.sendRedirect("/");
        }
    }

    private String sanitizeInput(String input) {
        // Basic sanitization to remove any potential harmful characters
        return input.replaceAll("[^a-zA-Z0-9-\\.]", "");
    }
}