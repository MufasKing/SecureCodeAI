# Step 1: Import necessary libraries
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import logging

# Step 2: Initialize Flask app, database, CSRF protection, and rate limiter
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Secure secret key
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS
app.config['REMEMBER_COOKIE_HTTPONLY'] = True  # Prevent client-side script access to the cookie
app.config['REMEMBER_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])  # Rate limiting

# Step 3: Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Step 4: Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Step 5: Create the database
db.create_all()

# Step 6: Define routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Rate limiting for login attempts
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Input validation
        if not username or not password:
            flash('Username and password are required!')
            return redirect(url_for('login'))
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  # Session management
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Step 7: Run the app
if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Run with HTTPS