package com.example.webapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import javax.servlet.http.HttpSession;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;

@SpringBootApplication
public class WebAppApplication {

    public static void main(String[] args) {
        SpringApplication.run(WebAppApplication.class, args);
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
            .anyRequest().authenticated()
            .and()
            .formLogin().permitAll()
            .and()
            .logout().permitAll();
        return http.build();
    }
}

@Controller
class InfoController {

    // Mock user details; in a real application, this should come from a secure database.
    private static class User {
        String username;
        @Email
        String email;
        String ssn; // This would be sensitive data

        User(String username, String email, String ssn) {
            this.username = username;
            this.email = email;
            this.ssn = ssn;
        }
    }

    @GetMapping("/info")
    public String info(HttpSession session, Model model) {
        // Retrieve user information from the session
        User user = (User) session.getAttribute("user");
        if (user == null) {
            return "redirect:/login"; // Redirect to login if not authenticated
        }

        // Escape user input to prevent XSS attacks
        String username = escapeHtml(user.username);
        String email = escapeHtml(user.email);
        String ssnMasked = maskSsn(user.ssn);

        model.addAttribute("username", username);
        model.addAttribute("email", email);
        model.addAttribute("ssn", ssnMasked);
        return "info"; // Return the view name
    }

    private String escapeHtml(String input) {
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#39;");
    }

    private String maskSsn(String ssn) {
        return "XXX-XX-" + ssn.substring(ssn.length() - 4); // Mask all but last four digits
    }
}
