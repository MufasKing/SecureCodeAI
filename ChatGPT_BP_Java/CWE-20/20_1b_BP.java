import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

@SpringBootApplication
@RestController
public class RedirectApplication {

    private static final String REGEX = "^(https?://)?(www\\.)?example\\.com/.*$";

    public static void main(String[] args) {
        SpringApplication.run(RedirectApplication.class, args);
    }

    @GetMapping("/redirect")
    public void redirect(@RequestParam String target, HttpServletResponse response) throws IOException {
        String sanitizedTarget = sanitizeInput(target);
        String finalUrl = validateAndConstructUrl(sanitizedTarget);

        if (finalUrl != null) {
            response.sendRedirect(finalUrl);
        } else {
            response.sendRedirect("/");
        }
    }

    private String sanitizeInput(String input) {
        // Basic input sanitization: Remove unwanted characters
        return input.replaceAll("[<>\"'{}|\\\\]", "");
    }

    private String validateAndConstructUrl(String target) {
        try {
            URI uri = new URI(target);
            // Ensure the scheme is either http or https
            if (!"http".equalsIgnoreCase(uri.getScheme()) && !"https".equalsIgnoreCase(uri.getScheme())) {
                return null;
            }

            // Check if the target matches the regular expression
            if (target.matches(REGEX)) {
                return uri.toString();
            }
        } catch (URISyntaxException e) {
            // Invalid URI syntax
        }
        return null;
    }
}
