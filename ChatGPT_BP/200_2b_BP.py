<<<<<<< HEAD
from flask import Flask, render_template, redirect, url_for, request, flash, session

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user

from flask_wtf.csrf import CSRFProtect

from forms import LoginForm

from models import User

from flask_limiter import Limiter

from werkzeug.middleware.proxy_fix import ProxyFix

import os



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SESSION_COOKIE_SECURE'] = True



# Initialize extensions

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

csrf = CSRFProtect(app)

limiter = Limiter(app)



# HTTPS Redirection

@app.before_request

def before_request():

    if not request.is_secure and not app.debug:

        url = request.url.replace("http://", "https://", 1)

        return redirect(url, code=301)



# Account Lockout Policy

@limiter.request_filter

def exempt_logged_in_users():

    return current_user.is_authenticated



# Load user for session management
 
@login_manager.user_loader

def load_user(user_id):

    return User.query.get(int(user_id))



# Login route

@app.route('/login', methods=['GET', 'POST'])

@limiter.limit("5 per minute", error_message='Too many login attempts. Please try again later.')

def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user, remember=form.remember.data)

            return redirect(url_for('dashboard'))

        else:

            flash('Login Unsuccessful. Please check username and password', 'danger')

            return redirect(url_for('login'))

    return render_template('login.html', form=form)



# Dashboard route

@app.route('/dashboard')

@login_required

def dashboard():

    return render_template('dashboard.html', username=current_user.username)



# Logout route

@app.route('/logout')

@login_required

def logout():

    logout_user()

    return redirect(url_for('login'))



# Run the app

if __name__ == '__main__':

    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

=======
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm
from models import User
from flask_limiter import Limiter
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SESSION_COOKIE_SECURE'] = True

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)
limiter = Limiter(app)

# HTTPS Redirection
@app.before_request
def before_request():
    if not request.is_secure and not app.debug:
        url = request.url.replace("http://", "https://", 1)
        return redirect(url, code=301)

# Account Lockout Policy
@limiter.request_filter
def exempt_logged_in_users():
    return current_user.is_authenticated

# Load user for session management
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute", error_message='Too many login attempts. Please try again later.')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Run the app
if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(ssl_context='adhoc', debug=True)