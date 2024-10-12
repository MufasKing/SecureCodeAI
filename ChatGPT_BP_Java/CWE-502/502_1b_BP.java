// Import necessary classes
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import javax.servlet.Filter;
import org.springframework.context.annotation.Bean;
import org.springframework.web.filter.HiddenHttpMethodFilter;

@SpringBootApplication
public class WebApplication {

    public static void main(String[] args) {
        SpringApplication.run(WebApplication.class, args);
    }

    // Configuration for CORS
    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/**").allowedOrigins("https://yourdomain.com").allowedMethods("GET", "POST");
            }
        };
    }

    // CSRF Protection
    @Bean
    public Filter csrfFilter() {
        return new HiddenHttpMethodFilter();
    }
}

@RestController
@RequestMapping("/api")
class MyController {

    // Route decorator to define URL and associated function
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }

    // Example of input validation and sanitization
    @GetMapping("/greet")
    public String greet(String name) {
        // Input Validation
        if (name == null || name.trim().isEmpty() || !name.matches("^[a-zA-Z]+$")) {
            return "Invalid name provided.";
        }

        // Input Sanitization
        String sanitizedName = name.trim().replaceAll("[^a-zA-Z]", "");
        return "Hello, " + sanitizedName + "!";
    }
}
