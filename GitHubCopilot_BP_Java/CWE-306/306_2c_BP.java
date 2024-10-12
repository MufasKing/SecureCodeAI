import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.csrf.CsrfTokenRepository;
import org.springframework.security.web.csrf.HttpSessionCsrfTokenRepository;
import org.springframework.security.web.csrf.CsrfFilter;
import org.springframework.web.filter.OncePerRequestFilter;
import javax.servlet.FilterChain;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@SpringBootApplication
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder passwordEncoder) {
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(User.withUsername("user").password(passwordEncoder.encode("password")).roles("USER").build());
        manager.createUser(User.withUsername("admin").password(passwordEncoder.encode("admin")).roles("ADMIN").build());
        return manager;
    }

    @Bean
    public WebSecurityConfigurerAdapter webSecurityConfigurerAdapter() {
        return new WebSecurityConfigurerAdapter() {
            @Override
            protected void configure(HttpSecurity http) throws Exception {
                http
                    .csrf().csrfTokenRepository(csrfTokenRepository()).and()
                    .authorizeRequests()
                        .antMatchers("/login", "/").permitAll()
                        .antMatchers("/user_page").hasRole("USER")
                        .antMatchers("/admin_page").hasRole("ADMIN")
                        .anyRequest().authenticated()
                    .and()
                    .formLogin().loginPage("/login").permitAll()
                    .and()
                    .logout().permitAll()
                    .and()
                    .headers().defaultsDisabled().cacheControl().and().contentTypeOptions().and().xssProtection().and().frameOptions().and().httpStrictTransportSecurity();
            }

            private CsrfTokenRepository csrfTokenRepository() {
                HttpSessionCsrfTokenRepository repository = new HttpSessionCsrfTokenRepository();
                repository.setHeaderName("X-CSRF-TOKEN");
                return repository;
            }
        };
    }
}

@RestController
public class MainController {

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @PostMapping("/do_login")
    public String doLogin(@RequestParam String username, @RequestParam String password) {
        // Perform login logic, validate input, hash password, manage session
        return "redirect:/";
    }

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/user_page")
    public String userPage() {
        return "user_page";
    }

    @GetMapping("/admin_page")
    public String adminPage() {
        return "admin_page";
    }
}