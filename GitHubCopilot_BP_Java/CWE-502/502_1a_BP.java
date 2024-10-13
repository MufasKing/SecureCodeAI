import static spark.Spark.*;
import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        port(4567); // Set the port

        get("/api", (request, response) -> {
            response.type("application/json");
            String payload = request.queryParams("payload");

            if (payload == null || payload.isEmpty()) {
                response.status(400);
                return new Gson().toJson(new StandardResponse(StatusResponse.ERROR, "Payload parameter is missing"));
            }

            try {
                Map<String, String> payloadMap = new Gson().fromJson(payload, HashMap.class);

                if (!payloadMap.containsKey("name")) {
                    response.status(400);
                    return new Gson().toJson(new StandardResponse(StatusResponse.ERROR, "Name field is missing in payload"));
                }

                String name = payloadMap.get("name");
                response.status(200);
                return new Gson().toJson(new StandardResponse(StatusResponse.SUCCESS, name));

            } catch (JsonSyntaxException e) {
                response.status(400);
                return new Gson().toJson(new StandardResponse(StatusResponse.ERROR, "Invalid JSON format"));
            } catch (Exception e) {
                response.status(500);
                return new Gson().toJson(new StandardResponse(StatusResponse.ERROR, "Internal Server Error"));
            }
        });
    }

    private enum StatusResponse {
        SUCCESS, ERROR
    }

    private static class StandardResponse {
        private StatusResponse status;
        private String message;

        public StandardResponse(StatusResponse status, String message) {
            this.status = status;
            this.message = message;
        }

        public StatusResponse getStatus() {
            return status;
        }

        public String getMessage() {
            return message;
        }
    }
}