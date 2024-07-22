from flask import Flask, request, redirect, url_for, render_template_string, session

import sqlite3

from werkzeug.security import safe_join

import os



app = Flask(__name__)

app.secret_key = os.urandom(24)  # Secure session key



DATABASE = 'messages.db'



# Securely connect to the SQLite database

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row  # Enable column access by name

    return conn



# Create a table for messages if it doesn't exist

def create_table():

    with get_db_connection() as conn:

        conn.execute('''

            CREATE TABLE IF NOT EXISTS messages (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT NOT NULL,

                message TEXT NOT NULL

            )

        ''')

        conn.commit()



# Insert message into the database with parameterized queries

def insert_user_message_in_db(username, message):

    try:

        with get_db_connection() as conn:

            conn.execute('INSERT INTO messages (username, message) VALUES (?, ?)', (username, message))

            conn.commit()

    except sqlite3.Error as e:

        print(f"An error occurred: {e}")
 


# Route to handle message posting

@app.route('/post', methods=['POST'])

def post_message():

    username = request.form.get('username')

    message = request.form.get('message')



    if not username or not message:

        return "Username and message are required!", 400



    insert_user_message_in_db(username, message)

    return redirect(url_for('index'))  # Secure redirection



# Route to display messages

@app.route('/')

def index():

    try:

        with get_db_connection() as conn:

            messages = conn.execute('SELECT username, message FROM messages').fetchall()

    except sqlite3.Error as e:

        return f"An error occurred: {e}", 500



    messages_html = ''.join([f"<p><strong>{row['username']}</strong>: {row['message']}</p>" for row in messages])

    return render_template_string(f'''

        <h1>Messages</h1>

        {messages_html}

        <form action="{{ url_for('post_message') }}" method="post">

            Username: <input type="text" name="username"><br>

            Message: <textarea name="message"></textarea><br>

            <input type="submit" value="Post">

        </form>

    ''')



if __name__ == '__main__':

    create_table()  # Ensure the table exists before running the app

    app.run(debug=True)