import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;

import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

@SpringBootApplication
@RestController
@RequestMapping("/api")
public class PriceCalculatorService {

    private static final Logger logger = Logger.getLogger(PriceCalculatorService.class.getName());

    // Simulated product prices
    private static final Map<String, Double> productPrices = new HashMap<>();

    static {
        productPrices.put("A001", 10.0);
        productPrices.put("A002", 15.5);
        productPrices.put("A003", 7.25);
        productPrices.put("A004", 20.0);
    }

    public static void main(String[] args) {
        SpringApplication.run(PriceCalculatorService.class, args);
    }

    @GetMapping("/calculate_price")
    public ResponseEntity<String> calculatePrice(@RequestParam String payload) {
        try {
            Yaml yaml = new Yaml();
            Map<String, Object> input = yaml.load(payload);

            // Input validation
            if (!input.containsKey("product_code") || !input.containsKey("quantity")) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                        .body("Invalid input: product_code and quantity are required");
            }

            String productCode = sanitizeInput(input.get("product_code").toString());
            int quantity;

            try {
                quantity = Integer.parseInt(input.get("quantity").toString());
                if (quantity <= 0) {
                    return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                            .body("Invalid quantity: must be greater than zero");
                }
            } catch (NumberFormatException e) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                        .body("Invalid quantity: must be a number");
            }

            // Calculate total price
            double price = getPriceForProductCode(productCode);
            if (price == -1) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND)
                        .body("Product code not found");
            }

            double totalPrice = price * quantity;

            // Logging the request and response
            logger.info("Calculated total price for product: " + productCode + ", quantity: " + quantity + ", total price: " + totalPrice);

            // Constructing the YAML response
            Map<String, Object> response = new HashMap<>();
            response.put("total_price", totalPrice);

            return ResponseEntity.ok(yaml.dump(response));

        } catch (Exception e) {
            logger.severe("Error processing request: " + e.getMessage());
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Internal server error");
        }
    }

    private double getPriceForProductCode(String productCode) {
        return productPrices.getOrDefault(productCode, -1.0);
    }

    private String sanitizeInput(String input) {
        return input.trim().replaceAll("[<>]", ""); // Simple sanitization to remove potential XSS
    }
}
