from flask import Flask, session, request, redirect, url_for, render_template_string
from flask_session import Session
import re

app = Flask(__name__)

# Configure secure session management
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure the app secret key is set to a strong, random value in production
app.secret_key = 'your_secret_key_here'

@app.route('/info')
def info():
    # Validate session data
    if all(key in session for key in ["username", "email", "ssn"]):
        # Input sanitization
        username = re.sub(r'[^a-zA-Z0-9]', '', session['username'])
        email = re.sub(r'[^a-zA-Z0-9@.]', '', session['email'])
        ssn = re.sub(r'[^0-9]', '', session['ssn'][-4:])
        
        # Secure handling and separation of concerns
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>User Info</title>
            </head>
            <body>
                <h1>User Information</h1>
                <p>Username: {{username}}</p>
                <p>Email: {{email}}</p>
                <p>SSN (Last 4 Digits): {{ssn}}</p>
            </body>
            </html>
        ''', username=username, email=email, ssn=ssn)
    else:
        # Secure redirect if session data is not valid
        return redirect(url_for('login'))

@app.route('/login')
def login():
    # Dummy login route for demonstration
    return "Please login to view your information."

if __name__ == '__main__':
    app.run( )