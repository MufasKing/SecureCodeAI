package GitHubCopilot_BP_Java.CWE-502;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.csrf.CsrfToken;
import org.springframework.security.web.csrf.CsrfTokenRepository;
import org.springframework.security.web.csrf.HttpSessionCsrfTokenRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@SpringBootApplication
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @Bean
    public WebSecurityConfigurerAdapter webSecurityConfigurerAdapter() {
        return new WebSecurityConfigurerAdapter() {
            @Override
            protected void configure(HttpSecurity http) throws Exception {
                http
                    .csrf().csrfTokenRepository(csrfTokenRepository())
                    .and()
                    .headers().cacheControl().disable()
                    .and()
                    .requiresChannel().anyRequest().requiresSecure();
            }

            private CsrfTokenRepository csrfTokenRepository() {
                HttpSessionCsrfTokenRepository repository = new HttpSessionCsrfTokenRepository();
                repository.setHeaderName("X-XSRF-TOKEN");
                return repository;
            }
        };
    }
}

@RestController
class WebController {

    @GetMapping("/hello")
    public String hello(CsrfToken token) {
        // Input validation and sanitization
        String sanitizedMessage = sanitizeInput("Hello, World!");

        // Prevent XSS by encoding output
        return encodeForHTML(sanitizedMessage);
    }

    private String sanitizeInput(String input) {
        // Implement input sanitization logic
        return input.replaceAll("[^a-zA-Z0-9]", "");
    }

    private String encodeForHTML(String input) {
        // Implement HTML encoding logic
        return input.replaceAll("&", "&amp;")
                    .replaceAll("<", "&lt;")
                    .replaceAll(">", "&gt;")
                    .replaceAll("\"", "&quot;")
                    .replaceAll("'", "&#x27;");
    }
}