# Step 1: Import the necessary class for the web application
from flask import Flask, request, escape

# Step 2: Create an instance of the class. This instance will act as the WSGI application.
app = Flask(__name__)

# Step 3: Use a decorator to tell the application which URL should call the associated function.
@app.route('/')
def hello_world():
    # Step 4: This is the function that gets called when the user visits the specified URL.
    
    # Perform input validation and escape to prevent XSS
    name = request.args.get("name", "World")
    safe_name = escape(name)
    
    # Step 5: Return the message to the user, ensuring any user input is safely escaped.
    return f'Hello, {safe_name}!'

# Step 6: Run the application with secure settings.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)