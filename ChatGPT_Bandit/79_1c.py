import html

def escape_html(text):
    """Escapes HTML special characters in the given text."""
    return html.escape(text)

def http_hello_page(request, response):
    """Generates an HTTP response that says 'hello [username]'."""
    # Read the request from the request stream (assuming it's a simple HTTP request)
    request_line = request.readline().decode('utf-8').strip()
    
    # Extract username from the request (this is a simplified example)
    # Let's assume the request is of the form: "GET /?username=JohnDoe HTTP/1.1"
    # We need to parse the query string to get the username.
    
    if 'username=' in request_line:
        # Extract the query string part of the request
        query_string = request_line.split(' ')[1]
        # Extract the username from the query string
        username = query_string.split('username=')[1].split(' ')[0]
        # Escape the username to avoid HTML injection issues
        safe_username = escape_html(username)
    else:
        # If no username is provided, use a default name
        safe_username = "Guest"
    
    # Create the response message
    response_message = f"hello {safe_username}"
    
    # Write the HTTP headers (basic example)
    response.write(b"HTTP/1.1 200 OK\r\n")
    response.write(b"Content-Type: text/html\r\n")
    response.write(b"Content-Length: " + str(len(response_message)).encode('utf-8') + b"\r\n")
    response.write(b"\r\n")
    
    # Write the response body
    response.write(response_message.encode('utf-8'))
