from flask import Flask, request, session
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
limiter = Limiter(app, key_func=get_remote_address)

app.secret_key = 'your_secret_key'  # Change this to a random secret key
users = {}  # This should be replaced with a database in a real application

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format", 400
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users[email] = hashed_password
    return "Signup successful", 200

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    hashed_password = users.get(email)
    if hashed_password and bcrypt.check_password_hash(hashed_password, password):
        session['user'] = email
        return "Login successful", 200
    else:
        return "Invalid credentials", 401

@app.route('/change_email', methods=['POST'])
@limiter.limit("5 per minute")
def change_email():
    if 'user' not in session:
        return "Unauthorized", 401
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    password = request.form['password']
    if old_email != session['user'] or not bcrypt.check_password_hash(users[old_email], password):
        return "Invalid credentials", 401
    if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
        return "Invalid new email format", 400
    users[new_email] = users.pop(old_email)
    session['user'] = new_email
    return "Email changed successfully", 200

if __name__ == '__main__':
    app.run( )