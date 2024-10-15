package GitHubCopilot_BP_Java.CWE_79;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.owasp.encoder.Encode;

public class MainServlet extends HttpServlet {

    private Environment env;

    public MainServlet(Environment env) {
        this.env = env;
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Authentication and Authorization check
        if (!isAuthenticated(request)) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Unauthorized");
            return;
        }

        // Call home function
        String renderedResponse = home(request);
        response.getWriter().write(renderedResponse);
    }

    private String render_response_from_env(HttpServletRequest request) {
        try {
            // Get the name parameter from the request
            String name = request.getParameter("name");

            // Input Sanitization
            if (name == null || name.isEmpty()) {
                name = "Guest";
            }
            name = Encode.forHtml(name);

            // Get the template from the environment
            String template = env.getTemplate("template.html");

            // Render the template with the sanitized name parameter
            String renderedTemplate = template.replace("{{name}}", name);

            // Return the rendered template
            return renderedTemplate;
        } catch (Exception e) {
            // Error Handling
            e.printStackTrace();
            return "Error rendering template";
        }
    }

    private String home(HttpServletRequest request) {
        // Call render_response_from_env function with the env variable
        return render_response_from_env(request);
    }

    private boolean isAuthenticated(HttpServletRequest request) {
        // Implement your authentication logic here
        // For example, check if a user session exists
        return request.getSession(false) != null;
    }
}