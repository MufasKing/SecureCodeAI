import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.util.HashMap;
import java.util.Map;

@RestController
public class AuthController {

    // Simulating a user store
    private Map<String, String> userStore = new HashMap<>();

    // Constructor to initialize some users (in a real application, use a database)
    public AuthController() {
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        userStore.put("user1", encoder.encode("password123")); // example user
    }

    @GetMapping("/check_mod")
    public String check_mod(@RequestParam String username, @RequestParam String password) {
        // Input Validation
        if (!isValidInput(username) || !isValidInput(password)) {
            return "false"; // or return an appropriate error message
        }

        // User Existence Check
        if (!userStore.containsKey(username)) {
            return "false"; // User does not exist
        }

        // Password Hashing and Verification
        String storedHash = userStore.get(username);
        boolean passwordMatch = constantTimeCompare(storedHash, password);
        
        return passwordMatch ? "true" : "false";
    }

    private boolean isValidInput(String input) {
        // Basic input validation (you can extend this with regex or other checks)
        return input != null && !input.trim().isEmpty() && input.length() <= 100;
    }

    private boolean constantTimeCompare(String storedHash, String password) {
        // Compare using BCrypt to hash the provided password and then compare in constant time
        return BCrypt.checkpw(password, storedHash);
    }

    private SecretKey generateSecretKey() throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256, new SecureRandom());
        return keyGen.generateKey();
    }
}

