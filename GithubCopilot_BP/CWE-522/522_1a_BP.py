from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pyotp
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup rate limiter
limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=False, default=pyotp.random_base32())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Create DB
db.create_all()

@app.route('/register', methods=['POST'])
@limiter.limit("2 per minute")
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    # Input validation and password complexity requirements should be implemented here
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        # Implement 2FA check here using PyOTP
        return jsonify({'message': 'Login successful!'}), 200
    else:
        abort(401)

if __name__ == '__main__':
    # Ensure you have a SSL context for HTTPS
    context = ('cert.pem', 'key.pem')  # You need to generate your own SSL certificates
    app.run(ssl_context=context)