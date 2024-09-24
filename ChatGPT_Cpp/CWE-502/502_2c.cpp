#include <pistache/httplistener.h>
#include <sqlite3.h>
#include <iostream>
#include <string>

using namespace Pistache;

class TemperatureApi {
public:
    TemperatureApi(Address addr) : httpListener(addr) {}

    void start() {
        httpListener.init();
        httpListener.setHandler(Http::make_handler<TemperatureApiHandler>());
        httpListener.serve();
    }

private:
    Http::Listener httpListener;

    class TemperatureApiHandler : public Http::Handler {
    public:
        HTTP_PROTOTYPE(TemperatureApiHandler)

        void onRequest(const Http::Request& request, Http::ResponseWriter response) override {
            // Check if the request is for the right endpoint
            if (request.resource() == "/api/temperature_for_location" && request.method() == Http::Method::Get) {
                // Parse query parameters
                auto query = request.query();
                auto latitude = query.get("latitude");
                auto longitude = query.get("longitude");
                auto date = query.get("date");

                if (latitude && longitude && date) {
                    // Get temperature for the specified location and date
                    std::string temperature = temperature_for_location(latitude.value(), longitude.value(), date.value());
                    response.send(Http::Code::Ok, temperature);
                } else {
                    response.send(Http::Code::Bad_Request, "Missing parameters");
                }
            } else {
                response.send(Http::Code::Not_Found, "Endpoint not found");
            }
        }

    private:
        std::string temperature_for_location(const std::string& latitude, const std::string& longitude, const std::string& date) {
            sqlite3* db;
            sqlite3_stmt* stmt;
            std::string temperature = "N/A";

            // Open the database connection
            if (sqlite3_open("temperature_data.db", &db) == SQLITE_OK) {
                // Prepare the SQL query
                std::string sql = "SELECT temperature FROM temperatures WHERE latitude = ? AND longitude = ? AND date = ?";
                
                if (sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr) == SQLITE_OK) {
                    // Bind parameters
                    sqlite3_bind_text(stmt, 1, latitude.c_str(), -1, SQLITE_STATIC);
                    sqlite3_bind_text(stmt, 2, longitude.c_str(), -1, SQLITE_STATIC);
                    sqlite3_bind_text(stmt, 3, date.c_str(), -1, SQLITE_STATIC);

                    // Execute the query and retrieve the temperature
                    if (sqlite3_step(stmt) == SQLITE_ROW) {
                        temperature = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 0));
                    }
                }
                sqlite3_finalize(stmt);
            }
            sqlite3_close(db);

            return temperature;
        }
    };
};

int main() {
    // Set up the API server
    Port port(9080);
    auto addr = Address(Ipv4::any(), port);
    TemperatureApi api(addr);
    api.start();

    return 0;
}
