from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
limiter = Limiter(app, key_func=get_remote_address)
Talisman(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

class ChangeEmailForm(FlaskForm):
    old_email = StringField('Old Email', validators=[validators.DataRequired(), validators.Email()])
    new_email = StringField('New Email', validators=[validators.DataRequired(), validators.Email(), validators.NoneOf(message="New email must be different", values=lambda form: [form.old_email.data])])
    password = PasswordField('Confirm Password', validators=[validators.DataRequired()])

# Define routes for login, registration, email change, etc.

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # For HTTPS, in production use a proper SSL context or a reverse proxy handling HTTPS