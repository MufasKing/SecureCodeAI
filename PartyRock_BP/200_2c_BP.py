import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

# CSRF protection
csp = {
    'default-src': [
        ''self'',
    ],
    'script-src': [
        ''self'',
    ],
    'style-src': [
        ''self'',
    ],
}
talisman = Talisman(app, content_security_policy=csp)

# Rate Limiting
limiter = Limiter(app, key_func=get_remote_address)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

# In-memory user database (replace with a proper database in production)
users = {
    1: User(1, 'admin', generate_password_hash('strongpassword'))
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("10/minute")  # Rate limiting
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        # Input validation
        if not username or not password:
            flash('Username and password are required.', 'error')
            return redirect(url_for('login'))

        user = next((user for user in users.values() if user.username == username), None)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('session'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/session', methods=['GET'])
@login_required
def session():
    return render_template('session.html', username=current_user.username)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run( )