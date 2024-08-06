from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/hello':
            try:
                # Input Sanitization
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype != 'multipart/form-data':
                    raise ValueError("Content type must be multipart/form-data")
                
                # Read the request body
                form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
                username = form.getvalue('username')
                if not username:
                    raise ValueError("Username is required")
                
                # Secure Handling Request Body
                username = self.sanitize_input(username)
                
                # Construct the response body
                outputbuf = self.construct_response(username)
                
                # Secure Handling Response Body
                outputbuf = self.secure_response(outputbuf)
                
                # Write the response body to the response stream
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(outputbuf.encode())
                
            except Exception as e:
                # Error Handling
                self.send_error(400, str(e))
            finally:
                # Close the response stream
                self.wfile.close()

    def sanitize_input(self, input_data):
        # Implement sanitization logic here
        # For example, escaping HTML characters, limiting length, etc.
        sanitized = cgi.escape(input_data, quote=True)
        return sanitized[:100]  # Limiting length to 100 characters

    def construct_response(self, username):
        # Separation of Concerns: Constructing response separately
        return f"<html><body><h2>Hello, {username}!</h2></body></html>"

    def secure_response(self, response):
        # Implement any additional security measures for the response
        # For example, adding security headers
        return response

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()