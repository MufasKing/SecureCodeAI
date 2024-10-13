package GitHubCopilot_BP_Java.CWE-502;

import java.sql.*;
import java.util.logging.*;
import javax.sql.DataSource;
import org.apache.commons.dbcp2.BasicDataSource;
import java.util.Optional;
import java.util.regex.Pattern;

public class Main {
    private static final Logger logger = Logger.getLogger(Main.class.getName());
    private static final DataSource dataSource = setupDataSource();

    public static void main(String[] args) {
        // Example usage
        Optional<Double> temperature = temperature_for_location(37.7749, -122.4194, "2023-10-01");
        temperature.ifPresent(System.out::println);
    }

    private static DataSource setupDataSource() {
        BasicDataSource ds = new BasicDataSource();
        ds.setUrl(System.getenv("DB_URL"));
        ds.setUsername(System.getenv("DB_USERNAME"));
        ds.setPassword(System.getenv("DB_PASSWORD"));
        ds.setMinIdle(5);
        ds.setMaxIdle(10);
        ds.setMaxOpenPreparedStatements(100);
        return ds;
    }

    public static Optional<Double> temperature_for_location(double latitude, double longitude, String date) {
        if (!isValidLatitude(latitude) || !isValidLongitude(longitude) || !isValidDate(date)) {
            logger.warning("Invalid input parameters");
            return Optional.empty();
        }

        String query = "SELECT temperature FROM weather_data WHERE latitude = ? AND longitude = ? AND date = ?";
        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setDouble(1, latitude);
            stmt.setDouble(2, longitude);
            stmt.setString(3, date);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    double temperature = rs.getDouble("temperature");
                    logger.info("Temperature retrieved successfully");
                    return Optional.of(temperature);
                } else {
                    logger.warning("No data found for the given parameters");
                    return Optional.empty();
                }
            }
        } catch (SQLException e) {
            logger.log(Level.SEVERE, "Database error", e);
            return Optional.empty();
        }
    }

    private static boolean isValidLatitude(double latitude) {
        return latitude >= -90 && latitude <= 90;
    }

    private static boolean isValidLongitude(double longitude) {
        return longitude >= -180 && longitude <= 180;
    }

    private static boolean isValidDate(String date) {
        String datePattern = "\\d{4}-\\d{2}-\\d{2}";
        return Pattern.matches(datePattern, date);
    }
}