// Import necessary packages
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.web.csrf.CsrfToken;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@RestController
@RequestMapping("/")
public class MessageController {

    private final DataSource dataSource;

    @Autowired
    public MessageController(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    // POST route to handle message insertion
    @PostMapping("/post")
    public ResponseEntity<String> postMessage(
            @RequestParam("username") String username,
            @RequestParam("message") String message,
            HttpServletRequest request,
            HttpServletResponse response
    ) {
        // Input validation
        if (username == null || username.isEmpty() || message == null || message.isEmpty()) {
            return ResponseEntity.badRequest().body("Username and message cannot be empty.");
        }

        // Perform input sanitization (simple example; ideally use a library)
        username = username.replaceAll("[^a-zA-Z0-9_]", ""); // Allow only alphanumeric and underscore
        message = message.replaceAll("[^\\p{L}\\p{Z}]", ""); // Allow letters and spaces

        // Call the method to insert the message into the database
        try {
            insertUserMessageInDb(username, message);
        } catch (SQLException e) {
            // Error handling
            return ResponseEntity.internalServerError().body("Database error: " + e.getMessage());
        }

        // Redirect securely to the home route
        response.setHeader("Location", "/");
        response.setStatus(HttpServletResponse.SC_FOUND); // 302 Found

        return ResponseEntity.ok("Message posted successfully");
    }

    // Method to insert user message into the database
    private void insertUserMessageInDb(String username, String message) throws SQLException {
        String sql = "INSERT INTO messages (username, message) VALUES (?, ?)";
        try (Connection connection = dataSource.getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, message);
            preparedStatement.executeUpdate();
        }
    }

    // GET route to display messages
    @GetMapping("/")
    public ModelAndView displayMessages() {
        ModelAndView modelAndView = new ModelAndView("messages");
        // Logic to fetch messages from the database and add them to the model can go here
        // For example: modelAndView.addObject("messages", fetchMessagesFromDb());
        return modelAndView;
    }

    // Placeholder for fetching messages from the database (not implemented)
    private List<Message> fetchMessagesFromDb() {
        // Implementation goes here
        return new ArrayList<>(); // Return fetched messages
    }
}
