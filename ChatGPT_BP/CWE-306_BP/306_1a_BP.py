from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_limiter import Limiter
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are only sent over HTTPS
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_DURATION'] = 3600  # 1 hour

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Dummy user data (use a database in production)
users = {
    'admin': bcrypt.generate_password_hash('Password123!').decode('utf-8')
}

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8),
        Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#]).+$', message="Password must contain an upper case letter, a lower case letter, a digit, and a special character.")
    ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Rate limiting
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and bcrypt.check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            flash('Invalid username or password', 'danger')
            logging.warning(f'Failed login attempt for username: {username}')
    return render_template('login.html', form=form)

@app.route('/secret')
def secret():
    if 'username' not in session:
        return redirect(url_for('login'))
    return 'Secret settings'

@app.errorhandler(404)
def not_found_error(error):
    return '404 Page Not Found', 404

@app.errorhandler(500)
def internal_error(error):
    return '500 Internal Server Error', 500

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use HTTPS in development; use a proper SSL certificate in production