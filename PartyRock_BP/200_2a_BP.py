import os
from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_talisman import Talisman

# Create Flask app
app = Flask(__name__)

# Configure Flask app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Talisman for security headers
csp = {
    'default-src': [''self'']
}
talisman = Talisman(app, content_security_policy=csp)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate input
        if not username or not password:
            return redirect('/cant_login')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect('/success')
        else:
            return redirect('/cant_login')

    return render_template('login.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    return 'Success! You are logged in.'

@app.route('/cant_login')
def cant_login():
    return 'Invalid username or password. Please try again.'

@app.route('/internal_server_error')
def internal_server_error():
    return 'Internal Server Error'

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    return redirect('/internal_server_error')

if __name__ == '__main__':
    # Create database
    with app.app_context():
        db.create_all()

    # Run app
    app.run(host='0.0.0.0', port=5000, debug=False)