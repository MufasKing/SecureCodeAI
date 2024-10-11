import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.authentication.LoginUrlAuthenticationEntryPoint;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.config.annotation.EnableWebMvcSecurity;

import javax.servlet.http.HttpSession;

@SpringBootApplication
@RestController
@EnableWebSecurity
public class Application extends WebSecurityConfigurerAdapter {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication()
            .withUser("user").password(passwordEncoder().encode("password")).roles("USER")
            .and()
            .withUser("admin").password(passwordEncoder().encode("admin")).roles("ADMIN");
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().and().authorizeRequests()
            .antMatchers("/admin").hasRole("ADMIN")
            .antMatchers("/user").hasRole("USER")
            .antMatchers("/", "/login").permitAll()
            .anyRequest().authenticated()
            .and()
            .formLogin()
            .loginPage("/login").permitAll()
            .and()
            .logout().permitAll()
            .and()
            .exceptionHandling().authenticationEntryPoint(new LoginUrlAuthenticationEntryPoint("/login"));
    }

    @GetMapping("/")
    public String home(HttpSession session) {
        return "Welcome! Please log in.";
    }

    @GetMapping("/login")
    public String login() {
        return "<form action='/login' method='post'>" +
               "Username: <input type='text' name='username'><br>" +
               "Password: <input type='password' name='password'><br>" +
               "<input type='submit' value='Login'>" +
               "</form>";
    }

    @GetMapping("/user")
    public String userPage() {
        return "Welcome to the user page!";
    }

    @GetMapping("/admin")
    public String adminPage() {
        return "Welcome to the admin page!";
    }

    @PostMapping("/login")
    public String loginPost(@RequestParam String username, @RequestParam String password) {
        // This would normally be handled by Spring Security
        return "Logging in " + username;
    }

    @PostMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "Logged out successfully!";
    }

    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
