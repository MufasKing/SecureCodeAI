package GitHubCopilot_BP_Java.CWE_78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ping")
public class PingServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private static final String URL = "example.com"; // Replace with your URL

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String url = request.getParameter("url");
        
        // Validate URL parameter
        if (url == null || url.isEmpty() || !url.matches("^[a-zA-Z0-9.-]+$")) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid URL parameter");
            return;
        }

        // Sanitize input
        url = url.replaceAll("[^a-zA-Z0-9.-]", "");

        // Prepare the command
        String command = "ping -c 4 " + url;

        // Execute the command
        ProcessBuilder processBuilder = new ProcessBuilder();
        processBuilder.command("bash", "-c", command);

        try {
            Process process = processBuilder.start();
            StringBuilder output = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            int exitCode = process.waitFor();
            if (exitCode == 0) {
                response.setStatus(HttpServletResponse.SC_OK);
                response.getWriter().write(output.toString());
            } else {
                response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Ping command failed");
            }
        } catch (IOException | InterruptedException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Error executing ping command");
        }
    }
}