from flask import Flask, request, redirect, url_for, render_template, session, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from itsdangerous import URLSafeTimedSerializer
import os
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # Secure secret management
csrf = CSRFProtect(app)
limiter = Limiter(app, key_func=get_remote_address)

# Logging
logging.basicConfig(level=logging.INFO)

# Secure headers
@app.after_request
def set_secure_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=36)])

# User database mockup
users = {
    "admin": generate_password_hash("admin_password"),
    "user": generate_password_hash("user_password")
}
roles = {
    "admin": "admin",
    "user": "user"
}

# Serializer for secure token generation
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@app.route('/login', methods=['GET'])
@limiter.limit("5 per minute")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/do_login', methods=['POST'])
@csrf.exempt  # Normally, you would not exempt this from CSRF protection
@limiter.limit("5 per minute")
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            session['role'] = roles[username]
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'danger')
    return redirect(url_for('login'))

@app.route('/')
@limiter.limit("10 per minute")
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/user_page')
@limiter.limit("5 per minute")
def user_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') != 'user':
        return redirect(url_for('index'))
    return render_template('user_page.html', username=session['username'])

@app.route('/admin_page')
@limiter.limit("5 per minute")
def admin_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') != 'admin':
        return redirect(url_for('index'))
    return render_template('admin_page.html', username=session['username'])

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Ensure HTTPS
@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace("http://", "https://", 1)
        return redirect(url)

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use 'adhoc' for a self-signed certificate for development
