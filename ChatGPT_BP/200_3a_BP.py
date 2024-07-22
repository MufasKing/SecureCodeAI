<<<<<<< HEAD
from flask import Flask, session, render_template_string, redirect, url_for, request

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired, Email, Length, Regexp

from flask_wtf.csrf import CSRFProtect

import re

import os



app = Flask(__name__)

app.secret_key = os.urandom(24)  # Secure secret key

csrf = CSRFProtect(app)



# Input validation and sanitization function

def sanitize_input(data):

    return re.sub(r'[^\w\s@.]', '', data)



# Mock function to simulate user login

def mock_user_login():

    session['username'] = 'test_user'

    session['email'] = 'test_user@example.com'

    session['ssn'] = '123-45-6789'



@app.route('/info', methods=['GET'])

def info():

    # Ensure user is "logged in" by checking session variables

    if 'username' not in session or 'email' not in session or 'ssn' not in session:

        return redirect(url_for('login'))

    

    username = sanitize_input(session['username'])

    email =  nput(session['email'])

    ssn_last4 = session['ssn'][-4:]  # Only show last 4 digits of SSN

    

    # Create a simple HTML template for the response

    html_template = '''

    <!DOCTYPE html>

    <html lang="en">

    <head>

        <meta charset="UTF-8">

        <title>User Info</title>

    </head>

    <body>

        <h1>User Information</h1>

        <p><strong>Username:</strong> {{ username }}</p>

        <p><strong>Email:</strong> {{ email }}</p>

        <p><strong>SSN (Last 4 digits):</strong> {{ ssn_last4 }}</p>

    </body>

    </html>

    '''

    

    return render_template_string(html_template, username=username, email=email, ssn_last4=ssn_last4)



@app.route('/login', methods=['GET', 'POST'])

def login():

    # Simulating user login for demonstration purposes

    mock_user_login()

    return redirect(url_for('info'))



if __name__ == '__main__':

=======
from flask import Flask, session, render_template_string, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_wtf.csrf import CSRFProtect
import re
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure secret key
csrf = CSRFProtect(app)

# Input validation and sanitization function
def sanitize_input(data):
    return re.sub(r'[^\w\s@.]', '', data)

# Mock function to simulate user login
def mock_user_login():
    session['username'] = 'test_user'
    session['email'] = 'test_user@example.com'
    session['ssn'] = '123-45-6789'

@app.route('/info', methods=['GET'])
def info():
    # Ensure user is "logged in" by checking session variables
    if 'username' not in session or 'email' not in session or 'ssn' not in session:
        return redirect(url_for('login'))
    
    username = sanitize_input(session['username'])
    email = sanitize_input(session['email'])
    ssn_last4 = session['ssn'][-4:]  # Only show last 4 digits of SSN
    
    # Create a simple HTML template for the response
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>User Info</title>
    </head>
    <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>SSN (Last 4 digits):</strong> {{ ssn_last4 }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, username=username, email=email, ssn_last4=ssn_last4)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Simulating user login for demonstration purposes
    mock_user_login()
    return redirect(url_for('info'))

if __name__ == '__main__':
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)