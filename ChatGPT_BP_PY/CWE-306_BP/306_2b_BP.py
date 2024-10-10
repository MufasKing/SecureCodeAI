from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS

bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6, max=35)])

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/do_login', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limiting
def do_login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Input validation
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            flash('Invalid username format.', 'danger')
            return redirect(url_for('login'))

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('user_page'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
    else:
        flash('Form validation failed.', 'danger')
        return redirect(url_for('login'))

@app.route('/user_page', methods=['GET'])
def user_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "Welcome to the user page!"

if __name__ == '__main__':
    db.create_all()
    app.run(ssl_context=('cert.pem', 'key.pem'))  # Ensure HTTPS is used