package GitHubCopilot_BP_Java.CWE_78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class Main {
    private static final String url = "example.com"; // URL to ping

    public static void main(String[] args) {
        String result = ping(url);
        System.out.println(result);
    }

    // Function to ping a URL
    public static String ping(String url) {
        // Input Validation and Sanitization
        if (url == null || url.isEmpty() || !isValidURL(url)) {
            return "Invalid URL";
        }

        String pong = "";
        ProcessBuilder processBuilder = new ProcessBuilder();
        processBuilder.command("ping", "-c", "4", url); // Principle of Least Privilege

        try {
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            StringBuilder output = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
            int exitCode = process.waitFor();
            pong = output.toString();

            if (exitCode == 0) {
                return "URL is alive\n" + pong;
            } else {
                return "URL is not alive\n" + pong;
            }
        } catch (IOException | InterruptedException e) {
            return "Error occurred while pinging: " + e.getMessage();
        }
    }

    // Helper function to validate URL
    private static boolean isValidURL(String url) {
        String regex = "^(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})([/\\w .-]*)*/?$";
        Pattern pattern = Pattern.compile(regex);
        return pattern.matcher(url).matches();
    }
}