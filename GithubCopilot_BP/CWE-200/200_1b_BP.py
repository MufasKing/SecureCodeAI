# Step 1: Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
import os

# Step 2: Initialize Flask app, CSRF protection, and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CSRFProtect(app)

# Step 3: Define User model for SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Step 4: Create the database
db.create_all()

# Step 5: Define route for login page and form handling
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Input Validation (basic example)
        if not username or not password:
            return redirect(url_for('login'))  # Redirect to login page if validation fails

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  # Session management
            return redirect(url_for('home'))  # Redirect to home page if login is successful
        else:
            return redirect(url_for('login'))  # Redirect to login page if login fails
    return render_template('login.html')  # Render login page for GET request

# Step 6: Define route for home page
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login page if not logged in
    return 'Welcome to the Home Page'  # Placeholder home page content

# Step 7: Run the Flask app
if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Run with HTTPS