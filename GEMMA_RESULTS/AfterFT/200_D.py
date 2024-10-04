from flask import Flask, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
import re

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secure_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Input Validation
        if not username or not password:
            return redirect(url_for('cant_login'))

        # Input Sanitization
        username = username.strip()
        password = password.strip()

        # Validate username format
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return redirect(url_for('cant_login'))

        # Database Query
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('success'))
        else:
            return redirect(url_for('cant_login'))

    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "Logged in successfully!"

@app.route('/cant_login')
def cant_login():
    return "Invalid username or password."

@app.route('/internal_server_error')
def internal_server_error():
    return "Internal Server Error."

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)