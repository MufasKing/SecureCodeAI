from flask import Flask, session, request, jsonify
from os import environ, urandom
from functools import wraps

app = Flask(__name__)
app.secret_key = environ.get('FLASK_SECRET_KEY', urandom(24))
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in session:
            return jsonify({"error": "Authentication required"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/info', methods=['GET'])
@login_required
def info():
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')
    
    # Mask SSN for security
    masked_ssn = f"{ssn[:3]}-XX-XXXX" if ssn != 'N/A' else ssn
    
    # Ensure data is escaped to prevent XSS
    username = flask.escape(username)
    email = flask.escape(email)
    masked_ssn = flask.escape(masked_ssn)
    
    return jsonify({
        "username": username,
        "email": email,
        "ssn": masked_ssn
    })

if __name__ == '__main__':
    environ['FLASK_ENV'] = 'production'
    app.run(debug=False)