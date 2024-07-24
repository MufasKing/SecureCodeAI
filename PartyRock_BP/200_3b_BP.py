import os
import bcrypt
import secrets
import logging
from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)  # Generate a secure secret key

# Configure Rate Limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Enable security headers
csp = {
    'default-src': ["'self'"]
}
talisman = Talisman(app, content_security_policy=csp)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Connect to SQLite database
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, email TEXT, password TEXT, ssn TEXT)''')

# User authentication and password hashing
def authenticate_user(username, password):
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        hashed_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
    return False

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Secure route for user information
@app.route('/info', methods=['GET'])
@limiter.limit("10 per minute")
def info():
    # Authenticate user
    auth = request.authorization
    if not auth or not authenticate_user(auth.username, auth.password):
        return make_response('Could not verify your login credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    # Get user data from database
    c.execute("SELECT email, ssn FROM users WHERE username = ?", (auth.username,))
    result = c.fetchone()
    if result:
        email, ssn = result
        ssn_last4 = ssn[-4:]  # Only show last 4 digits of SSN
        return render_template('info.html', username=auth.username, email=email, ssn_last4=ssn_last4)
    else:
        return "User not found"

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ssn = request.form['ssn']

        # Input validation
        if not username or not email or not password or not ssn:
            return "Please provide all required fields"
        if len(ssn) != 9 or not ssn.isdigit():
            return "Invalid social security number format"

        # Input sanitization
        username = username.strip()
        email = email.strip()
        password = password.strip()
        ssn = ssn.strip()

        # Check if user already exists
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result:
            return "Username already taken"

        # Hash password and store user data in database
        hashed_password = hash_password(password)
        c.execute("INSERT INTO users (username, email, password, ssn) VALUES (?, ?, ?, ?)", (username, email, hashed_password, ssn))
        conn.commit()

        return redirect(url_for('info'))
    return render_template('register.html')

if __name__ == '__main__':
    # Disable debug mode in production
    app.debug = False

    # Run the app securely over HTTPS
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))