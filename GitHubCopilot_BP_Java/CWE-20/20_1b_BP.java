package GitHubCopilot_BP_Java.CWE_20;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.view.RedirectView;

import java.util.regex.Pattern;

@SpringBootApplication
public class MainApplication {
    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }
}

@RestController
class RedirectController {

    private static final Pattern URL_PATTERN = Pattern.compile("^(https?://)?(www\\.)?example\\.com(/.*)?$");

    @GetMapping("/redirect")
    public RedirectView redirect(@RequestParam String target) {
        // Input Sanitization
        target = target.trim();

        // URL Validation
        if (URL_PATTERN.matcher(target).matches()) {
            // Secure Redirect
            return new RedirectView(target);
        } else {
            // Redirect to home if validation fails
            return new RedirectView("/");
        }
    }
}