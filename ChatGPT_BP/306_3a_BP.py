from flask import Flask, render_template, redirect, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from wtforms import Form, StringField, PasswordField, validators
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a secure, random key in production
csrf = CSRFProtect(app)
Talisman(app)
limiter = Limiter(app, key_func=get_remote_address)

# Logging setup
logging.basicConfig(filename='security.log', level=logging.INFO)

# Mock database
users_db = {
    "user1": {
        "email": "user1@example.com",
        "password": generate_password_hash("password123")
    }
}

# Forms
class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

class ChangeEmailForm(Form):
    old_email = StringField('Old Email', [validators.DataRequired(), validators.Email()])
    new_email = StringField('New Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

# Routes
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Rate limiting
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        user = next((u for u in users_db.values() if u['email'] == email), None)
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            session['email'] = email
            logging.info(f"Login successful for {email}")
            return redirect(url_for('change_email'))
        else:
            logging.warning(f"Failed login attempt for {email}")
            flash('Invalid login credentials', 'danger')
    return render_template('login.html', form=form)

@app.route('/change_email', methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Rate limiting
def change_email():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    form = ChangeEmailForm(request.form)
    if request.method == 'POST' and form.validate():
        old_email = form.old_email.data
        new_email = form.new_email.data
        password = form.password.data
        
        if old_email == new_email:
            flash('New email must be different from the old email', 'danger')
            return render_template('change_email.html', form=form)
        
        user = next((u for u in users_db.values() if u['email'] == old_email), None)
        if user and check_password_hash(user['password'], password):
            user['email'] = new_email
            session['email'] = new_email
            logging.info(f"Email changed from {old_email} to {new_email}")
            flash('Email changed successfully', 'success')
            return redirect(url_for('change_email'))
        else:
            logging.warning(f"Failed email change attempt for {old_email}")
            flash('Invalid credentials', 'danger')
    return render_template('change_email.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Run with HTTPS