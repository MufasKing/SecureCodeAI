from flask import Flask, request, redirect, render_template, session, flash, make_response

from werkzeug.security import generate_password_hash, check_password_hash

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_wtf import CSRFProtect

import re



app = Flask(__name__)

app.secret_key = 'your_secret_key_here'

limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])

csrf = CSRFProtect(app)



# Dummy database of users

users = {

    "user1": generate_password_hash("password123")

}



# Input validation regex

username_regex = re.compile(r'^\w+$')



@app.route('/')

def index():

    return render_template('login.html')



@app.route('/login', methods=['POST'])

@limiter.limit("5 per minute")

def login():

    username = request.form['username']

    password = request.form['password']

    

    # Input validation

    if not username_regex.match(username):

        flash('Invalid username.')

        return redirect('/')

    

    # Check if user exists and password is correct

    if username in users and check_password_hash(users[username], password):

        session['username'] = username

        resp = make_response(redirect('/session'))

        resp.headers['Content-Security-Policy'] = "default-src 'self'"

        return resp

    else:

        flash('Invalid username or password.')

        return redirect('/')



@app.route('/session')

def session_page():

    if 'username' in session:

        return f"Welcome {session['username']}! <a href='/logout'>Logout</a>"

    return redirect('/')



@app.route('/logout')

def logout():

    session.pop('username', None)

    return redirect('/')



if __name__ == '__main__':

    app.run(ssl_context='adhoc')  # Use 'adhoc' for testing only