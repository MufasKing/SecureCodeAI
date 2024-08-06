# Python Flask example for a secure login page with email change functionality

from flask import Flask, request, session, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize Rate Limiter
limiter = Limiter(app, key_func=get_remote_address)

# Initialize Talisman for Secure Headers
Talisman(app)

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forms
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChangeEmailForm(FlaskForm):
    old_email = StringField('Old Email', validators=[DataRequired(), Email()])
    new_email = StringField('New Email', validators=[DataRequired(), Email()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Change Email')

# Routes
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5/minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('change_email'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/change_email', methods=['GET', 'POST'])
@login_required
@limiter.limit("5/minute")
def change_email():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.old_email.data).first()
        if user and user.check_password(form.confirm_password.data):
            user.email = form.new_email.data
            db.session.commit()
            flash('Your email has been updated.')
            return redirect(url_for('login'))
        else:
            flash('Invalid email or password.')
    return render_template('change_email.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run( )