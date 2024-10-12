import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class WebApp {

    public static void main(String[] args) {
        SpringApplication.run(WebApp.class, args);
    }
}

@RestController
class ApiController {

    @GetMapping("/api")
    public ResponseEntity<Map<String, String>> getPayload(@RequestParam(required = false) String payload) {
        // Input Validation
        if (payload == null || payload.isEmpty()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body(createErrorResponse("Payload parameter is missing or empty."));
        }

        // Load payload into a dictionary (Map)
        Map<String, String> dictionary = parsePayload(payload);

        // Return the name value if it exists
        if (dictionary.containsKey("name")) {
            Map<String, String> response = new HashMap<>();
            response.put("name", dictionary.get("name"));
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body(createErrorResponse("Name not found in the payload."));
        }
    }

    private Map<String, String> parsePayload(String payload) {
        Map<String, String> dictionary = new HashMap<>();
        String[] keyValuePairs = payload.split("&");

        for (String pair : keyValuePairs) {
            String[] entry = pair.split("=");
            if (entry.length == 2) {
                String key = decode(entry[0]);
                String value = decode(entry[1]);
                dictionary.put(key, value);
            }
        }
        return dictionary;
    }

    private String decode(String value) {
        return value.replace("+", " ").replace("%20", " "); // Simple decoding for URL parameters
    }

    private Map<String, String> createErrorResponse(String message) {
        Map<String, String> errorResponse = new HashMap<>();
        errorResponse.put("error", message);
        return errorResponse;
    }
}
