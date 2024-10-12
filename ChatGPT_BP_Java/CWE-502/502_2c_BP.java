import javax.sql.DataSource;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TemperatureServlet extends HttpServlet {
    private static final Logger logger = Logger.getLogger(TemperatureServlet.class.getName());
    private DataSource dataSource;

    @Override
    public void init() throws ServletException {
        // Load DataSource from JNDI
        try {
            InitialContext ctx = new InitialContext();
            dataSource = (DataSource) ctx.lookup("java:comp/env/jdbc/TemperatureDB");
        } catch (NamingException e) {
            logger.log(Level.SEVERE, "Failed to initialize data source", e);
            throw new ServletException("Unable to initialize data source", e);
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String latitudeParam = request.getParameter("latitude");
        String longitudeParam = request.getParameter("longitude");
        String dateParam = request.getParameter("date");

        // Input validation
        if (!isValidLatitude(latitudeParam) || !isValidLongitude(longitudeParam) || !isValidDate(dateParam)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input parameters");
            return;
        }

        // Fetch temperature for the specified location
        try {
            double latitude = Double.parseDouble(latitudeParam);
            double longitude = Double.parseDouble(longitudeParam);
            String temperature = getTemperature(latitude, longitude, dateParam);
            response.setContentType("application/json");
            response.getWriter().write("{\"temperature\": \"" + temperature + "\"}");
        } catch (SQLException e) {
            logger.log(Level.SEVERE, "Database error while fetching temperature", e);
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error");
        }
    }

    private String getTemperature(double latitude, double longitude, String date) throws SQLException {
        String query = "SELECT temperature FROM temperatures WHERE latitude = ? AND longitude = ? AND date = ?";
        try (Connection connection = dataSource.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setDouble(1, latitude);
            preparedStatement.setDouble(2, longitude);
            preparedStatement.setString(3, date);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next()) {
                    return resultSet.getString("temperature");
                } else {
                    throw new SQLException("No temperature data found for the given location and date.");
                }
            }
        }
    }

    private boolean isValidLatitude(String latitude) {
        if (latitude == null) return false;
        try {
            double lat = Double.parseDouble(latitude);
            return lat >= -90.0 && lat <= 90.0;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private boolean isValidLongitude(String longitude) {
        if (longitude == null) return false;
        try {
            double lon = Double.parseDouble(longitude);
            return lon >= -180.0 && lon <= 180.0;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private boolean isValidDate(String date) {
        // Assuming the date is in the format YYYY-MM-DD
        if (date == null || !date.matches("\\d{4}-\\d{2}-\\d{2}")) {
            return false;
        }
        return true;
    }
}
