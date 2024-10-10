from flask import Flask, request, redirect, render_template, session, url_for, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Rate limiting setup
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute"]
)

# CSRF protection is enabled by default in Flask-WTF
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Dummy database of users
users_db = {
    "user1": generate_password_hash("password1")
}

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/do_login', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limiting for login attempts
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_hash = users_db.get(username)
        if user_hash and check_password_hash(user_hash, password):
            session['username'] = username  # Session management
            return redirect(url_for('user_page'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return 'Invalid input', 400

@app.route('/user_page')
def user_page():
    if 'username' in session:
        return f"Welcome {session['username']}!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # HTTPS