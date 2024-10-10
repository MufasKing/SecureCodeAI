from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_limiter import Limiter
from flask_talisman import Talisman
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import os
import re
from cryptography.fernet import Fernet

# Secure key generation for sensitive data protection
SECRET_KEY = os.urandom(32)
FERNET_KEY = Fernet.generate_key()
cipher_suite = Fernet(FERNET_KEY)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Secure headers with Flask-Talisman
talisman = Talisman(app)

# Rate limiting with Flask-Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    ssn = db.Column(db.String(200), nullable=False)  # Encrypted SSN

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_ssn(self, ssn):
        self.ssn = cipher_suite.encrypt(ssn.encode()).decode()

    def get_ssn(self):
        return cipher_suite.decrypt(self.ssn.encode()).decode()

# Login manager user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    ssn = StringField('SSN', validators=[DataRequired(), Length(min=11, max=11)])
    submit = SubmitField('Register')

    def validate_ssn(self, ssn):
        if not re.match(r'^\d{3}-\d{2}-\d{4}$', ssn.data):
            raise ValidationError('SSN must be in the format XXX-XX-XXXX')

# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.set_ssn(form.ssn.data)
        db.session.add(user)
        db.session.commit()
        logger.info(f"New user registered: {user.username}")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            logger.info(f"User logged in: {user.username}")
            return redirect(url_for('info'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logger.info(f"User logged out: {current_user.username}")
    logout_user()
    return redirect(url_for('login'))

@app.route('/info')
@login_required
def info():
    user = current_user
    email = user.email
    username = user.username
    ssn = user.get_ssn()
    last_4_ssn = ssn[-4:]
    return render_template('info.html', username=username, email=email, last_4_ssn=last_4_ssn)

# Disable debug mode for production
if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, ssl_context='adhoc')  # Using ad-hoc SSL context for HTTPS