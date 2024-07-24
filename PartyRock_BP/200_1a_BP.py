import os
import bcrypt
from flask import Flask, render_template, request, redirect, session, abort, make_response
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

# Initialize Flask app
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Set a secure secret key for session management
app.secret_key = os.environ.get('SECRET_KEY', 'your_secure_secret_key_here')

# Enable CSRF protection
csp = {
    'default-src': [
        ''self'',
        ''unsafe-inline'',
        'stackpath.bootstrapcdn.com',
        'code.jquery.com'
    ]
}
talisman = Talisman(app, content_security_policy=csp)

# Rate limiting
limiter = Limiter(app, key_func=get_remote_address)

# Fake database for demonstration purposes
users = {
    'admin': generate_password_hash('password123', method='bcrypt')
}

# Login route
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit('5/minute')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not username or not password:
            return render_template('login.html', error='Please enter both username and password.')

        # Check if user exists and password is correct
        if username in users:
            if check_password_hash(users[username], password):
                session['user'] = username
                return redirect('/dashboard')
            else:
                app.logger.warning(f'Failed login attempt for user {username}')
                return render_template('login.html', error='Invalid username or password.')
        else:
            app.logger.warning(f'Failed login attempt for non-existent user {username}')
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        abort(403)

    return render_template('dashboard.html', user=session['user'])

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# Error handling
@app.errorhandler(403)
def forbidden(error):
    return render_template('error.html', error='Forbidden'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Page not found'), 404

# Secure headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

# Secure Jinja template rendering
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    # Run the app securely on HTTPS
    app.run(ssl_context='adhoc', debug=False)