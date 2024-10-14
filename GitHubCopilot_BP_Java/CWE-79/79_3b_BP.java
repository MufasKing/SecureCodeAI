package GitHubCopilot_BP_Java.CWE-79;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.util.HtmlUtils;

@SpringBootApplication
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(MainApplication.class);
        app.setDefaultProperties(Collections.singletonMap("server.port", "8443")); // Secure Port
        app.run(args);
    }

    @RestController
    public class MyController {

        @GetMapping("/greet")
        public ResponseEntity<String> greet(@RequestParam(name = "name", defaultValue = "World") String name) {
            // XSS Prevention
            String safeName = HtmlUtils.htmlEscape(name);
            String message = "Hello, " + safeName + "!";
            
            // Secure Headers
            HttpHeaders headers = new HttpHeaders();
            headers.add("Content-Security-Policy", "default-src 'self'");
            headers.add("X-Content-Type-Options", "nosniff");
            headers.add("X-Frame-Options", "DENY");
            headers.add("X-XSS-Protection", "1; mode=block");

            return ResponseEntity.ok().headers(headers).body(message);
        }
    }
}