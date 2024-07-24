import html

def escape_html(text):
    """Escape HTML characters in the given text."""
    return html.escape(text)

def read_request(request):
    """Read and parse the username from the request stream."""
    try:
        # Assuming the request is in the format 'username=someusername'
        content = request.read().decode('utf-8')
        if not content.startswith('username='):
            raise ValueError("Invalid request format")
        username = content[len('username='):]
        return username.strip()
    except Exception as e:
        raise ValueError(f"Error reading request: {e}")

def construct_response(username):
    """Construct the response message."""
    sanitized_username = escape_html(username)
    return f"hello {sanitized_username}"

def write_response(response, message):
    """Write the response message to the response stream."""
    try:
        response.write(message.encode('utf-8'))
    except Exception as e:
        raise IOError(f"Error writing response: {e}")

def http_hello_page(request, response):
    """Handle the HTTP request and send back a hello message."""
    try:
        username = read_request(request)
        message = construct_response(username)
        write_response(response, message)
    except ValueError as ve:
        error_message = f"400 Bad Request: {ve}"
        response.write(error_message.encode('utf-8'))
    except IOError as ioe:
        error_message = f"500 Internal Server Error: {ioe}"
        response.write(error_message.encode('utf-8'))

# Example usage:
if __name__ == "__main__":
    from io import BytesIO
    
    # Simulate request and response streams
    request_stream = BytesIO(b"username=JohnDoe")
    response_stream = BytesIO()
    
    http_hello_page(request_stream, response_stream)
    
    # Check the response
    response_stream.seek(0)
    print(response_stream.read().decode('utf-8'))