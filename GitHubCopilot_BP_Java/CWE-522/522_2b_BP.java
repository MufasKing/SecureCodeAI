package GitHubCopilot_BP_Java.CWE_522;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Base64;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/register")
public class RegistrationServlet extends HttpServlet {

    private static final String DB_URL = "jdbc:mysql://localhost:3306/securedb";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "password";
    private static final int SALT_LENGTH = 16;
    private static final int HASH_ITERATIONS = 65536;
    private static final int KEY_LENGTH = 256;

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (!isValidInput(username, password)) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid input");
            return;
        }

        try {
            byte[] salt = generateSalt();
            String hashedPassword = hashPassword(password, salt);
            storeUser(username, hashedPassword, salt);
            response.setStatus(HttpServletResponse.SC_OK);
        } catch (Exception e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "An error occurred");
        }
    }

    private boolean isValidInput(String username, String password) {
        // Implement input validation and password strength validation
        return username != null && !username.isEmpty() && password != null && password.length() >= 8;
    }

    private byte[] generateSalt() throws NoSuchAlgorithmException {
        SecureRandom sr = SecureRandom.getInstanceStrong();
        byte[] salt = new byte[SALT_LENGTH];
        sr.nextBytes(salt);
        return salt;
    }

    private String hashPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
        PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, HASH_ITERATIONS, KEY_LENGTH);
        SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA512");
        byte[] hash = skf.generateSecret(spec).getEncoded();
        return Base64.getEncoder().encodeToString(hash);
    }

    private void storeUser(String username, String hashedPassword, byte[] salt) throws SQLException {
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String sql = "INSERT INTO users (username, password, salt) VALUES (?, ?, ?)";
            try (PreparedStatement stmt = conn.prepareStatement(sql)) {
                stmt.setString(1, username);
                stmt.setString(2, hashedPassword);
                stmt.setString(3, Base64.getEncoder().encodeToString(salt));
                stmt.executeUpdate();
            }
        }
    }
}