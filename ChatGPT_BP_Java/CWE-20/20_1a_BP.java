import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.net.URL;
import java.net.URISyntaxException;

public class URLRedirector {

    // Compile the regular expression once when the module is loaded
    private static final Pattern TARGET_URL_PATTERN = Pattern.compile("^https://(www\\.)?trusteddomain\\.com/.*");
    private static final String DEFAULT_REDIRECT_URL = "https://www.defaultdomain.com";
    private static final String[] TRUSTED_DOMAINS = { "trusteddomain.com", "anothertrusted.com" };

    // Method to sanitize the URL
    public static String sanitizeUrl(String url) {
        try {
            URL validUrl = new URL(url);
            validUrl.toURI(); // Ensure it's a valid URI
            return validUrl.toString();
        } catch (URISyntaxException | java.net.MalformedURLException e) {
            // Invalid URL: fallback to default URL
            return DEFAULT_REDIRECT_URL;
        }
    }

    // Method to check if the URL is from a trusted domain
    public static boolean isTrustedDomain(String url) {
        try {
            URL validUrl = new URL(url);
            String host = validUrl.getHost();
            for (String trustedDomain : TRUSTED_DOMAINS) {
                if (host.endsWith(trustedDomain)) {
                    return true;
                }
            }
        } catch (java.net.MalformedURLException e) {
            // Malformed URL
        }
        return false;
    }

    // Method to perform the redirect based on the target URL
    public static String handleRedirect(String targetUrl) {
        targetUrl = sanitizeUrl(targetUrl); // Sanitize input URL

        // Check if target URL matches the regular expression pattern
        Matcher matcher = TARGET_URL_PATTERN.matcher(targetUrl);
        if (matcher.matches() && isTrustedDomain(targetUrl)) {
            return targetUrl; // Use the target URL if it matches the pattern
        } else {
            return DEFAULT_REDIRECT_URL; // Use default URL if not matching
        }
    }

    public static void main(String[] args) {
        // Example target URL
        String targetUrl = "https://www.trusteddomain.com/path/to/resource";
        String redirectUrl = handleRedirect(targetUrl);

        System.out.println("Redirecting to: " + redirectUrl);

        // Example of an untrusted URL
        targetUrl = "https://www.untrusted.com/unsafe/path";
        redirectUrl = handleRedirect(targetUrl);
        System.out.println("Redirecting to: " + redirectUrl);
    }
}
