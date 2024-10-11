import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Logger;

@SpringBootApplication
public class SecurityApplication {

    public static void main(String[] args) {
        SpringApplication.run(SecurityApplication.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

@EnableWebSecurity
class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().and()
            .authorizeRequests()
            .antMatchers("/", "/login", "/do_login").permitAll()
            .antMatchers("/admin_page").hasRole("ADMIN") // Access control
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .loginPage("/login")
            .permitAll()
            .and()
            .logout()
            .permitAll()
            .and()
            .headers()
            .contentSecurityPolicy("default-src 'self'"); // Security headers
    }
}

@RestController
@RequestMapping
class LoginController {

    private static final Logger logger = Logger.getLogger(LoginController.class.getName());
    private final Map<String, String> userDatabase = new HashMap<>();
    private final Map<String, Integer> loginAttempts = new ConcurrentHashMap<>();

    public LoginController(PasswordEncoder passwordEncoder) {
        // Simulated database with two users
        String username = "user";
        String password = passwordEncoder.encode("userpassword");
        userDatabase.put(username, password);
        
        String adminUsername = "admin";
        String adminPassword = passwordEncoder.encode("adminpassword");
        userDatabase.put(adminUsername, adminPassword);
    }

    @GetMapping("/")
    public ModelAndView index() {
        return new ModelAndView("index");
    }

    @GetMapping("/login")
    public ModelAndView login() {
        return new ModelAndView("login");
    }

    @PostMapping("/do_login")
    public ModelAndView doLogin(@RequestParam String username, @RequestParam String password,
                                 HttpServletRequest request) {
        // Rate limiting: restrict login attempts
        int attempts = loginAttempts.getOrDefault(username, 0);
        if (attempts >= 5) {
            logger.warning("Too many login attempts for user: " + username);
            return new ModelAndView("error").addObject("message", "Too many login attempts. Try again later.");
        }

        if (userDatabase.containsKey(username)) {
            String storedPassword = userDatabase.get(username);
            PasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

            if (passwordEncoder.matches(password, storedPassword)) {
                HttpSession session = request.getSession();
                session.setAttribute("username", username);
                loginAttempts.remove(username); // Reset attempts on successful login
                logger.info("User " + username + " logged in successfully.");
                return new ModelAndView("redirect:/user_page");
            } else {
                loginAttempts.put(username, attempts + 1);
                logger.warning("Failed login attempt for user: " + username);
                return new ModelAndView("login").addObject("error", "Invalid username or password.");
            }
        }
        return new ModelAndView("login").addObject("error", "Invalid username or password.");
    }

    @GetMapping("/user_page")
    public ModelAndView userPage(HttpSession session) {
        String username = (String) session.getAttribute("username");
        if (username != null) {
            logger.info("User " + username + " accessed user page.");
            return new ModelAndView("user_page").addObject("username", username);
        }
        logger.warning("Unauthorized access attempt to user page.");
        return new ModelAndView("login").addObject("error", "Please log in first.");
    }

    @GetMapping("/admin_page")
    public ModelAndView adminPage(HttpSession session) {
        String username = (String) session.getAttribute("username");
        if (username != null && username.equals("admin")) {
            logger.info("Admin " + username + " accessed admin page.");
            return new ModelAndView("admin_page").addObject("username", username);
        }
        logger.warning("Unauthorized access attempt to admin page by user: " + username);
        return new ModelAndView("login").addObject("error", "Access denied.");
    }
}
