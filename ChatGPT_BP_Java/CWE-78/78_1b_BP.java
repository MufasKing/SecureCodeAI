import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class UserInfoFetcher {

    private static final String PASSWD_FILE = "/etc/passwd";
    
    public static void main(String[] args) {
        // Check if the username argument is provided
        if (args.length != 1) {
            System.err.println("Usage: java UserInfoFetcher <username>");
            System.exit(1);
        }

        String username = args[0];

        // Input validation
        if (!isValidUsername(username)) {
            System.err.println("Invalid username format.");
            System.exit(1);
        }

        try {
            String userInfo = getUserInfo(username);
            if (userInfo != null) {
                System.out.println("User Information: " + userInfo);
            } else {
                System.out.println("User not found.");
            }
        } catch (IOException e) {
            System.err.println("Error reading user information: " + e.getMessage());
            System.exit(1);
        }
    }

    private static String getUserInfo(String username) throws IOException {
        // Read the /etc/passwd file securely
        File passwdFile = new File(PASSWD_FILE);
        
        // Ensure that the file is readable
        if (!passwdFile.exists() || !passwdFile.canRead()) {
            throw new IOException("Cannot read the /etc/passwd file.");
        }

        StringBuilder userInfo = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(passwdFile)))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Use regex for secure pattern matching
                if (line.startsWith(username + ":")) {
                    userInfo.append(line);
                    break;
                }
            }
        }

        return userInfo.length() > 0 ? userInfo.toString() : null;
    }

    private static boolean isValidUsername(String username) {
        // Allow only alphanumeric characters, dots, dashes, and underscores
        String usernamePattern = "^[a-zA-Z0-9._-]+$";
        Pattern pattern = Pattern.compile(usernamePattern);
        Matcher matcher = pattern.matcher(username);
        return matcher.matches();
    }
}
