from flask import Flask
import sqlite3

# Create a Flask web app
app = Flask(__name__)

# Define a function that returns a database connection
def get_db_connection():
    # For the sake of this example, we'll use an SQLite database
    conn = sqlite3.connect('example.db')  # Replace 'example.db' with your actual database file
    conn.row_factory = sqlite3.Row
    return conn

# Define a function that returns the server name
def get_server_name():
    return "localhost"  # Replace with your actual server name

# Define a function that returns the database name
def get_database_name():
    return "example.db"  # Replace with your actual database name

# Define a function that returns the database user
def get_database_user():
    return "admin"  # Replace with your actual database user

# Define a function that returns the database password
def get_database_password():
    return "password"  # Replace with your actual database password

# Define a route for the web app
@app.route('/')
def home():
    return f"""
        Server Name: {get_server_name()}<br>
        Database Name: {get_database_name()}<br>
        Database User: {get_database_user()}<br>
        Database Password: {get_database_password()}
    """

# Run the web app
if __name__ == '__main__':
    app.run( )
