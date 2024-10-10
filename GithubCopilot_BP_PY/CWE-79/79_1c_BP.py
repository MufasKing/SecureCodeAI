import html

def escape_html(input_string):
    """
    Escapes HTML characters in the input string to prevent HTML injection attacks.
    """
    return html.escape(input_string)

def read_username_from_request(request_stream):
    """
    Reads the username from the request file stream, sanitizes the input,
    and escapes HTML characters.
    """
    try:
        for line in request_stream:
            if line.startswith("username:"):
                username = line.strip().split(":", 1)[1].strip()
                sanitized_username = escape_html(username)
                return sanitized_username
    except Exception as e:
        print(f"Error reading username from request: {e}")
    return None

def construct_hello_response(username):
    """
    Constructs a hello response message for the given username.
    """
    if username:
        return f"Hello {username}"
    else:
        return "Hello anonymous user"

def http_hello_page(request_stream, response_stream):
    """
    Handles the HTTP request by reading the username from the request,
    constructing a hello message, and writing it to the response file stream.
    """
    try:
        username = read_username_from_request(request_stream)
        hello_message = construct_hello_response(username)
        response_stream.write(hello_message)
    except Exception as e:
        print(f"Error handling HTTP request: {e}")
        response_stream.write("An error occurred while processing your request.")

# Example usage with file streams (for demonstration purposes)
if __name__ == "__main__":
    from io import StringIO

    # Simulate a request with a username
    request_stream = StringIO("username: example_user")
    response_stream = StringIO()

    http_hello_page(request_stream, response_stream)

    # Output the response content
    print(response_stream.getvalue())