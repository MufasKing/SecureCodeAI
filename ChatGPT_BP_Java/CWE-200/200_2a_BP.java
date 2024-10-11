import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.query.Query;
import org.mindrot.jbcrypt.BCrypt;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletResponse;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Pattern;

@Controller
public class LoginController extends WebSecurityConfigurerAdapter {

    // Hibernate session factory setup
    private SessionFactory sessionFactory;

    public LoginController(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @PostMapping("/login")
    public String login(
        @RequestParam("username") 
        @NotEmpty @Pattern(regexp = "^[a-zA-Z0-9_]{3,30}$") String username,
        @RequestParam("password") @NotEmpty String password,
        HttpServletResponse response) {

        // Validate input
        if (username == null || password == null) {
            return "redirect:/cant_login";
        }

        // Begin Hibernate session
        Session session = null;
        Transaction tx = null;
        try {
            session = sessionFactory.openSession();
            tx = session.beginTransaction();

            // Query to get user details
            Query query = session.createQuery("FROM User WHERE username = :username");
            query.setParameter("username", username);
            User user = (User) query.uniqueResult();

            // If user exists, validate password
            if (user != null && BCrypt.checkpw(password, user.getPasswordHash())) {
                // Success: Redirect to success page
                return "redirect:/success";
            } else {
                // Invalid credentials: Redirect to failure page
                return "redirect:/cant_login";
            }
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
            return "redirect:/internal_server_error";
        } finally {
            if (session != null) session.close();
        }
    }

    // Password hashing method (uses BCrypt)
    private String hashPassword(String plainTextPassword) {
        return BCrypt.hashpw(plainTextPassword, BCrypt.gensalt(12));
    }

    // Security configuration for HTTPS, CSRF, and Content Security Policy (CSP)
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf() // Enable CSRF protection
            .and()
            .headers()
            .contentSecurityPolicy("default-src 'self'; script-src 'self'; object-src 'none'; style-src 'self';")
            .and()
            .requiresChannel() // Enforce HTTPS
            .anyRequest().requiresSecure()
            .and()
            .authorizeRequests()
            .antMatchers("/login").permitAll()
            .anyRequest().authenticated();
    }
}

// Hibernate User entity mapping
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String passwordHash;

    // Getters and Setters
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }
}
