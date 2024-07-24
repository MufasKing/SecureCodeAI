from flask import Flask, request, jsonify

import hashlib

import secrets

import hmac

import sqlite3

import re

from werkzeug.security import safe_str_cmp

from functools import wraps

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_sslify import SSLify



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key



# Configure rate limiting (adjust limits as per your needs)

limiter = Limiter(

    app,

    key_func=get_remote_address,

    default_limits=["100 per day", "20 per hour"]

)



# Force HTTPS (assuming you have HTTPS configured)

sslify = SSLify(app)



# SQLite database initialization

DATABASE = 'users.db'



def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn



# Utility functions

def generate_salt():

    return secrets.token_hex(16)



def generate_hashed_password(password, salt):

    # MD5 hashing (not recommended for production)

    hashed_password = hashlib.md5((password + salt).encode()).hexdigest()

    return hashed_password



def verify_password(provided_password, salt, stored_password):

    # Compare using constant-time comparison
 
    calculated_password = generate_hashed_password(provided_password, salt)

    return safe_str_cmp(calculated_password, stored_password)



# Middleware for input validation

def validate_input(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        username = request.json.get('username')

        password = request.json.get('password')



        # Validate username and password

        if not (username and re.match(r'^[\w.@+-]+$', username)):

            return jsonify({'error': 'Invalid username'}), 400

        if not (password and len(password) >= 8):  # Example: enforce password complexity

            return jsonify({'error': 'Password must be at least 8 characters long'}), 400



        return func(*args, **kwargs)

    return wrapper



# Route for user registration

@app.route('/register', methods=['POST'])

@limiter.limit("5 per minute")  # Example rate limiting

@validate_input

def register():

    username = request.json.get('username')

    password = request.json.get('password')



    salt = generate_salt()

    hashed_password = generate_hashed_password(password, salt)



    # Insert into database

    try:

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (username, salt, password) VALUES (?, ?, ?)',

                       (username, salt, hashed_password))

        conn.commit()

        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except sqlite3.Error as e:

        return jsonify({'error': 'Database error', 'details': str(e)}), 500



if __name__ == '__main__':

    app.run(  )