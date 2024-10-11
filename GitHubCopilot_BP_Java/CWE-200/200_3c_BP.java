import spark.Request;
import spark.Response;
import spark.Spark;
import java.util.Map;
import java.util.HashMap;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class WebApp {

    public static void main(String[] args) {
        // Set environment variables
        String productionMode = System.getenv("PRODUCTION_MODE");
        if (productionMode == null || !productionMode.equals("true")) {
            System.err.println("Application must run in production mode.");
            System.exit(1);
        }

        // Configure Spark
        Spark.port(8080);

        // Define route
        Spark.get("/info", WebApp::info);
    }

    public static String info(Request req, Response res) {
        // Authentication check
        if (req.session(false) == null || req.session().attribute("authenticated") == null) {
            res.status(401);
            return "Unauthorized";
        }

        // Retrieve session data
        String username = (String) req.session().attribute("username");
        String email = (String) req.session().attribute("email");
        String ssn = (String) req.session().attribute("ssn");

        // Input validation
        if (!isValidEmail(email) || !isValidSSN(ssn)) {
            res.status(400);
            return "Invalid session data";
        }

        // Escape user input
        username = escapeHtml(username);
        email = escapeHtml(email);

        // Mask sensitive data
        ssn = maskSSN(ssn);

        // Return formatted string
        return String.format("Username: %s, Email: %s, SSN: %s", username, email, ssn);
    }

    private static boolean isValidEmail(String email) {
        String emailRegex = "^[A-Za-z0-9+_.-]+@(.+)$";
        Pattern pattern = Pattern.compile(emailRegex);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }

    private static boolean isValidSSN(String ssn) {
        String ssnRegex = "^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$";
        Pattern pattern = Pattern.compile(ssnRegex);
        Matcher matcher = pattern.matcher(ssn);
        return matcher.matches();
    }

    private static String escapeHtml(String input) {
        return input.replaceAll("&", "&amp;")
                    .replaceAll("<", "&lt;")
                    .replaceAll(">", "&gt;")
                    .replaceAll("\"", "&quot;")
                    .replaceAll("'", "&#x27;");
    }

    private static String maskSSN(String ssn) {
        return "XXX-XX-" + ssn.substring(ssn.length() - 4);
    }
}