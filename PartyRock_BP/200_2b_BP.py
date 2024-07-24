import hashlib
import os
from flask import Flask, render_template, request, redirect, session
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timedelta

# Flask app configuration
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management
csrf = CSRFProtect(app)  # Enable CSRF protection

# Database of users (for demonstration purposes)
users = {
    'admin': {
        'password_hash': hashlib.sha256(b'securepassword').hexdigest(),
        'failed_attempts': 0,
        'lockout_time': None
    }
}

# Maximum allowed failed login attempts
MAX_FAILED_ATTEMPTS = 5

# Account lockout duration (in minutes)
LOCKOUT_DURATION = 30

# Helper function to check if an account is locked
def is_account_locked(username):
    if username in users:
        user = users[username]
        if user['lockout_time'] is not None:
            if datetime.now() < user['lockout_time']:
                return True
    return False

# Helper function to lock an account
def lock_account(username):
    if username in users:
        user = users[username]
        user['lockout_time'] = datetime.now() + timedelta(minutes=LOCKOUT_DURATION)
        user['failed_attempts'] = 0

# Helper function to reset failed login attempts
def reset_failed_attempts(username):
    if username in users:
        users[username]['failed_attempts'] = 0

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Input validation
        if not username or not password:
            return render_template('login.html', error='Please enter both username and password.')

        # Check if the account is locked
        if is_account_locked(username):
            return render_template('login.html', error='Your account is temporarily locked due to too many failed login attempts. Please try again later.')

        # Retrieve user from the database
        if username in users:
            user = users[username]
            password_hash = user['password_hash']

            # Password comparison using a secure method
            if hashlib.sha256(password.encode()).hexdigest() == password_hash:
                # Reset failed login attempts
                reset_failed_attempts(username)

                # Set the session and redirect to the dashboard
                session['username'] = username
                return redirect('/dashboard', code=302)  # Use 302 for secure redirect

            # Incorrect password
            user['failed_attempts'] += 1
            if user['failed_attempts'] >= MAX_FAILED_ATTEMPTS:
                lock_account(username)
                return render_template('login.html', error='Too many failed login attempts. Your account has been temporarily locked.')

        # Invalid username
        return render_template('login.html', error='Invalid username or password.')

    # Render the login page for GET requests
    return render_template('login.html')

# Dashboard route (accessible only after successful login)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome to the dashboard, {session['username']}!"
    else:
        return redirect('/login')  # Redirect to the login page if not authenticated

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,  , ssl_context='adhoc')