from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route using the route() decorator
@app.route('/')
def home():
    return "Hello, World!"

# Run the application
if __name__ == '__main__':
    app.run( )
