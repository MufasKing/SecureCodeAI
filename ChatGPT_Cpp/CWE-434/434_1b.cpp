#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <boost/asio.hpp>
#include <boost/filesystem.hpp>
#include <iostream>
#include <string>
#include <fstream>

namespace beast = boost::beast;            // from <boost/beast.hpp>
namespace http = beast::http;              // from <boost/beast/http.hpp>
namespace net = boost::asio;                // from <boost/asio.hpp>
using tcp = boost::asio::ip::tcp;          // from <boost/asio/ip/tcp.hpp>

const std::string upload_directory = "uploads/";

class HttpServer {
public:
    HttpServer(net::io_context& ioc, unsigned short port)
        : acceptor_(ioc, tcp::endpoint(tcp::v4(), port)) {
        do_accept();
    }

private:
    tcp::acceptor acceptor_;

    void do_accept() {
        acceptor_.async_accept(
            beast::bind_front_handler(&HttpServer::on_accept, this));
    }

    void on_accept(beast::error_code ec, tcp::socket socket) {
        if (ec) {
            std::cerr << "Accept error: " << ec.message() << "\n";
        } else {
            std::make_shared<HttpSession>(std::move(socket))->start();
        }
        do_accept();
    }
};

class HttpSession : public std::enable_shared_from_this<HttpSession> {
public:
    HttpSession(tcp::socket socket)
        : socket_(std::move(socket)), buffer_() {}

    void start() {
        do_read();
    }

private:
    tcp::socket socket_;
    beast::flat_buffer buffer_;
    http::request<http::string_body> req_;

    void do_read() {
        auto self(shared_from_this());
        http::async_read(socket_, buffer_, req_,
            [this, self](beast::error_code ec, std::size_t bytes_transferred) {
                beast::ignore_unused(bytes_transferred);
                if (!ec) {
                    handle_request();
                }
            });
    }

    void handle_request() {
        if (req_.method() == http::verb::post) {
            std::string filename = upload_directory + "uploaded.pdf";
            std::ofstream ofs(filename, std::ios::binary);
            ofs.write(req_.body().data(), req_.body().size());
            ofs.close();

            http::response<http::string_body> res{http::status::ok, req_.version()};
            res.set(http::field::content_type, "text/plain");
            res.body() = "File uploaded successfully!";
            res.prepare_payload();
            http::async_write(socket_, res,
                [self = shared_from_this()](beast::error_code ec, std::size_t bytes_transferred) {
                    beast::ignore_unused(bytes_transferred);
                    if (ec) {
                        std::cerr << "Write error: " << ec.message() << "\n";
                    }
                });
        } else {
            http::response<http::string_body> res{http::status::bad_request, req_.version()};
            res.set(http::field::content_type, "text/plain");
            res.body() = "Invalid request method.";
            res.prepare_payload();
            http::async_write(socket_, res,
                [self = shared_from_this()](beast::error_code ec, std::size_t bytes_transferred) {
                    beast::ignore_unused(bytes_transferred);
                    if (ec) {
                        std::cerr << "Write error: " << ec.message() << "\n";
                    }
                });
        }
    }
};

int main() {
    try {
        boost::filesystem::create_directory(upload_directory); // Create the uploads directory if it doesn't exist
        net::io_context ioc;
        unsigned short port = 8080; // Set the port for the server
        HttpServer server(ioc, port);
        ioc.run();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
    }
    return 0;
}
