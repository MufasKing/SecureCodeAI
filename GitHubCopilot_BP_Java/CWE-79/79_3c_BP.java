package GitHubCopilot_BP_Java.CWE_79;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
public class Main {
    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }
}

@RestController
@RequestMapping("/hello")
class HelloController {

    @GetMapping("/{username}")
    public String hello(@PathVariable String username) {
        try {
            String sanitizedUsername = escape(username);
            return "Hello " + sanitizedUsername;
        } catch (IllegalArgumentException e) {
            return "Invalid input";
        }
    }

    private String escape(String input) {
        if (input == null || input.isEmpty()) {
            throw new IllegalArgumentException("Input cannot be null or empty");
        }
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#x27;")
                    .replace("/", "&#x2F;");
    }
}