import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.logging.Level;
import java.util.logging.Logger;

@Controller
@SessionAttributes("userSession")
@RequestMapping("/home")
public class HomeController {

    private static final Logger LOGGER = Logger.getLogger(HomeController.class.getName());

    @Autowired
    private Environment env; // Assuming Environment is injected for configuration

    // Method to sanitize user input
    private String sanitizeInput(String input) {
        return input.replaceAll("[^a-zA-Z0-9 ]", ""); // Simple sanitization, enhance as needed
    }

    // Render response from environment
    public ModelAndView renderResponseFromEnv(HttpServletRequest request, HttpServletResponse response) {
        String name = sanitizeInput(request.getParameter("name")); // Get and sanitize input

        if (name == null || name.isEmpty()) {
            LOGGER.log(Level.WARNING, "Invalid name parameter");
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            return null; // Or return an error view
        }

        try {
            ModelAndView modelAndView = new ModelAndView("template"); // Use your actual template name
            modelAndView.addObject("name", name); // Add sanitized name to model
            return modelAndView;
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Error rendering template", e);
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            return null; // Or return an error view
        }
    }

    @GetMapping
    public ModelAndView home(HttpServletRequest request, HttpServletResponse response) {
        return renderResponseFromEnv(request, response); // Call the render function
    }
}
