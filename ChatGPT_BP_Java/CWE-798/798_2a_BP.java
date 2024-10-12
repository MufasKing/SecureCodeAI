// MainApplication.java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import javax.annotation.PostConstruct;
import javax.sql.DataSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

@SpringBootApplication
@EnableWebMvc
@EnableWebSecurity
@RestController
@RequestMapping("/api")
public class MainApplication extends WebSecurityConfigurerAdapter {
    private static final Logger logger = LoggerFactory.getLogger(MainApplication.class);

    @Autowired
    private DataSource dataSource;

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @PostConstruct
    public void init() {
        // Initialize your database connection or settings here
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
            .authorizeRequests()
            .antMatchers("/api/secure").authenticated()
            .and()
            .httpBasic(); // Use basic authentication for simplicity
    }

    @GetMapping("/query")
    public String executeQuery(@RequestParam String userInput) {
        // Input validation and sanitization
        if (!isValidInput(userInput)) {
            logger.error("Invalid input: {}", userInput);
            throw new IllegalArgumentException("Invalid input");
        }

        String result = "";
        try (Connection connection = dataSource.getConnection();
             Statement statement = connection.createStatement()) {
            String query = "SELECT * FROM users WHERE username = '" + userInput + "'"; // Avoid SQL injection
            ResultSet resultSet = statement.executeQuery(query);

            while (resultSet.next()) {
                result += resultSet.getString("username") + ", ";
            }
        } catch (Exception e) {
            logger.error("Database error: {}", e.getMessage());
            return "Error executing query";
        }
        return result.isEmpty() ? "No results found" : result;
    }

    private boolean isValidInput(String input) {
        // Perform input validation (e.g., regex checks)
        return input != null && !input.trim().isEmpty() && input.matches("[a-zA-Z0-9]+");
    }

    // Password hashing example (for user registration)
    public String hashPassword(String plainPassword) {
        PasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        return passwordEncoder.encode(plainPassword);
    }

    // Implement other security features and configurations as necessary...
}
