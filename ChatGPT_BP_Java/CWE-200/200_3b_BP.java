import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.filter.ForwardedHeaderFilter;

import javax.annotation.PostConstruct;
import javax.servlet.Filter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@SpringBootApplication
public class SecureWebApplication {

    public static void main(String[] args) {
        SpringApplication.run(SecureWebApplication.class, args);
    }

    @Bean
    public Filter forwardedHeaderFilter() {
        return new ForwardedHeaderFilter();
    }

    @PostConstruct
    public void init() {
        // Perform any initialization here if needed
    }
}

@EnableWebSecurity
class SecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication()
            .withUser("user")
            .password(passwordEncoder().encode("password"))
            .roles("USER");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable() // Ideally, enable CSRF
            .authorizeRequests()
                .antMatchers("/info").authenticated()
                .and()
            .httpBasic()
                .and()
            .headers()
                .contentSecurityPolicy("default-src 'self'")
                .and()
            .and()
            .requiresChannel()
                .anyRequest()
                .requiresSecure(); // Ensure HTTPS
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

@RestController
@RequestMapping("/info")
class InfoController {

    @GetMapping
    public String getUserInfo(HttpServletRequest request, HttpServletResponse response) {
        // Simulate fetching user data (username, email, SSN)
        String username = "user"; // Get username from security context
        String email = "user@example.com"; // Get email from user data
        String ssn = "123-45-6789"; // Example SSN

        // Return a simple HTML response
        return "<html><body>" +
               "<h1>User Info</h1>" +
               "<p>Username: " + username + "</p>" +
               "<p>Email: " + email + "</p>" +
               "<p>Last 4 digits of SSN: " + ssn.substring(ssn.length() - 4) + "</p>" +
               "</body></html>";
    }
}
