def escape_html(text):
    """Escapes HTML special characters in the given text."""
    import html
    return html.escape(text)

def http_hello_page(request, response):
    # Read the username from the request
    username = request.read().strip()
    
    # Escape the username to prevent HTML injection
    escaped_username = escape_html(username)
    
    # Construct the response string
    response_string = f"hello {escaped_username}"
    
    # Write the response string to the response file stream
    response.write(response_string)