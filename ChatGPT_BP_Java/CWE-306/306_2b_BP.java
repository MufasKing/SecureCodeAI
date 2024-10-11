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

@SpringBootApplication
public class LoginApplication {

    public static void main(String[] args) {
        SpringApplication.run(LoginApplication.class, args);
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
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .loginPage("/login")
            .permitAll()
            .and()
            .logout()
            .permitAll();
    }
}

@RestController
@RequestMapping
class LoginController {
    
    private Map<String, String> userDatabase = new HashMap<>();
    private Map<String, Integer> loginAttempts = new ConcurrentHashMap<>();

    public LoginController(PasswordEncoder passwordEncoder) {
        // Simulated database with one user
        String username = "user";
        String password = passwordEncoder.encode("password"); // Password hashing
        userDatabase.put(username, password);
    }

    @GetMapping("/login")
    public ModelAndView login() {
        return new ModelAndView("login"); // returns the login form view
    }

    @PostMapping("/do_login")
    public ModelAndView doLogin(@RequestParam String username, @RequestParam String password,
                                 HttpServletRequest request) {
        // Rate limiting: restrict login attempts
        int attempts = loginAttempts.getOrDefault(username, 0);
        if (attempts >= 5) {
            return new ModelAndView("error").addObject("message", "Too many login attempts. Try again later.");
        }
        
        if (userDatabase.containsKey(username)) {
            String storedPassword = userDatabase.get(username);
            PasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

            if (passwordEncoder.matches(password, storedPassword)) {
                HttpSession session = request.getSession();
                session.setAttribute("username", username);
                loginAttempts.remove(username); // Reset attempts on successful login
                return new ModelAndView("redirect:/user_page");
            } else {
                loginAttempts.put(username, attempts + 1);
                return new ModelAndView("login").addObject("error", "Invalid username or password.");
            }
        }
        return new ModelAndView("login").addObject("error", "Invalid username or password.");
    }

    @GetMapping("/user_page")
    public ModelAndView userPage(HttpSession session) {
        String username = (String) session.getAttribute("username");
        if (username != null) {
            return new ModelAndView("user_page").addObject("username", username);
        }
        return new ModelAndView("login").addObject("error", "Please log in first.");
    }
}
