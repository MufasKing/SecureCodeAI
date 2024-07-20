from flask import Flask, request, session, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

DATABASE = 'login_system.db'
RATE_LIMIT = {}

# Rate limit function
def rate_limited():
    client_ip = request.remote_addr
    current_time = time.time()
    if client_ip in RATE_LIMIT:
        if current_time - RATE_LIMIT[client_ip] < 1:
            return True
    RATE_LIMIT[client_ip] = current_time
    return False

# Database connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create users table
def create_tables():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("You need to log in first!")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# CSRF token generation
def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = os.urandom(24).hex()
    return session['_csrf_token']

# CSRF token validation
@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            return "CSRF token missing or incorrect!", 403

app.jinja_env.globals['csrf_token'] = generate_csrf_token

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if rate_limited():
        return "Too many requests, please try again later.", 429

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash("All fields are required!")
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password)
        
        try:
            with get_db() as conn:
                conn.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)', 
                             (username, email, password_hash))
                conn.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
            return redirect(url_for('register'))

    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if rate_limited():
        return "Too many requests, please try again later.", 429

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Username and password required!")
            return redirect(url_for('login'))

        with get_db() as conn:
            user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user and check_password_hash(user['password_hash'], password):
            session['username'] = username
            flash("Logged in successfully!")
            return redirect(url_for('change_email'))
        else:
            flash("Invalid credentials!")
            return redirect(url_for('login'))

    return render_template('login.html')

# Change email address
@app.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    if rate_limited():
        return "Too many requests, please try again later.", 429

    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        password = request.form['password']

        username = session['username']

        with get_db() as conn:
            user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user and check_password_hash(user['password_hash'], password) and user['email'] == old_email:
            with get_db() as conn:
                conn.execute('UPDATE users SET email = ? WHERE username = ?', (new_email, username))
                conn.commit()
            flash("Email updated successfully!")
        else:
            flash("Incorrect old email or password!")
            return redirect(url_for('change_email'))

    return render_template('change_email.html')

# User logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)