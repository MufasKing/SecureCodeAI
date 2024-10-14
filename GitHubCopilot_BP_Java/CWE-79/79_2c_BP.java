package GitHubCopilot_BP_Java.CWE-79;

import java.util.logging.Logger;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.owasp.encoder.Encode;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.WebContext;

public class Main {
    private static final Logger logger = Logger.getLogger(Main.class.getName());
    private static final TemplateEngine templateEngine = new TemplateEngine();

    public static void main(String[] args) {
        // Example usage
        // HttpServletRequest request = ...;
        // HttpServletResponse response = ...;
        // String env = ...;
        // home(request, response, env);
    }

    public static void render_response_from_env(HttpServletRequest request, HttpServletResponse response, String env) {
        try {
            // Get the name parameter from the user request
            String name = request.getParameter("name");

            // Input Sanitization and Validation
            if (name == null || name.isEmpty() || !name.matches("^[a-zA-Z0-9_]+$")) {
                response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
                return;
            }

            // Secure Template Rendering
            WebContext context = new WebContext(request, response, request.getServletContext());
            context.setVariable("name", Encode.forHtml(name));

            // Get the template from the environment
            String template = env; // Assuming env contains the template name

            // Render the template with the name parameter
            String renderedTemplate = templateEngine.process(template, context);

            // Return a response with the rendered template
            response.setContentType("text/html");
            response.getWriter().write(renderedTemplate);

            // Logging and Monitoring
            logger.info("Rendered template successfully for user: " + name);

        } catch (Exception e) {
            // Error Handling
            logger.severe("Error rendering template: " + e.getMessage());
            try {
                response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "An error occurred");
            } catch (Exception ex) {
                logger.severe("Error sending error response: " + ex.getMessage());
            }
        }
    }

    public static void home(HttpServletRequest request, HttpServletResponse response, String env) {
        render_response_from_env(request, response, env);
    }
}