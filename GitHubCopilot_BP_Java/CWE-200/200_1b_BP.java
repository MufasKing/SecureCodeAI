import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import org.sql2o.Sql2o;
import org.sql2o.Connection;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private Sql2o sql2o;

    @Override
    public void init() throws ServletException {
        sql2o = new Sql2o("jdbc:mysql://localhost:3306/yourdb", "username", "password");
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        if (username == null || password == null || username.isEmpty() || password.isEmpty()) {
            response.sendRedirect("login.html");
            return;
        }

        String hashedPassword = hashPassword(password);

        try (Connection con = sql2o.open()) {
            String sql = "SELECT COUNT(*) FROM users WHERE username = :username AND password = :password";
            int count = con.createQuery(sql)
                           .addParameter("username", username)
                           .addParameter("password", hashedPassword)
                           .executeScalar(Integer.class);

            if (count > 0) {
                HttpSession session = request.getSession();
                session.setAttribute("username", username);
                response.sendRedirect("home.html");
            } else {
                response.sendRedirect("login.html");
            }
        }
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (byte b : hashedBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}