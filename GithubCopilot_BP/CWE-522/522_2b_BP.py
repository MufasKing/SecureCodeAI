from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_wtf.csrf import CSRFProtect

from flask_talisman import Talisman

import os



app = Flask(__name__)

# Secure Secret Key

app.config['SECRET_KEY'] = os.urandom(24)

# Database Configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# CSRF Protection

CSRFProtect(app)

# Content Security Policy

csp = {

    'default-src': ['self','https://trusted.cdn.com']

}

Talisman(app, content_security_policy=csp)

# Rate Limiting

limiter = Limiter(app, key_func=get_remote_address, default_limits=["5 per minute"])

# Bcrypt for Password Hashing

bcrypt = Bcrypt(app)

# Database Initialization

db = SQLAlchemy(app)



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(120), nullable=False)



@app.route('/register', methods=['POST'])

@limiter.limit("2 per minute", error_message='Rate limit exceeded')

def register():

    username = request.form.get('username')

    password = request.form.get('password')

    # Input Validation (basic example)

    if not username or not password:

        return jsonify({"error": "Invalid input"}), 400

    # Password Hashing and Salt Generation

    hashed_password = bcrypt.generate_password_hash(password + os.urandom(16).hex()).decode('utf-8')

    # Database Storage

    try:

        user = User(username=username, password=hashed_password)

        db.session.add(user)

        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:

        return jsonify({"error": "User registration failed"}), 500



if __name__ == '__main__':

    db.create_all()

    app.run(ssl_context='adhoc')  # This enables HTTPS. For production, use a proper SSL certificate.