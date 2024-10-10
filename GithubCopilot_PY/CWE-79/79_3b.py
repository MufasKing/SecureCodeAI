from flask import Flask  # Import the web application class

app = Flask(__name__)  # Create the application object

@app.route('/')  # Decorator to associate URL with function
def hello_world():  # Function called when user visits the URL
    return 'Hello, World!'  # Return message to the user

if __name__ == '__main__':
    app.run()  # Run the application