import hashlib
import os
import sqlite3
from flask import Flask, request, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect

# Initialize Flask app
app = Flask(__name__)
csrf = CSRFProtect(app)

# Rate limiting setup
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute"]
)

# Database setup
DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Password policy enforcement
def enforce_password_policy(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    # Add more policies as needed

# Input validation
def validate_username(username):
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric")

# Salt generation and password hashing
def hash_password(password):
    salt = os.urandom(16)  # Generate a salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed_password

@app.route('/register', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limiting for registration
def register():
    try:
        username = request.form['username']
        password = request.form['password']
        
        validate_username(username)
        enforce_password_policy(password)
        
        hashed_password = hash_password(password)
        
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Run with HTTPS