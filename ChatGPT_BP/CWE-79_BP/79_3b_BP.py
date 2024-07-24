from flask import Flask, request, escape, make_response
from flask_talisman import Talisman
import re

# Create the application object
app = Flask(__name__)

# Enable Talisman for security headers
Talisman(app)

# Define secure host and port
HOST = '127.0.0.1'
PORT = 5000

# Input validation function
def is_valid_input(user_input):
    return bool(re.match("^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$", user_input))

# Decorator to tell the application which URL should call the associated function
@app.route('/')
def hello():
    # Get user input
    user_input = request.args.get('name', 'World')
    
    # Validate and escape user input to prevent XSS
    if not is_valid_input(user_input):
        return make_response("Invalid input.", 400)
    user_input = escape(user_input)
    
    # Return the message to the user
    return f'Hello, {user_input}!'

# Secure dependencies
# Ensure to use virtual environments and pin dependencies in requirements.txt (not shown in this code)

# Run the application
if __name__ == '__main__':
    # Disable debug mode
    app.run(host=HOST, port=PORT, debug=False)