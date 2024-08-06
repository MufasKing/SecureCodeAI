# Import necessary libraries
from flask import Flask, request, redirect, session, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

# Create the database
db.create_all()

# Login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Input validation (basic example)
        if not username or not password:
            flash('Username and password are required!')
            return redirect('/login')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return redirect('/home')
        else:
            flash('Invalid username or password!')
            return redirect('/login')
    return render_template('login.html')

# Home page
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/login')
    return 'Welcome to the home page!'

# Logout function
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

# Run the app
if __name__ == '__main__':
    app.run( )