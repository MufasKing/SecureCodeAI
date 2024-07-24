from flask import Flask, session, redirect, request, escape
from flask_session import Session
import os
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure random secret key

# Configure secure session management
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Input validation and sanitization functions
def validate_username(username):
    # Check if the username contains only alphanumeric characters and underscore
    return bool(re.match(r'^[\w]+$', username))

def validate_email(email):
    # Use a regular expression to validate the email format
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))

def validate_ssn(ssn):
    # Check if the SSN is a 9-digit number
    return bool(re.match(r'^\d{9}$', ssn))

def sanitize_input(input_str):
    # Escape any special characters in the input string
    return escape(input_str)

@app.route('/info', methods=['GET'])
def info():
    # Check if the user is authenticated
    if 'username' not in session or 'email' not in session or 'ssn' not in session:
        return redirect('/login')  # Redirect to the login page if not authenticated

    # Retrieve and validate the user data from the session
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')

    if not validate_username(username) or not validate_email(email) or not validate_ssn(ssn):
        return redirect('/login')  # Redirect to the login page if user data is invalid

    # Sanitize the user data
    sanitized_username = sanitize_input(username)
    sanitized_email = sanitize_input(email)
    sanitized_ssn = sanitize_input(ssn[-4:])  # Display only the last 4 digits of the SSN

    # Render the info page with the sanitized user data
    return f'Username: {sanitized_username}<br>Email: {sanitized_email}<br>Last 4 digits of SSN: {sanitized_ssn}'

if __name__ == '__main__':
    app.run(debug=False)  # Run the Flask app in production mode (without debug)