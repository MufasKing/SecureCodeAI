import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import java.util.Optional;

@SpringBootApplication
public class TemperatureApiApplication {

    public static void main(String[] args) {
        SpringApplication.run(TemperatureApiApplication.class, args);
    }

    @Bean
    CommandLineRunner initDatabase(TemperatureRepository repository) {
        return args -> {
            // Initialization code can go here if needed.
        };
    }
}

@Entity
@Table(name = "temperatures")
class Temperature {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Double latitude;
    private Double longitude;
    private String date; // Consider using a date type like LocalDate

    @Column(name = "temperature")
    private Double temperature;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Double getLatitude() {
        return latitude;
    }

    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public Double getLongitude() {
        return longitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Double getTemperature() {
        return temperature;
    }

    public void setTemperature(Double temperature) {
        this.temperature = temperature;
    }
}

interface TemperatureRepository extends JpaRepository<Temperature, Long> {
    Optional<Temperature> findByLatitudeAndLongitudeAndDate(Double latitude, Double longitude, String date);
}

@RestController
@RequestMapping("/api")
class TemperatureController {

    @Autowired
    private TemperatureRepository temperatureRepository;

    @GetMapping("/temperature_for_location")
    public ResponseEntity<Double> temperatureForLocation(
            @RequestParam @NotNull Double latitude,
            @RequestParam @NotNull Double longitude,
            @RequestParam @NotNull @Pattern(regexp = "^\\d{4}-\\d{2}-\\d{2}$") String date) {

        return temperatureRepository.findByLatitudeAndLongitudeAndDate(latitude, longitude, date)
                .map(temperature -> ResponseEntity.ok(temperature.getTemperature()))
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Temperature data not found"));
    }
}

@Configuration
class DatabaseConfig {

    @Autowired
    private Environment env;

    @Bean
    public DataSource dataSource() {
        DataSourceBuilder dataSourceBuilder = DataSourceBuilder.create();
        dataSourceBuilder
                .driverClassName(env.getProperty("DB_DRIVER"))
                .url(env.getProperty("DB_URL"))
                .username(env.getProperty("DB_USERNAME"))
                .password(env.getProperty("DB_PASSWORD"));
        return dataSourceBuilder.build();
    }
}
