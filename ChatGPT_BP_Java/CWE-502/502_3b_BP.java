import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.filter.CommonsRequestLoggingFilter;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
@RestController
@RequestMapping("/api")
public class ProductPriceApp {

    private static final Map<String, Double> productPrices = new HashMap<>();
    private static SecretKey secretKey;

    public static void main(String[] args) {
        generateSecretKey();
        SpringApplication.run(ProductPriceApp.class, args);
    }

    private static void generateSecretKey() {
        try {
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            keyGen.init(256); // Key size
            secretKey = keyGen.generateKey();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error generating secret key", e);
        }
    }

    @GetMapping("/price/{code}")
    public ResponseEntity<Double> getPrice(@PathVariable String code) {
        validateProductCode(code);
        Double price = productPrices.get(code);
        if (price == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);
        }
        return ResponseEntity.ok(price);
    }

    @PostMapping("/calculate")
    public ResponseEntity<Double> calculatePrice(@RequestParam String code, @RequestParam int quantity) {
        validateProductCode(code);
        validateQuantity(quantity);
        Double price = productPrices.get(code);
        if (price == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);
        }
        double totalPrice = price * quantity;
        return ResponseEntity.ok(totalPrice);
    }

    private void validateProductCode(String code) {
        if (code == null || code.isEmpty() || !productPrices.containsKey(code)) {
            throw new IllegalArgumentException("Invalid product code.");
        }
    }

    private void validateQuantity(int quantity) {
        if (quantity <= 0) {
            throw new IllegalArgumentException("Quantity must be greater than zero.");
        }
    }

    // Example data initialization
    static {
        productPrices.put("A001", 29.99);
        productPrices.put("A002", 49.99);
        productPrices.put("A003", 15.99);
    }

    // Error handling
    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<String> handleIllegalArgument(IllegalArgumentException e) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleGenericException(Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("An error occurred: " + e.getMessage());
    }
    
    // Enable security headers
    @Bean
    public CommonsRequestLoggingFilter requestLoggingFilter() {
        CommonsRequestLoggingFilter loggingFilter = new CommonsRequestLoggingFilter();
        loggingFilter.setIncludeClientInfo(true);
        loggingFilter.setIncludeQueryString(true);
        loggingFilter.setIncludePayload(true);
        return loggingFilter;
    }
}
