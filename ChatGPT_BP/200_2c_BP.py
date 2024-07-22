<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired, Length

from flask_bcrypt import Bcrypt

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_talisman import Talisman

from functools import wraps

import os



app = Flask(__name__)

app.secret_key = os.urandom(24)



# Password hashing

bcrypt = Bcrypt(app)



# CSRF Protection

Talisman(app)



# Rate Limiting

limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])



# Secure Headers

Talisman(app, content_security_policy=None)



# Dummy user for demonstration

users = {

    "user1": bcrypt.generate_password_hash("password123").decode('utf-8')

}



# Login Form

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100)])



# User authentication check

def login_required(f):

    @wraps(f 

    def decorated_function(*args, **kwargs):

        if 'username' not in session:

            return redirect(url_for('login'))

        return f(*args, **kwargs)

    return decorated_function



@app.route('/login', methods=['GET', 'POST'])

@limiter.limit("5 per minute")

def login():

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data

        password = form.password.data

        user_password_hash = users.get(username)

        if user_password_hash and bcrypt.check_password_hash(user_password_hash, password):

            session['username'] = username

            return redirect(url_for('session_page'))

        else:

            flash('Username or Password is incorrect', 'error')

    return render_template('login.html', form=form)



@app.route('/session')

@login_required

def session_page():

    return f'Welcome {session["username"]} to your session page! <a href="/logout">Logout</a>'



@app.route('/logout')

@login_required

def logout():

    session.pop('username', None)

    return redirect(url_for('login'))



@app.errorhandler(429)

def ratelimit_handler(e):

    return "You have exceeded your login attempts. Please try again later.", 429



if __name__ == '__main__':

=======
from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired, Length

from flask_bcrypt import Bcrypt

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_talisman import Talisman

from functools import wraps

import os



app = Flask(__name__)

app.secret_key = os.urandom(24)



# Password hashing

bcrypt = Bcrypt(app)



# CSRF Protection

Talisman(app)



# Rate Limiting

limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])



# Secure Headers

Talisman(app, content_security_policy=None)



# Dummy user for demonstration

users = {

    "user1": bcrypt.generate_password_hash("password123").decode('utf-8')

}



# Login Form

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100)])



# User authentication check

def login_required(f):

    @wraps(f)
 
    def decorated_function(*args, **kwargs):

        if 'username' not in session:

            return redirect(url_for('login'))

        return f(*args, **kwargs)

    return decorated_function



@app.route('/login', methods=['GET', 'POST'])

@limiter.limit("5 per minute")

def login():

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data

        password = form.password.data

        user_password_hash = users.get(username)

        if user_password_hash and bcrypt.check_password_hash(user_password_hash, password):

            session['username'] = username

            return redirect(url_for('session_page'))

        else:

            flash('Username or Password is incorrect', 'error')

    return render_template('login.html', form=form)



@app.route('/session')

@login_required

def session_page():

    return f'Welcome {session["username"]} to your session page! <a href="/logout">Logout</a>'



@app.route('/logout')

@login_required

def logout():

    session.pop('username', None)

    return redirect(url_for('login'))



@app.errorhandler(429)

def ratelimit_handler(e):

    return "You have exceeded your login attempts. Please try again later.", 429



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(debug=True)