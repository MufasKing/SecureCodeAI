import html

def read_username_from_request(request):
    """
    Reads the username from the request file stream.
    Assumes the username is sent in a simple format: "username: <username>"
    """
    try:
        for line in request:
            if line.startswith("username:"):
                # Extracting the username part and sanitizing it to prevent HTML injection
                return html.escape(line.strip().split(":", 1)[1].strip())
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

def http_hello_page(request, response):
    """
    Handles the HTTP request by reading the username from the request,
    constructing a hello message, and writing it to the response file stream.
    """
    try:
        username = read_username_from_request(request)
        hello_message = construct_hello_response(username)
        response.write(hello_message)
    except Exception as e:
        print(f"Error handling HTTP request: {e}")
        response.write("An error occurred while processing your request.")

# Example usage
with open("request.txt", "r") as request_stream, open("response.txt", "w") as response_stream:
    http_hello_page(request_stream, response_stream)