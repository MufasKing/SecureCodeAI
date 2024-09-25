#include <crow.h> // Import the web application class

int main()
{
    crow::SimpleApp app; // Create the application object

    // Define a route using a lambda function
    CROW_ROUTE(app, "/")([](){
        return "Hello, World!"; // Return the message to the user
    });

    app.port(18080).multithreaded().run(); // Run the application
}
