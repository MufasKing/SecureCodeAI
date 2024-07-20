from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)

# Database setup
DATABASE = 'users.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        db.commit()

# Initialize the database
init_db()

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login page template
login_page = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

# Home page template
home_page = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home</title>
</head>
<body>
    <h2>Welcome to the Home Page!</h2>
    <a href="/">Logout</a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hash_password(password)

    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    if user and user['password'] == hashed_password:
        return render_template_string(home_page)
    else:
        return 'Invalid username or password', 403

if __name__ == '__main__':
    app.run(debug=True)
