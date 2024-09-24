#include <cppcms/application.h>
#include <cppcms/service.h>
#include <cppcms/session.h>
#include <cppcms/http_response.h>
#include <cppcms/view.h>

class MyApp : public cppcms::application {
public:
    MyApp(cppcms::service &srv) : cppcms::application(srv) {}

    void info() {
        // Check if session variables are set
        std::string username = session().get<std::string>("username", "Guest");
        std::string email = session().get<std::string>("email", "not provided");
        std::string ssn = session().get<std::string>("ssn", "not provided");

        // Create the HTML response
        response().out() << "<html><head><title>User Info</title></head><body>";
        response().out() << "<h1>User Information</h1>";
        response().out() << "<p><strong>Username:</strong> " << username << "</p>";
        response().out() << "<p><strong>Email:</strong> " << email << "</p>";
        response().out() << "<p><strong>Last 4 digits of SSN:</strong> " 
                         << ssn.substr(ssn.length() - 4) << "</p>";
        response().out() << "</body></html>";
    }
};

int main(int argc, char **argv) {
    cppcms::service srv(argc, argv);
    srv.applications_pool().mount(cppcms::create_pool<MyApp>());
    srv.run();
    return 0;
}
