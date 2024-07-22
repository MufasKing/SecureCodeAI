def sanitize_username(username):
    # Remove any leading/trailing whitespace and any unwanted characters
    # Only allow alphanumeric characters and a few special characters for usernames
    sanitized_username = ''.join(c for c in username if c.isalnum() or c in '-_.')
    return sanitized_username.strip()

def read_request(request):
    try:
        # Read the request data
        request_data = request.read()
        # Assuming the request data is in a simple format "username=the_username"
        if request_data.startswith("username="):
            username = request_data[len("username="):]
            return username
        else:
            raise ValueError("Invalid request format")
    except Exception as e:
        raise ValueError(f"Error reading request: {str(e)}")

def write_response(response, message):
    try:
        response.write(message)
    except Exception as e:
        raise IOError(f"Error writing response: {str(e)}")

def http_hello_page(request, response):
    try:
        # Read and sanitize the username
        raw_username = read_request(request)
        username = sanitize_username(raw_username)

        # Construct the response message
        response_message = f"Hello {username}"

        # Write the response
        write_response(response, response_message)
    
    except ValueError as ve:
        # Handle errors related to reading the request
        error_message = f"400 Bad Request: {str(ve)}"
        write_response(response, error_message)
    
    except IOError as ioe:
        # Handle errors related to writing the response
        error_message = f"500 Internal Server Error: {str(ioe)}"
        write_response(response, error_message)
    
    except Exception as e:
        # Catch-all for any other exceptions
        error_message = f"500 Internal Server Error: {str(e)}"
        write_response(response, error_message)

# Example usage with file streams (for demonstration purposes)
if __name__ == "__main__":
    from io import StringIO
    
    # Simulate a request with a username
    request_stream = StringIO("username=example_user")
    response_stream = StringIO()

    http_hello_page(request_stream, response_stream)

    # Output the response content
    print(response_stream.getvalue())