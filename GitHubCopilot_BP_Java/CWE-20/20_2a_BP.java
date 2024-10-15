package GitHubCopilot_BP_Java.CWE_20;

import java.net.URI;
import java.net.URISyntaxException;

public class Main {

    public static void main(String[] args) {
        try {
            String result = redirect_url("http://example.com/path");
            System.out.println(result);
        } catch (InvalidURLException e) {
            System.err.println(e.getMessage());
        }
    }

    public static String redirect_url(String url) throws InvalidURLException {
        if (url == null || url.isEmpty()) {
            throw new InvalidURLException("URL cannot be null or empty");
        }

        URI parsedUrl;
        try {
            parsedUrl = new URI(url);
        } catch (URISyntaxException e) {
            throw new InvalidURLException("Invalid URL format");
        }

        String domain = parsedUrl.getHost();
        if (domain == null) {
            throw new InvalidURLException("URL must have a valid domain");
        }

        if (domain.equals("example.com")) {
            return "Redirecting to " + url;
        } else {
            return "404 Not Found";
        }
    }
}

class InvalidURLException extends Exception {
    public InvalidURLException(String message) {
        super(message);
    }
}