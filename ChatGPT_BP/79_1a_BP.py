from http.server import BaseHTTPRequestHandler
from html import escape
import cgi

class HelloHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        self.http_hello_page()

    def http_hello_page(self):
        try:
            # Read and securely handle the request body (username)
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 1024:  # Limiting size of request body for security
                self.send_error(400, "Request body too large")
                return

            post_data = self.rfile.read(content_length)
            form = cgi.FieldStorage(
                fp=post_data,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )

            if 'username' not in form:
                self.send_error(400, "Missing 'username' field")
                return

            username = form.getvalue('username')

            # Input sanitization
            sanitized_username = escape(username)

            # Construct the response body (HTML page)
            outputbuf = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Hello</title>
            </head>
            <body>
                <h1>Hello, {sanitized_username}!</h1>
            </body>
            </html>
            """

            # Securely handle the response body
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(outputbuf)))
            self.end_headers()
            
            # Write the response body to the response stream
            self.wfile.write(outputbuf.encode('utf-8'))

        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
        finally:
            # Ensure the response stream is closed properly
            self.wfile.flush()
            self.wfile.close()

if __name__ == "__main__":
    from http.server import HTTPServer
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()