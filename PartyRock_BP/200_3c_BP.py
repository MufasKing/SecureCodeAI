import os
from flask import Flask, session, redirect, url_for, escape, request
from flask_login import LoginManager, UserMixin, login_required, current_user
from dotenv import load_dotenv
import bcrypt
import re

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
SALT = bcrypt.gensalt()

# Flask app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

# User model for authentication
class User(UserMixin):
    def __init__(self, username, email, ssn):
        self.username = username
        self.email = email
        self.ssn = ssn

@login_manager.user_loader
def load_user(user_id):
    # Load user from your data source here
    pass

# Input validation functions
def validate_username(username):
    # Implement username validation rules
    pattern = r'^[a-zA-Z0-9_]+$'
    return bool(re.match(pattern, username))

def validate_email(email):
    # Implement email validation rules
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_ssn(ssn):
    # Implement SSN validation rules
    pattern = r'^\d{9}$'
    return bool(re.match(pattern, ssn))

# Route for /info
@app.route('/info', methods=['GET'])
@login_required
def info():
    # Check if user is authenticated
    if current_user.is_authenticated:
        # Retrieve user data from session
        username = escape(session.get('username', ''))
        email = escape(session.get('email', ''))
        ssn = session.get('ssn', '')

        # Mask sensitive data
        masked_ssn = '***-**-' + ssn[-4:]

        # Return user information as a string
        info_str = f"Username: {username}
Email: {email}
SSN: {masked_ssn}"
        return info_str
    else:
        return redirect(url_for('login'))

# Production mode configuration
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)