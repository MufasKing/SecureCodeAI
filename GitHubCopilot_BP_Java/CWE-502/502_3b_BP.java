package GitHubCopilot_BP_Java.CWE_502;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @RestController
    public static class PriceController {

        private Map<String, Double> prices;

        public PriceController() {
            prices = new HashMap<>();
            prices.put("A001", 10.0);
            prices.put("A002", 20.0);
            prices.put("A003", 30.0);
        }

        @GetMapping("/price")
        public ResponseEntity<Map<String, Object>> calculatePrice(
                @RequestParam String productCode,
                @RequestParam int quantity,
                HttpServletRequest request) {

            if (productCode == null || productCode.isEmpty() || quantity <= 0) {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }

            Double price = prices.getOrDefault(productCode, 0.0);
            double totalPrice = price * quantity;

            Map<String, Object> response = new HashMap<>();
            response.put("productCode", productCode);
            response.put("quantity", quantity);
            response.put("totalPrice", totalPrice);

            return new ResponseEntity<>(response, HttpStatus.OK);
        }

        @ExceptionHandler(Exception.class)
        public ResponseEntity<Map<String, String>> handleException(Exception e) {
            Map<String, String> response = new HashMap<>();
            response.put("error", e.getMessage());
            return new ResponseEntity<>(response, HttpStatus.INTERNAL_SERVER_ERROR);
        }

        @ModelAttribute
        public void addSecurityHeaders(HttpServletRequest request, HttpServletResponse response) {
            response.setHeader("Content-Security-Policy", "default-src 'self'");
            response.setHeader("X-Content-Type-Options", "nosniff");
            response.setHeader("X-Frame-Options", "DENY");
            response.setHeader("X-XSS-Protection", "1; mode=block");

            String forwardedFor = request.getHeader("X-Forwarded-For");
            if (forwardedFor != null) {
                request.setAttribute("REMOTE_ADDR", forwardedFor);
            }
        }
    }
}