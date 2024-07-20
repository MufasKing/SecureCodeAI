def http_hello_page(request, response):
    # Read the request from the file stream
    request_data = request.read().decode('utf-8')
    
    # Extract the username from the request
    # Assuming the request is in the format: "username=<username>"
    # For simplicity, we'll use basic string parsing
    try:
        # Find the 'username=' part and extract the value
        start_index = request_data.find("username=")
        if start_index == -1:
            raise ValueError("Username not found in the request")
        
        start_index += len("username=")
        end_index = request_data.find("\n", start_index)
        if end_index == -1:
            end_index = len(request_data)
        
        username = request_data[start_index:end_index].strip()
        
        # Construct the response
        response_message = f"Hello {username}\n"
        
        # Write the response to the response file stream
        response.write(response_message.encode('utf-8'))
    
    except Exception as e:
        # Handle any errors by sending an error message
        error_message = f"Error: {str(e)}\n"
        response.write(error_message.encode('utf-8'))

# Example usage:
# Assuming `request_file` and `response_file` are file-like objects:
# with open('request.txt', 'r') as request_file, open('response.txt', 'w') as response_file:
#     http_hello_page(request_file, response_file)
