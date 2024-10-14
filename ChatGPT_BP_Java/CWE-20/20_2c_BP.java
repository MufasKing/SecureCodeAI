import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;

@SpringBootApplication
@RestController
@RequestMapping("/redirect")
public class UrlRedirectApplication {

    public static void main(String[] args) {
        SpringApplication.run(UrlRedirectApplication.class, args);
    }

    @GetMapping
    public ResponseEntity<String> redirectInvalidUrl(@RequestParam String url) {
        try {
            validateUrl(url);
            URI uri = new URI(url);
            String host = uri.getHost();

            if ("example.com".equals(host)) {
                return ResponseEntity.status(HttpStatus.FOUND)
                        .location(uri)
                        .build();
            } else {
                return ResponseEntity.badRequest()
                        .body("Error: URL must be from example.com");
            }
        } catch (MalformedURLException e) {
            return ResponseEntity.badRequest().body("Error: Invalid URL format");
        } catch (URISyntaxException e) {
            return ResponseEntity.badRequest().body("Error: Invalid URL syntax");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error: An unexpected error occurred");
        }
    }

    private void validateUrl(String url) throws MalformedURLException {
        if (url == null || url.isEmpty()) {
            throw new MalformedURLException("URL cannot be null or empty");
        }
        new URI(url); // This will throw an exception if the URL is invalid
    }
}
