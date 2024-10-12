import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.yaml.snakeyaml.Yaml;

import javax.net.ssl.*;
import java.io.FileInputStream;
import java.io.InputStream;
import java.security.KeyStore;
import java.util.Map;

@SpringBootApplication
@RestController
public class MyWebApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyWebApplication.class, args);
    }

    @PostMapping("/process")
    public ResponseEntity<String> processRequest(@RequestParam(required = false) String payload) {
        if (payload == null || payload.isEmpty()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Error: Missing 'payload' parameter.");
        }

        Map<String, Object> parsedPayload;
        try {
            parsedPayload = parseYAML(payload);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Error: Invalid YAML format.");
        }

        String type = (String) parsedPayload.get("type");
        if ("Create".equalsIgnoreCase(type)) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN)
                    .body("Error: Operation 'Create' is not allowed.");
        } else if ("Update".equalsIgnoreCase(type)) {
            String name = (String) parsedPayload.get("name");
            if ("UnsafeDeserialization".equalsIgnoreCase(name)) {
                return ResponseEntity.status(HttpStatus.FORBIDDEN)
                        .body("Error: 'UnsafeDeserialization' is not permitted.");
            }
        }

        return ResponseEntity.ok("Success: Request processed.");
    }

    private Map<String, Object> parseYAML(String payload) throws Exception {
        Yaml yaml = new Yaml();
        return yaml.load(payload);
    }

    // Secure SSL configuration for HTTPS
    private void configureHttps() throws Exception {
        char[] password = "your-keystore-password".toCharArray();
        KeyStore keyStore = KeyStore.getInstance("JKS");
        try (InputStream keyStoreInput = new FileInputStream("your-keystore.jks")) {
            keyStore.load(keyStoreInput, password);
        }
        SSLContext sslContext = SSLContext.getInstance("TLS");
        KeyManagerFactory keyManagerFactory = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
        keyManagerFactory.init(keyStore, password);
        sslContext.init(keyManagerFactory.getKeyManagers(), null, null);
        HttpsURLConnection.setDefaultSSLSocketFactory(sslContext.getSocketFactory());
    }
}
