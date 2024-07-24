# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def hello_world():
    # Return the message to the user
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run( )
