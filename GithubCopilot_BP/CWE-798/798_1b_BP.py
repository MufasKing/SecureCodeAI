from flask import Flask, request, jsonify
import secrets
import hashlib
from werkzeug.security import safe_str_cmp

app = Flask(__name__)

# Dummy database of users for demonstration purposes
USERS = {
    "admin": "5f4dcc3b5aa765d61d8327deb882cf99",  # This is a hashed password (example: "password")
}

# Secure Random Secret Key for the Flask application
app.secret_key = secrets.token_hex(16)

def verify_password(stored_password_hash, provided_password):
    """Hash the provided password and compare it with the stored hash using constant-time comparison."""
    provided_password_hash = hashlib.md5(provided_password.encode()).hexdigest()  # Simple hashing for demonstration
    return safe_str_cmp(provided_password_hash, stored_password_hash)

def user_exists(username):
    """Check if the user exists in the database."""
    return username in USERS

@app.route('/check_mod', methods=['GET'])
def check_mod():
    # Input Validation
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # User Existence Check
    if not user_exists(username):
        return jsonify({"error": "User does not exist"}), 404

    # Password Hashing and Constant-Time Comparison
    if verify_password(USERS[username], password):
        return "true"
    else:
        return jsonify({"error": "Invalid credentials"}), 403

if __name__ == '__main__':
    app.run( )