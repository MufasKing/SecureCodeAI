from flask import Flask, request, jsonify

import sqlite3

import bcrypt

import re



app = Flask(__name__)



# Function to validate username format

def is_valid_username(username):

    # Simple check for alphanumeric characters and underscores

    return re.match(r'^\w+$', username) is not None



# Function to hash password using bcrypt

def hash_password(password):

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed.decode('utf-8')



# Function to insert username and hashed password into database

def insert_user(username, hashed_password):

    conn = sqlite3.connect('users.db')

    cursor = conn.cursor()

    try:

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

        conn.commit()

    except sqlite3.IntegrityError:

        conn.rollback()  # Rollback if username is not unique
 
        conn.close()

        return False

    conn.close()

    return True



# Route to handle user registration

@app.route('/register', methods=['POST'])

def register():

    data = request.get_json()

    username = data.get('username')

    password = data.get('password')



    if not username or not password:

        return jsonify({'error': 'Username and password are required'}), 400



    if not is_valid_username(username):

        return jsonify({'error': 'Invalid username format'}), 400



    hashed_password = hash_password(password)



    if insert_user(username, hashed_password):

        return jsonify({'message': 'User registered successfully'}), 201

    else:

        return jsonify({'error': 'Username already exists'}), 409



if __name__ == '__main__':

    app.run(  )