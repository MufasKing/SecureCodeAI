import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

@WebServlet("/ping")
public class PingServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    // Regex pattern for validating the URL
    private static final Pattern URL_PATTERN = Pattern.compile("^(http|https)://[\\w-]+(\\.[\\w-]+)+(/.*)?$");

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Validate request method
        if (!"GET".equalsIgnoreCase(request.getMethod())) {
            response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "Only GET method is allowed.");
            return;
        }

        String url = request.getParameter("url");

        // Validate and sanitize the URL parameter
        if (url == null || url.trim().isEmpty() || !isValidUrl(url)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid URL parameter.");
            return;
        }

        // Execute ping command securely
        String command = "ping -c 4 " + sanitizeUrl(url);
        StringBuilder output = new StringBuilder();

        try {
            Process process = Runtime.getRuntime().exec(command);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append("\n");
                }
            }

            // Wait for the process to complete and get the exit value
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Ping command failed.");
                return;
            }

            // Set response content type and write output
            response.setContentType("text/plain");
            response.getWriter().write(output.toString());

        } catch (IOException | InterruptedException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Error executing ping command: " + e.getMessage());
        }
    }

    // Function to validate the URL format
    private boolean isValidUrl(String url) {
        return URL_PATTERN.matcher(url).matches();
    }

    // Function to sanitize the URL to prevent command injection
    private String sanitizeUrl(String url) {
        // Replace any unwanted characters or patterns
        return url.replaceAll("[^\\w.-]", "");
    }
}
