import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = null;
        StringBuilder outputbuf = new StringBuilder();

        try {
            // Securely read the request body
            BufferedReader reader = request.getReader();
            username = reader.readLine();
            
            // Input sanitization and validation
            if (username == null || username.trim().isEmpty() || !username.matches("^[a-zA-Z0-9_]+$")) {
                throw new IllegalArgumentException("Invalid username");
            }

            // Construct the HTML response body
            outputbuf.append("<html>")
                     .append("<head><title>Hello Page</title></head>")
                     .append("<body>")
                     .append("<h1>Hello, ").append(escapeHtml(username)).append("!</h1>")
                     .append("</body>")
                     .append("</html>");

            // Write the response body to the response stream
            response.setContentType("text/html");
            PrintWriter out = response.getWriter();
            out.write(outputbuf.toString());
            out.close();

        } catch (Exception e) {
            // Error handling
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid request");
        }
    }

    // Utility method to escape HTML characters
    private String escapeHtml(String input) {
        if (input == null) {
            return null;
        }
        return input.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\"", "&quot;")
                    .replace("'", "&#x27;");
    }
}