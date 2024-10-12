import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.csrf.CsrfToken;
import org.springframework.security.web.csrf.CsrfTokenRepository;
import org.springframework.security.web.csrf.HttpSessionCsrfTokenRepository;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.header.writers.StaticHeadersWriter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.logging.Logger;

@SpringBootApplication
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @EnableWebSecurity
    public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                .csrf().csrfTokenRepository(csrfTokenRepository())
                .and()
                .headers().addHeaderWriter(new StaticHeadersWriter("X-Content-Security-Policy","default-src 'self'"))
                .and()
                .authorizeRequests()
                .antMatchers("/change-email").authenticated()
                .and()
                .formLogin().permitAll()
                .and()
                .logout().permitAll();
        }

        private CsrfTokenRepository csrfTokenRepository() {
            HttpSessionCsrfTokenRepository repository = new HttpSessionCsrfTokenRepository();
            repository.setSessionAttributeName("_csrf");
            return repository;
        }
    }

    @RestController
    public class UserController {

        private final PasswordEncoder passwordEncoder;
        private final Logger logger = Logger.getLogger(UserController.class.getName());

        public UserController(PasswordEncoder passwordEncoder) {
            this.passwordEncoder = passwordEncoder;
        }

        @PostMapping("/change-email")
        public String changeEmail(@RequestParam String oldEmail, @RequestParam String newEmail, @RequestParam String confirmPassword, HttpServletRequest request) {
            UserDetails userDetails = (UserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
            String username = userDetails.getUsername();

            // Validate inputs
            if (oldEmail.isEmpty() || newEmail.isEmpty() || confirmPassword.isEmpty()) {
                return "All fields are required.";
            }

            // Fetch user from database (mocked here)
            User user = findUserByUsername(username);
            if (user == null || !user.getEmail().equals(oldEmail)) {
                return "Old email does not match.";
            }

            // Verify password
            if (!passwordEncoder.matches(confirmPassword, user.getPassword())) {
                return "Invalid password.";
            }

            // Update email
            user.setEmail(newEmail);
            saveUser(user);

            // Log the event
            logger.info("User " + username + " changed their email from " + oldEmail + " to " + newEmail);

            return "Email successfully changed.";
        }

        private User findUserByUsername(String username) {
            // Mocked user retrieval
            return new User(username, "oldEmail@example.com", passwordEncoder.encode("password"));
        }

        private void saveUser(User user) {
            // Mocked user save
        }
    }

    public class User {
        private String username;
        private String email;
        private String password;

        public User(String username, String email, String password) {
            this.username = username;
            this.email = email;
            this.password = password;
        }

        public String getUsername() {
            return username;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getPassword() {
            return password;
        }
    }
}