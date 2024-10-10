from flask import Flask, request, redirect, render_template, session
import psycopg2
import psycopg2.extras
from psycopg2 import sql
import os

app = Flask(__name__)

# Secure session key
app.secret_key = os.urandom(24)

# Database connection parameters
DB_HOST = "your_host"
DB_NAME = "your_dbname"
DB_USER = "your_user"
DB_PASS = "your_password"

# Secure database connection function
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        cursor_factory=psycopg2.extras.DictCursor
    )
    return conn

# Function to insert user message into the database
def insert_user_message_in_db(username, message):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Parameterized query to prevent SQL injection
        cur.execute(
            "INSERT INTO messages (username, message) VALUES (%s, %s)",
            (username, message)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form.get('username', '')
    message = request.form.get('message', '')

    # Input sanitization
    username = sanitize_input(username)
    message = sanitize_input(message)

    # Insert the sanitized input into the database
    insert_user_message_in_db(username, message)

    # Secure redirection
    return redirect('/', code=302)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username, message FROM messages ORDER BY id DESC")
        messages = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', messages=messages)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while fetching messages."

# Function to sanitize input
def sanitize_input(input_string):
    # Implement input sanitization logic here
    # This is a placeholder for actual sanitization logic
    sanitized_string = input_string.replace("<", "&lt;").replace(">", "&gt;")
    return sanitized_string

if __name__ == '__main__':
    app.run( )