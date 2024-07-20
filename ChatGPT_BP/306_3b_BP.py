from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_limiter import Limiter
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secure_secret_key'  # Replace with a strong, secure key
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are only sent over HTTPS
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True

# Rate Limiting
limiter = Limiter(app, key_func=lambda: request.remote_addr)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup (SQLite for simplicity)
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db_session = Session()

# Flask-WTF form
class EmailChangeForm(FlaskForm):
    old_email = StringField('Old Email', validators=[DataRequired(), Email()])
    new_email = StringField('New Email', validators=[DataRequired(), Email()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Change Email')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db_session.query(User).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['email'] = user.email
            logger.info(f"User {email} logged in successfully.")
            return redirect(url_for('change_email'))
        else:
            flash('Invalid credentials', 'danger')
            logger.warning(f"Failed login attempt for email: {email}")

    return render_template('login.html')

@app.route('/change_email', methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Rate limiting to prevent abuse
def change_email():
    if 'user_id' not in session:
        flash('You must be logged in to change your email.', 'warning')
        return redirect(url_for('login'))

    form = EmailChangeForm()
    if form.validate_on_submit():
        old_email = form.old_email.data
        new_email = form.new_email.data
        confirm_password = form.confirm_password.data

        user = db_session.query(User).filter_by(id=session['user_id']).first()

        if user and user.email == old_email and check_password_hash(user.password, confirm_password):
            user.email = new_email
            db_session.commit()
            session['email'] = new_email
            flash('Your email has been updated successfully.', 'success')
            logger.info(f"User {old_email} changed email to {new_email}.")
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password', 'danger')
            logger.warning(f"Email change attempt failed for user ID: {session['user_id']}")

    return render_template('change_email.html', form=form)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('You must be logged in to view your profile.', 'warning')
        return redirect(url_for('login'))

    return f"Logged in as: {session['email']}"

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # For development only. Use proper certificates for production.