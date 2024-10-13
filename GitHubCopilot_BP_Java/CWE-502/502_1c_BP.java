package GitHubCopilot_BP_Java.CWE-502;

import static spark.Spark.*;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.dataformat.yaml.YAMLParser;
import spark.Request;
import spark.Response;

import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Secure server setup
        secure("keystore.jks", "password", null, null);
        port(5000);

        // Route to handle requests
        post("/handleRequest", (request, response) -> handleRequest(request, response));
    }

    private static String handleRequest(Request request, Response response) {
        String payload = request.queryParams("payload");

        // Input validation
        if (payload == null || payload.isEmpty()) {
            response.status(400);
            return "Error: Missing payload parameter.";
        }

        try {
            // Secure YAML parsing
            ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
            YAMLParser parser = mapper.getFactory().createParser(payload);
            Map<String, Object> yamlMap = mapper.readValue(parser, Map.class);

            // Access control and input sanitization
            if (yamlMap.containsKey("type")) {
                String type = (String) yamlMap.get("type");
                if ("Create".equals(type)) {
                    response.status(400);
                    return "Error: Create type is not allowed.";
                } else if ("Update".equals(type)) {
                    if ("UnsafeDeserialization".equals(yamlMap.get("name"))) {
                        response.status(200);
                        return "Update request with name UnsafeDeserialization is processed.";
                    }
                }
            }

            response.status(400);
            return "Error: Invalid payload content.";
        } catch (Exception e) {
            response.status(500);
            return "Error: Failed to parse YAML payload.";
        }
    }
}