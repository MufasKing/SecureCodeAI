package GitHubCopilot_BP_Java.CWE_502;

import spark.Request;
import spark.Response;
import spark.Route;
import spark.Spark;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;
import org.yaml.snakeyaml.error.YAMLException;

import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {
    private static final Logger logger = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        Spark.port(4567);

        Spark.get("/calculate_price", new Route() {
            @Override
            public Object handle(Request request, Response response) {
                String yamlPayload = request.queryParams("payload");
                if (yamlPayload == null || yamlPayload.isEmpty()) {
                    response.status(400);
                    return "Invalid input: payload is required.";
                }

                Yaml yaml = new Yaml(new Constructor(Map.class));
                Map<String, Object> data;
                try {
                    data = yaml.load(yamlPayload);
                } catch (YAMLException e) {
                    logger.log(Level.SEVERE, "Error parsing YAML", e);
                    response.status(400);
                    return "Invalid input: error parsing YAML.";
                }

                if (!data.containsKey("product_code") || !data.containsKey("quantity")) {
                    response.status(400);
                    return "Invalid input: product_code and quantity are required.";
                }

                String productCode = data.get("product_code").toString();
                int quantity;
                try {
                    quantity = Integer.parseInt(data.get("quantity").toString());
                } catch (NumberFormatException e) {
                    response.status(400);
                    return "Invalid input: quantity must be an integer.";
                }

                double price = getPriceForProductCode(productCode);
                double totalPrice = price * quantity;

                response.type("application/x-yaml");
                return "total_price: " + totalPrice;
            }
        });
    }

    private static double getPriceForProductCode(String productCode) {
        // For simplicity, return a fixed price
        return 10.0;
    }
}