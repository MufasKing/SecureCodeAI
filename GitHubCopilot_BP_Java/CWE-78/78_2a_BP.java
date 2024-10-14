package GitHubCopilot_BP_Java.CWE-78;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.regex.Pattern;

public class Main {

    @WebRoute(url = "/ping")
    public static String ping(String url) {
        // Validate URL
        if (!isValidURL(url)) {
            return "Invalid URL";
        }

        StringBuilder output = new StringBuilder();
        ProcessBuilder processBuilder = new ProcessBuilder();

        // Escape the URL to prevent command injection
        String escapedUrl = escapeShellArg(url);

        // Run the ping command
        processBuilder.command("ping", "-c", "4", escapedUrl);

        try {
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                return "Error executing ping command";
            }
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }

        return output.toString();
    }

    private static boolean isValidURL(String url) {
        try {
            new URL(url).toURI();
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static String escapeShellArg(String arg) {
        return arg.replaceAll("([\"'`\\\\])", "\\\\$1");
    }
}

// Custom annotation to define web routes
@interface WebRoute {
    String url();
}