def http_hello_page(request, response):
    # Read the username from the request file stream
    username = request.read().strip()
    
    # Construct the response string
    response_message = f"Hello {username}"
    
    # Write the response message to the response file stream
    response.write(response_message)