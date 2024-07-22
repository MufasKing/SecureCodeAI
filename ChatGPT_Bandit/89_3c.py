from flask import Flask, request, redirect, url_for, render_template
import sqlite3  # or any other database module you're using

app = Flask(__name__)

# Function to insert user message into the database
def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('database.db')  # Replace with your database file or connection details
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO messages (username, message)
        VALUES (?, ?)
    ''', (username, message))
    conn.commit()
    conn.close()

# Route for handling POST requests from the message form
@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect(url_for('index'))

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run( )
