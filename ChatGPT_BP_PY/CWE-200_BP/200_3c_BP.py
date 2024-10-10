from flask import Flask, session, request, jsonify
from flask import escape as flask_escape
import os

app = Flask(__name__)

# Ensure the secret key is set from an environment variable for session management
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# Dummy authentication check function
def is_authenticated():
    # In a real-world scenario, you'd have proper authentication mechanisms
    return session.get('authenticated', False)

# Utility function for sensitive data masking
def mask_sensitive_data(data, mask_char='*', unmasked_count=4):
    if len(data) <= unmasked_count:
        return data
    return mask_char * (len(data) - unmasked_count) + data[-unmasked_count:]

@app.route('/info', methods=['GET'])
def info():
    # Check if the user is authenticated
    if not is_authenticated():
        return jsonify({"error": "Unauthorized access"}), 401
    
    # Get user info from session (ensure these are set in session during login)
    username = session.get('username', 'Unknown')
    email = session.get('email', 'Unknown')
    ssn = session.get('ssn', 'Unknown')

    # Escape the output to prevent XSS
    escaped_username = flask_escape(username)
    escaped_email = flask_escape(email)
    masked_ssn = mask_sensitive_data(ssn)
    
    # Return the user info
    return jsonify({
        "username": escaped_username,
        "email": escaped_email,
        "ssn": masked_ssn
    })

# Simulated login route for setting session data
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    email = request.form.get('email')
    ssn = request.form.get('ssn')

    if not username or not email or not ssn:
        return jsonify({"error": "Invalid input"}), 400

    # Simple validation (expand as needed)
    if len(ssn) != 9 or not ssn.isdigit():
        return jsonify({"error": "Invalid SSN"}), 400

    # Set session data
    session['authenticated'] = True
    session['username'] = username
    session['email'] = email
    session['ssn'] = ssn
    
    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
