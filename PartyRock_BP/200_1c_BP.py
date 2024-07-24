import os
import bcrypt
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure secret key

# Database simulation (replace with your actual database implementation)
users = {
    "admin": {
        "password_hash": b'$2b$12$9WdMbgMySXNl2eSfrohWAOZpQHLhp8zYqkx7gtOYoEQ.C8ECq7BxW',  # hashed password: "password123"
        "is_active": True
    }
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return redirect(url_for('login'))

        # Check if the user exists in the database
        user = users.get(username)
        if not user or not user['is_active']:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), user['password_hash']):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' not in session:
        flash('You are not logged in', 'warning')
        return redirect(url_for('login'))

    username = session['username']
    return render_template('home.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run( )