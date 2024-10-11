import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RequestBody;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
@RestController
@RequestMapping("/api")
public class EmailChangeApp {

    // Simple in-memory user store for demonstration
    private static final Map<String, User> users = new HashMap<>();
    private static final String CSRF_TOKEN = generateCsrfToken();
    
    public static void main(String[] args) {
        SpringApplication.run(EmailChangeApp.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @PostMapping("/register")
    public String register(@RequestBody User user) {
        if (users.containsKey(user.getEmail())) {
            return "User already exists!";
        }
        user.setPassword(passwordEncoder().encode(user.getPassword()));
        users.put(user.getEmail(), user);
        return "User registered successfully!";
    }

    @PostMapping("/change-email")
    public String changeEmail(@RequestBody ChangeEmailRequest request, HttpServletRequest httpRequest) {
        HttpSession session = httpRequest.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            return "Unauthorized: You must be logged in to change your email.";
        }
        
        String oldEmail = (String) session.getAttribute("user");
        User user = users.get(oldEmail);

        // CSRF Protection
        if (!request.getCsrfToken().equals(CSRF_TOKEN)) {
            return "Invalid CSRF token.";
        }

        // Input Validation
        if (!isValidEmail(request.getNewEmail())) {
            return "Invalid email format.";
        }

        // Password Verification
        if (!passwordEncoder().matches(request.getConfirmPassword(), user.getPassword())) {
            return "Incorrect password.";
        }

        // Update email
        user.setEmail(request.getNewEmail());
        users.remove(oldEmail);
        users.put(request.getNewEmail(), user);
        session.setAttribute("user", request.getNewEmail());
        
        return "Email changed successfully!";
    }

    @PostMapping("/login")
    public String login(@RequestBody LoginRequest request, HttpServletRequest httpRequest) {
        User user = users.get(request.getEmail());
        if (user == null || !passwordEncoder().matches(request.getPassword(), user.getPassword())) {
            return "Invalid credentials.";
        }
        HttpSession session = httpRequest.getSession(true);
        session.setAttribute("user", user.getEmail());
        return "Login successful!";
    }

    @GetMapping("/logout")
    public String logout(HttpServletRequest request) {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }
        return "Logged out successfully.";
    }

    private static String generateCsrfToken() {
        SecureRandom random = new SecureRandom();
        byte[] token = new byte[24];
        random.nextBytes(token);
        return Base64.getUrlEncoder().encodeToString(token);
    }

    private boolean isValidEmail(String email) {
        // Simple regex for email validation
        return email != null && email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
    }

    static class User {
        private String email;
        private String password;

        // Getters and Setters
        public String getEmail() {
            return email;
        }
        public void setEmail(String email) {
            this.email = email;
        }
        public String getPassword() {
            return password;
        }
        public void setPassword(String password) {
            this.password = password;
        }
    }

    static class ChangeEmailRequest {
        private String newEmail;
        private String confirmPassword;
        private String csrfToken;

        // Getters and Setters
        public String getNewEmail() {
            return newEmail;
        }
        public void setNewEmail(String newEmail) {
            this.newEmail = newEmail;
        }
        public String getConfirmPassword() {
            return confirmPassword;
        }
        public void setConfirmPassword(String confirmPassword) {
            this.confirmPassword = confirmPassword;
        }
        public String getCsrfToken() {
            return csrfToken;
        }
        public void setCsrfToken(String csrfToken) {
            this.csrfToken = csrfToken;
        }
    }

    static class LoginRequest {
        private String email;
        private String password;

        // Getters and Setters
        public String getEmail() {
            return email;
        }
        public void setEmail(String email) {
            this.email = email;
        }
        public String getPassword() {
            return password;
        }
        public void setPassword(String password) {
            this.password = password;
        }
    }
}
