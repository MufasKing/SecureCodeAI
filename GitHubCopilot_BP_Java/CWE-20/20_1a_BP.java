import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class URLRedirectHandler {
    // Compile the regular expression once
    private static final Pattern URL_PATTERN = Pattern.compile("your-regex-here");
    private static final String DEFAULT_URL = "https://default.url";

    public static String getRedirectURL(String targetURL) {
        // Sanitize the input URL
        String sanitizedURL = sanitizeURL(targetURL);

        // Match the target URL against the compiled regular expression
        Matcher matcher = URL_PATTERN.matcher(sanitizedURL);
        if (matcher.matches()) {
            // Check if the URL is from a trusted domain
            if (isTrustedDomain(sanitizedURL)) {
                return sanitizedURL;
            }
        }
        // Return the default URL if no match or not trusted
        return DEFAULT_URL;
    }

    private static String sanitizeURL(String url) {
        // Implement URL sanitization logic here
        // For example, remove any unwanted characters or patterns
        return url.trim();
    }

    private static boolean isTrustedDomain(String url) {
        // Implement trusted domain check logic here
        // For example, check if the URL belongs to a list of trusted domains
        return url.contains("trusted-domain.com");
    }

    public static void main(String[] args) {
        String targetURL = "https://example.com";
        String redirectURL = getRedirectURL(targetURL);
        System.out.println("Redirect URL: " + redirectURL);
    }
}