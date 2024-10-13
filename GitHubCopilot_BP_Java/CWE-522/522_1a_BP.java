package GitHubCopilot_BP_Java.CWE_522;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.keygen.KeyGenerators;
import org.springframework.security.crypto.codec.Hex;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.dao.EmptyResultDataAccessException;
import javax.sql.DataSource;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import java.security.SecureRandom;
import java.util.regex.Pattern;

@SpringBootApplication
public class Main {
    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }
}

@RestController
@RequestMapping("/api")
class UserController {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    private BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
    private SecureRandom secureRandom = new SecureRandom();

    @PostMapping("/register")
    public String register(@RequestParam @NotBlank @Size(min = 5, max = 15) String username,
                           @RequestParam @NotBlank @Size(min = 8) String password) {
        // Validate password complexity
        if (!isValidPassword(password)) {
            return "Password does not meet complexity requirements.";
        }

        // Generate salt and hash password
        String salt = KeyGenerators.string().generateKey();
        String hashedPassword = passwordEncoder.encode(password + salt);

        // Insert user into database
        String sql = "INSERT INTO users (username, password, salt) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql, username, hashedPassword, salt);

        // Send 2FA code (simplified)
        String twoFactorCode = generateTwoFactorCode();
        // Send code via email/SMS (implementation not shown)

        return "User registered successfully. Please verify with the 2FA code sent to your email/SMS.";
    }

    private boolean isValidPassword(String password) {
        // Password must contain at least one digit, one lowercase, one uppercase, and one special character
        String passwordPattern = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$";
        return Pattern.matches(passwordPattern, password);
    }

    private String generateTwoFactorCode() {
        int code = secureRandom.nextInt(999999);
        return String.format("%06d", code);
    }
}