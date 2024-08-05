def http_hello_page(request, response):
    # Step 1: Read the request body (the username)
    username = request.body.decode('utf-8')
    
    # Step 2: Construct the response body (the HTML page)
    outputbuf = f"""
    <html>
    <head><title>Hello Page</title></head>
    <body>
        <h1>Hello, {username}!</h1>
    </body>
    </html>
    """
    
    # Step 3: Write the response body to the response stream
    response.write(outputbuf.encode('utf-8'))
    
    # Step 4: Close the response stream
    response.close()
    
    # The server is now ready to handle the next request