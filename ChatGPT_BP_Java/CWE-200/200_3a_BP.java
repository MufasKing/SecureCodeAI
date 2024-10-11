import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpSession;

@SpringBootApplication
public class SecureWebApp {

    public static void main(String[] args) {
        SpringApplication.run(SecureWebApp.class, args);
    }

    @RestController
    @RequestMapping("/info")
    public class InfoController {
        
        @GetMapping
        public String info(HttpSession session) {
            // Secure session management
            String username = (String) session.getAttribute("username");
            String email = (String) session.getAttribute("email");
            String ssn = (String) session.getAttribute("ssn");

            // Input validation and sanitization (basic example)
            if (username == null || email == null || ssn == null || ssn.length() != 4) {
                return "Error: Invalid session data.";
            }

            return String.format("Username: %s<br>Email: %s<br>Last 4 SSN: %s", 
                                 escapeHtml(username), escapeHtml(email), escapeHtml(ssn));
        }

        // Method to escape HTML to prevent XSS attacks
        private String escapeHtml(String input) {
            if (input == null) return null;
            return input.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;");
        }
    }

    @EnableWebSecurity
    public class SecurityConfig extends WebSecurityConfigurerAdapter {

        @Override
        protected void configure(HttpSecurity http) throws Exception {
            // Secure transmission
            http
                .requiresChannel()
                .anyRequest()
                .requiresSecure()
                .and()
                .authorizeRequests()
                .anyRequest().authenticated()
                .and()
                .formLogin() // Using form-based authentication
                .permitAll()
                .and()
                .logout()
                .permitAll();
        }

        @Bean
        public PasswordEncoder passwordEncoder() {
            // Password hashing
            return new BCryptPasswordEncoder();
        }
    }
}
