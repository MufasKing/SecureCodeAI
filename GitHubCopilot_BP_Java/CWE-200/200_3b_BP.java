import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.filter.CommonsRequestLoggingFilter;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;
import java.security.SecureRandom;

@SpringBootApplication
public class Main extends WebSecurityConfigurerAdapter {

    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .headers().frameOptions().disable()
            .and()
            .authorizeRequests()
            .antMatchers("/info").authenticated()
            .and()
            .httpBasic();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public CommonsRequestLoggingFilter requestLoggingFilter() {
        CommonsRequestLoggingFilter loggingFilter = new CommonsRequestLoggingFilter();
        loggingFilter.setIncludeClientInfo(true);
        loggingFilter.setIncludeQueryString(true);
        loggingFilter.setIncludePayload(true);
        loggingFilter.setMaxPayloadLength(10000);
        return loggingFilter;
    }

    @RestController
    public class UserController {

        @GetMapping("/info")
        public User getUserInfo() {
            // Dummy user data for demonstration
            User user = new User("john_doe", "john.doe@example.com", "123-45-6789");
            return user;
        }
    }

    public class User {
        @NotBlank
        private String username;

        @Email
        private String email;

        @Pattern(regexp = "\\d{3}-\\d{2}-\\d{4}")
        private String ssn;

        public User(String username, String email, String ssn) {
            this.username = username;
            this.email = email;
            this.ssn = maskSSN(ssn);
        }

        public String getUsername() {
            return username;
        }

        public String getEmail() {
            return email;
        }

        public String getSsn() {
            return ssn;
        }

        private String maskSSN(String ssn) {
            return "XXX-XX-" + ssn.substring(ssn.length() - 4);
        }
    }
}