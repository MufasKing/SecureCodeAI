import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.regex.Pattern;

@SpringBootApplication
@RestController
@RequestMapping("/redirect")
public class RedirectApplication {

    private static final String BASE_URL = "example.com";
    private static final Pattern URL_PATTERN = Pattern.compile("^(https?://)?(www\\.)?" + BASE_URL + "(/.*)?$");

    public static void main(String[] args) {
        SpringApplication.run(RedirectApplication.class, args);
    }

    @GetMapping("/{url:.+}")
    public ResponseEntity<String> redirectInvalidUrl(@PathVariable String url) {
        try {
            // Input validation
            if (!isValidUrl(url)) {
                return new ResponseEntity<>("Invalid URL format.", HttpStatus.BAD_REQUEST);
            }

            // Sanitize the URL
            String sanitizedUrl = sanitizeUrl(url);

            // Check if the URL is valid
            if (isFromExample(sanitizedUrl)) {
                // Perform a secure redirect
                return ResponseEntity.status(HttpStatus.FOUND)
                        .location(URI.create(sanitizedUrl))
                        .build();
            } else {
                return new ResponseEntity<>("Error: URL is not from example.com.", HttpStatus.FORBIDDEN);
            }
        } catch (URISyntaxException e) {
            return new ResponseEntity<>("Error: Malformed URL.", HttpStatus.BAD_REQUEST);
        }
    }

    private boolean isValidUrl(String url) {
        return url != null && URL_PATTERN.matcher(url).matches();
    }

    private String sanitizeUrl(String url) {
        return url.trim().replaceAll("[<>]", ""); // Basic sanitization
    }

    private boolean isFromExample(String url) {
        return url != null && URL_PATTERN.matcher(url).matches();
    }
}
