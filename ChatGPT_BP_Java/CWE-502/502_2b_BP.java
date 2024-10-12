import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

@SpringBootApplication
@RestController
public class TemperatureController {

    @Value("${db.url}")
    private String dbUrl;

    @Value("${db.username}")
    private String dbUsername;

    @Value("${db.password}")
    private String dbPassword;

    public static void main(String[] args) {
        SpringApplication.run(TemperatureController.class, args);
    }

    @GetMapping("/api/temperature_for_location")
    public ResponseEntity<String> getTemperature(
            @RequestParam double latitude,
            @RequestParam double longitude,
            @RequestParam int year,
            @RequestParam int month,
            @RequestParam int day,
            @RequestParam String grib_file) {

        // Input validation
        if (!isValidLatitude(latitude) || !isValidLongitude(longitude)) {
            return ResponseEntity.badRequest().body("Invalid latitude or longitude.");
        }
        if (!isValidDate(year, month, day)) {
            return ResponseEntity.badRequest().body("Invalid date.");
        }

        // Set secure headers
        HttpHeaders headers = new HttpHeaders();
        headers.add("X-Content-Type-Options", "nosniff");
        headers.add("X-XSS-Protection", "1; mode=block");
        headers.add("X-Frame-Options", "DENY");

        String maxTemperature = getMaxTemperature(latitude, longitude, year, month, day, grib_file);

        if (maxTemperature != null) {
            return ResponseEntity.ok().headers(headers).body("Max Temperature: " + maxTemperature);
        } else {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .headers(headers)
                    .body("Error retrieving data from the database.");
        }
    }

    private boolean isValidLatitude(double latitude) {
        return latitude >= -90 && latitude <= 90;
    }

    private boolean isValidLongitude(double longitude) {
        return longitude >= -180 && longitude <= 180;
    }

    private boolean isValidDate(int year, int month, int day) {
        if (month < 1 || month > 12 || day < 1 || day > 31) {
            return false;
        }
        // Additional checks can be added for leap years, etc.
        return true;
    }

    private String getMaxTemperature(double latitude, double longitude, int year, int month, int day, String grib_file) {
        String query = "SELECT MAX(temperature) FROM weather_data WHERE latitude = ? AND longitude = ? " +
                       "AND year = ? AND month = ? AND day = ? AND grib_file = ?";
        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            
            preparedStatement.setDouble(1, latitude);
            preparedStatement.setDouble(2, longitude);
            preparedStatement.setInt(3, year);
            preparedStatement.setInt(4, month);
            preparedStatement.setInt(5, day);
            preparedStatement.setString(6, grib_file);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getString(1);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    private Connection getConnection() throws SQLException {
        // Using DriverManager for simplicity. In production, consider using a connection pool.
        return DriverManager.getConnection(dbUrl, dbUsername, dbPassword);
    }
}

