import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

@Controller
public class HomeController {

    @Autowired
    private TemplateService templateService;

    @GetMapping("/home")
    public ModelAndView home(HttpServletRequest request, HttpServletResponse response) {
        // Call render_response_from_env with the current request and response
        return renderResponseFromEnv(request, response);
    }

    private ModelAndView renderResponseFromEnv(HttpServletRequest request, HttpServletResponse response) {
        // Input Validation and Sanitization
        String name = request.getParameter("name");
        if (name == null || name.isEmpty()) {
            name = "Guest"; // Default name if not provided
        } else {
            // Sanitize input
            name = sanitizeInput(name);
        }

        // Get the template
        String template = templateService.getTemplate();

        // Output Encoding
        String encodedName = outputEncode(name);

        // Render the template with the sanitized and encoded name
        Map<String, String> model = new HashMap<>();
        model.put("name", encodedName);
        String renderedTemplate = templateService.render(template, model);

        // Security Headers
        response.setHeader("Content-Security-Policy", "default-src 'self'");
        response.setHeader("X-Content-Type-Options", "nosniff");
        response.setHeader("X-Frame-Options", "DENY");
        response.setHeader("X-XSS-Protection", "1; mode=block");

        // Return the response with the rendered template
        return new ModelAndView("responseView", "content", renderedTemplate);
    }

    private String sanitizeInput(String input) {
        // Implement input sanitization logic (e.g., strip HTML tags, etc.)
        return input.replaceAll("[<>]", "");
    }

    private String outputEncode(String input) {
        // Implement output encoding to prevent XSS attacks
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#x27;");
    }
}
