from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Initialize SQLite database and create a users table
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# Function to check credentials in the database
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None

# Route for the login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Route to handle login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if check_credentials(username, password):
        return redirect('/home')
    else:
        return redirect('/')

# Route for the home page
@app.route('/home')
def home():
    return '<h1>Welcome to the Home Page!</h1>'

if __name__ == '__main__':
    init_db()  # Create database and table if not exists
    app.run( )
