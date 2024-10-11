// fw.java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import javax.servlet.http.HttpSession;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Controller
    public class InfoController {

        @GetMapping("/info")
        public String info(HttpSession session, Model model) {
            String username = (String) session.getAttribute("username");
            String email = (String) session.getAttribute("email");
            String ssn = (String) session.getAttribute("ssn");

            if (username == null || email == null || ssn == null) {
                return "redirect:/login";
            }

            model.addAttribute("username", username);
            model.addAttribute("email", email);
            model.addAttribute("ssn", ssn.substring(ssn.length() - 4));

            return "info";
        }
    }

    @Controller
    public class LoginController {

        @GetMapping("/login")
        public String login() {
            return "login";
        }
    }

    @Controller
    public class ErrorController {

        @GetMapping("/error")
        public String error() {
            return "error";
        }
    }

    @Bean
    public WebSecurityConfigurerAdapter webSecurityConfigurerAdapter() {
        return new WebSecurityConfigurerAdapter() {
            @Override
            protected void configure(HttpSecurity http) throws Exception {
                http
                    .authorizeRequests()
                    .antMatchers("/info").authenticated()
                    .anyRequest().permitAll()
                    .and()
                    .formLogin()
                    .loginPage("/login")
                    .defaultSuccessUrl("/info")
                    .and()
                    .logout()
                    .logoutSuccessUrl("/login")
                    .and()
                    .csrf().disable();
            }
        };
    }
}