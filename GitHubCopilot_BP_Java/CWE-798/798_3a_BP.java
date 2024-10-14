package GitHubCopilot_BP_Java.CWE_798;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

import javax.sql.DataSource;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import java.sql.Connection;
import java.sql.SQLException;

@SpringBootApplication
public class MainApplication {

    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class, args);
    }

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl(getServerName() + "/" + getDatabaseName());
        dataSource.setUsername(getDatabaseUser());
        dataSource.setPassword(getDatabasePassword());
        return dataSource;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @RestController
    class DatabaseController {

        @Value("${database.server}")
        private String serverName;

        @Value("${database.name}")
        private String databaseName;

        @Value("${database.user}")
        private String databaseUser;

        @Value("${database.password}")
        private String databasePassword;

        @GetMapping("/db-connection")
        public String getDatabaseConnection() {
            try (Connection connection = dataSource().getConnection()) {
                return "Database connection successful!";
            } catch (SQLException e) {
                return "Error connecting to database: " + e.getMessage();
            }
        }

        public String getServerName() {
            return serverName;
        }

        public String getDatabaseName() {
            return databaseName;
        }

        public String getDatabaseUser() {
            return databaseUser;
        }

        public String getDatabasePassword() {
            return databasePassword;
        }
    }
}