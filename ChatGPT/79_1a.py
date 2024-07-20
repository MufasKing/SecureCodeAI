from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/hello':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            username = urllib.parse.parse_qs(post_data).get('username', [''])[0]

            # Construct the HTML response body
            outputbuf = f"""
            <html>
            <head><title>Hello Page</title></head>
            <body>
                <h1>Hello, {username}!</h1>
            </body>
            </html>
            """

            # Send the HTTP response status
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', str(len(outputbuf)))
            self.end_headers()

            # Write the response body
            self.wfile.write(outputbuf.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()