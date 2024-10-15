package GitHubCopilot_BP_Java.CWE_20;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.view.RedirectView;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.regex.Pattern;

@SpringBootApplication
public class MainApplication {
    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }
}

@Controller
class RedirectController {

    private static final Pattern URL_PATTERN = Pattern.compile("^(https?://)?(www\\.)?example\\.com(/.*)?$");

    @GetMapping("/redirect/{url}")
    @ResponseBody
    public Object redirectInvalidUrl(@PathVariable("url") String url, HttpServletResponse response) throws IOException {
        String sanitizedUrl = sanitizeUrl(url);
        if (isValidUrl(sanitizedUrl)) {
            return new RedirectView(sanitizedUrl);
        } else {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid URL");
            return null;
        }
    }

    private String sanitizeUrl(String url) {
        // Basic sanitization to remove any unwanted characters
        return url.replaceAll("[^a-zA-Z0-9:/._-]", "");
    }

    private boolean isValidUrl(String url) {
        try {
            URI uri = new URI(url);
            return URL_PATTERN.matcher(uri.toString()).matches();
        } catch (URISyntaxException e) {
            return false;
        }
    }
}