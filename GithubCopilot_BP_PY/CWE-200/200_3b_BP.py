from flask import Flask, request, render_template_string, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
import secrets

# App setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
db = SQLAlchemy(app)
limiter = Limiter(app, key_func=get_remote_address)

# Logging
logging.basicConfig(level=logging.INFO)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    ssn = db.Column(db.String(9), nullable=False)  # Store full SSN securely

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=50)])
    password = PasswordField('Password', [validators.Length(min=8)])

# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.hashed_password, form.password.data):
            session['user_id'] = user.id
            return redirect(url_for('info'))
        else:
            return 'Invalid username or password', 401
    return render_template_string('{{ form.csrf_token }} {{ form.username }} {{ form.password }}')

@app.route('/info')
@limiter.limit("5 per minute")
def info():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user:
        # Only display the last 4 digits of SSN
        return f"Username: {user.username}, Email: {user.email}, SSN: ****{user.ssn[-4:]}"
    return 'User not found', 404

if __name__ == '__main__':
    db.create_all()
    app.run(ssl_context='adhoc')  # Use 'adhoc' for development only