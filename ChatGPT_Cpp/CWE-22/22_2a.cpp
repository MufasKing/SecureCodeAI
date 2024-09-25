#include <crow.h>
#include <fstream>
#include <sstream>

using namespace std;

// Function to read the image file and return it as a response
crow::response img(const string& name) {
    // Construct the file path
    string filePath = "images/" + name;
    
    // Open the file
    ifstream file(filePath, ios::binary);
    
    // Check if the file was opened successfully
    if (!file.is_open()) {
        return crow::response(404, "File not found");
    }

    // Read the contents of the file into a stringstream
    stringstream buffer;
    buffer << file.rdbuf();
    
    // Create a response with the file contents
    crow::response response(200);
    response.body = buffer.str();
    response.add_header("Content-Type", "image/jpeg"); // Assuming JPEG images
    response.add_header("Content-Length", to_string(response.body.size()));

    return response;
}

// Main function to set up the server and routing
int main() {
    crow::SimpleApp app;

    // Route for /img
    CROW_ROUTE(app, "/img/<string>")
    ([](const crow::request& req, const string& name) {
        return img(name);
    });

    // Start the server on port 8080
    app.port(8080).multithreaded().run();

    return 0;
}
