from flask import Flask, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import re

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secure_secret_key_here'

# CSRF Protection
csrf = CSRFProtect(app)

# Rate Limiting
limiter = Limiter(app, key_func=get_remote_address)

# Content Security Policy (CSP)
csp = {
    'default-src': [
        '\'self\'',
        'https://example.com',  # Replace with your domain
    ]
}
Talisman(app, content_security_policy=csp)

# Forms
class ChangeEmailForm(FlaskForm):
    old_email = StringField('Old Email', validators=[DataRequired(), Email()])
    new_email = StringField('New Email', validators=[DataRequired(), Email()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Change Email')

# User Authentication
# This is a simplified example. In a real application, you would use a secure authentication method.
users = {
    'user1': {
        'password': 'secure_password',
        'email': 'user1@example.com'
    }
}

@app.route('/change_email', methods=['GET', 'POST'])
@limiter.limit("5/minute")  # Limiting to 5 requests per minute
def change_email():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        # Input Validation
        new_email = form.new_email.data
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', new_email):
            flash('Invalid email format.', 'error')
            return redirect(url_for('change_email'))

        # User Authentication
        user = session.get('user')
        if not user:
            flash('You must be logged in to change your email.', 'error')
            return redirect(url_for('login'))

        # Password Verification
        old_email = form.old_email.data
        password = form.confirm_password.data
        if password != users[user]['password']:
            flash('Incorrect password.', 'error')
            return redirect(url_for('change_email'))

        # Update Email
        if old_email == users[user]['email']:
            users[user]['email'] = new_email
            flash('Your email has been updated successfully.', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid old email.', 'error')
            return redirect(url_for('change_email'))

    return form

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # User Authentication
        if username in users and users[username]['password'] == password:
            session['user'] = username
            flash('Logged in successfully.', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password.', 'error')

    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/profile')
def profile():
    user = session.get('user')
    if user:
        user_info = users[user]
        return f"Welcome, {user_info['email']} ({user})"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)