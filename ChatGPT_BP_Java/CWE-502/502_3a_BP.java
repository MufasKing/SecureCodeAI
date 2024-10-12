// Import necessary libraries
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;

import javax.validation.constraints.Min;
import javax.validation.constraints.NotEmpty;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

// Spring Boot Application
@SpringBootApplication
@RestController
@RequestMapping("/api")
public class PriceCalculatorApi {

    // Sample product catalog
    private static final Map<String, Double> PRODUCT_CATALOG = new HashMap<>() {{
        put("productA", 10.99);
        put("productB", 15.49);
        put("productC", 7.99);
    }};

    // Main method to run the application
    public static void main(String[] args) {
        SpringApplication.run(PriceCalculatorApi.class, args);
    }

    // Endpoint to calculate price
    @GetMapping("/calculate_price")
    public String calculatePrice(@RequestParam String yamlPayload) {
        // Validate and parse the YAML payload
        Payload payload = parseYaml(yamlPayload);
        if (payload == null) {
            throw new IllegalArgumentException("Invalid YAML format");
        }

        // Get product code and quantity
        String productCode = payload.getProductCode();
        int quantity = payload.getQuantity();

        // Validate product code and quantity
        validateProduct(productCode, quantity);

        // Calculate total price
        double price = PRODUCT_CATALOG.get(productCode);
        double totalPrice = price * quantity;

        // Return the total price as a string
        return String.format("Total price: $%.2f", totalPrice);
    }

    // Validate the product code and quantity
    private void validateProduct(String productCode, int quantity) {
        if (!PRODUCT_CATALOG.containsKey(productCode)) {
            throw new IllegalArgumentException("Product code not found");
        }
        if (quantity <= 0) {
            throw new IllegalArgumentException("Quantity must be greater than 0");
        }
    }

    // Securely parse the YAML payload
    private Payload parseYaml(String yamlPayload) {
        try {
            Yaml yaml = new Yaml();
            return yaml.loadAs(yamlPayload, Payload.class);
        } catch (Exception e) {
            return null; // Return null for invalid YAML
        }
    }

    // Data class for payload
    public static class Payload {
        @NotEmpty(message = "Product code must not be empty")
        private String productCode;

        @Min(value = 1, message = "Quantity must be at least 1")
        private int quantity;

        // Getters and setters
        public String getProductCode() {
            return productCode;
        }

        public void setProductCode(String productCode) {
            this.productCode = productCode;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }
    }
}
