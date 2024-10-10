from flask import Flask, request, redirect, url_for, session, render_template, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from itsdangerous import os

# Initialize Flask app
app = Flask(__name__)

# Generate a secure secret key
app.config['SECRET_KEY'] = os.urandom(24)

# Setup Flask-Limiter
limiter = Limiter(app, key_func=get_remote_address)

# Setup Flask-Talisman for HTTPS and security headers
Talisman(app)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define the login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Regexp(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', message="Password complexity requirements not met.")])

# Mock database for demonstration
users = {"admin": generate_password_hash("Admin@123")}

@app.route('/')
def index():
    return 'Index Page <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_password_hash = users.get(username)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('do_login'))
    return render_template('login.html', form=form)

@app.route('/secret')
def secret():
    if 'username' in session:
        return 'Secret settings'
    else:
        return redirect(url_for('do_login'))

@app.errorhandler(404)
def page_not_found(e):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use 'adhoc' for demo purposes. For production, specify cert and key.