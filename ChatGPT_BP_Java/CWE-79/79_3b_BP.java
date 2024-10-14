// Import necessary classes
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.web.filter.ForwardedHeaderFilter;

// Main application class
@SpringBootApplication
public class MyApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }

    // Configure security settings
    @Bean
    public WebMvcConfigurer webMvcConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                // Allow only specific origins
                registry.addMapping("/**").allowedOrigins("https://your-allowed-origin.com");
            }
        };
    }
}

// Security configuration
@EnableWebSecurity
class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .headers()
                .contentSecurityPolicy("default-src 'self'; script-src 'self';") // Secure headers
                .and()
            .and()
                .xssProtection() // XSS protection
                .and()
                .frameOptions().deny() // Clickjacking protection
                .and()
                .csrf().disable() // Disable CSRF for simplicity
                .authorizeRequests()
                .anyRequest().permitAll();
    }
}

// REST controller
@RestController
class MyController {

    // Endpoint to handle GET requests
    @GetMapping("/greet")
    public String greet(String name) {
        validateInput(name); // Input validation
        return "Hello, " + escapeHtml(name) + "!"; // Return a greeting
    }

    // Input validation method
    private void validateInput(String input) {
        if (input == null || input.isEmpty() || input.length() > 100) {
            throw new IllegalArgumentException("Invalid input.");
        }
    }

    // Simple XSS prevention method using HTML escaping
    private String escapeHtml(String input) {
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#x27;");
    }
}
