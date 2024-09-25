#include <iostream>
#include <string>
#include <crow.h> // Make sure to include the Crow library

// Function to insert the user message into the database (dummy implementation)
void insert_user_message_in_db(const std::string& username, const std::string& message) {
    // Implement your database insertion logic here
    std::cout << "Inserted message from " << username << ": " << message << std::endl;
}

// Function to handle POST request
void post(const crow::request& req, crow::response& res) {
    // Extract username and message from the request
    auto username = req.body["username"];
    auto message = req.body["message"];
    
    // Call the function to insert the message into the database
    insert_user_message_in_db(username, message);

    // Redirect back to the main page
    res.redirect("/");
}

// Main function to set up the server and the form
int main() {
    crow::SimpleApp app;

    // Define the route for the post function
    CROW_ROUTE(app, "/submit").methods("POST"_method)([](const crow::request& req) {
        crow::response res;
        post(req, res);
        return res;
    });

    // Main page with a form to submit a message
    CROW_ROUTE(app, "/")([]() {
        return R"(
            <html>
                <body>
                    <h1>Message Submission</h1>
                    <form action="/submit" method="post">
                        Username: <input type="text" name="username" required><br>
                        Message: <textarea name="message" required></textarea><br>
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>
        )";
    });

    // Start the server
    app.port(18080).multithreaded().run();
    return 0;
}
