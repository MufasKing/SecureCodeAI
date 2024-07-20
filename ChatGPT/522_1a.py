from flask import Flask, request, redirect, url_for, render_template
import sqlite3
import hashlib

app = Flask(__name__)

# Function to hash passwords
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database and create the users table
def init_db():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
        conn.commit()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    hashed_password = hash_password(password)
    
    with get_db_connection() as conn:
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            return 'Username already exists. Please choose a different username.'

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
