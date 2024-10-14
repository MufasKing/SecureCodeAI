import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/hello/*")
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        String pathInfo = request.getPathInfo();
        
        if (pathInfo == null || pathInfo.length() < 1) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Username is missing");
            return;
        }

        String username = pathInfo.substring(1); // Remove the leading '/'
        username = sanitizeInput(username); // Input sanitization

        if (!isValidUsername(username)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid username");
            return;
        }

        // Call the hello function
        String result = hello(username);
        
        // Set content type and send the response
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println(result);
    }

    // Decorator function to handle the hello request
    private String hello(String username) {
        return renderTemplate("hello.html", username);
    }

    // Method to render the template
    private String renderTemplate(String templateFile, String username) {
        StringBuilder rendered = new StringBuilder();
        rendered.append("<html><body>");
        rendered.append("<h1>Hello, ").append(username).append("!</h1>");
        // Here you can read from hello.html and append its content
        rendered.append("</body></html>");
        return rendered.toString();
    }

    // Input validation for the username
    private boolean isValidUsername(String username) {
        return username.matches("^[a-zA-Z0-9_]{1,20}$"); // Alphanumeric and underscores, 1 to 20 characters
    }

    // Input sanitization method
    private String sanitizeInput(String input) {
        return input.replaceAll("[^a-zA-Z0-9_]", ""); // Allow only alphanumeric characters and underscores
    }
}
