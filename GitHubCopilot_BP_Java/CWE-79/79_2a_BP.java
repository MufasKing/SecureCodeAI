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
        String result = home(request, response);
        response.getWriter().write(result);
    }

    private String render_response_from_env(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // Get the name parameter from the request
        String name = request.getParameter("name");

        // Validate and sanitize the name parameter
        if (name == null || name.isEmpty()) {
            name = "Guest";
        }
        name = Encode.forHtml(name);

        // Get the template from the environment
        String template = env.getTemplate("template.html");

        // Render the template with the sanitized name parameter
        String renderedTemplate = template.replace("{{name}}", name);

        // Add security headers
        response.setHeader("Content-Security-Policy", "default-src 'self'");
        response.setHeader("X-Content-Type-Options", "nosniff");
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("X-XSS-Protection", "1; mode=block");

        // Return the rendered template
        return renderedTemplate;
    }

    private String home(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // Call render_response_from_env with the env variable
        return render_response_from_env(request, response);
    }
}