<<<<<<< HEAD
from flask import Flask, request, jsonify

import bcrypt

import hmac

import re

import secrets



app = Flask(__name__)



# Secure random secret key

app.secret_key = secrets.token_hex(16)



# Example user data (for demonstration purposes, normally this would be stored securely in a database)

users = {

    "user1": bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt()),

    "user2": bcrypt.hashpw("mypassword".encode('utf-8'), bcrypt.gensalt())

}



def validate_input(username, password):

    """Validates the username and password format."""

    username_re = re.compile(r'^[a-zA-Z0-9_]{3,30}$')

    password_re = re.compile(r'^[a-zA-Z0-9@#$%^&+=]{8,30}$')

    if not username_re.match(username) or not password_re.match(password):

        return False
 
    return True



@app.route('/check_mod', methods=['GET'])

def check_mod():

    username = request.args.get('username')

    password = request.args.get('password')

    

    # Input validation

    if not username or not password or not validate_input(username, password):

        return jsonify(result='false'), 400

    

    # User existence check and password verification

    if username in users:

        stored_password_hash = users[username]

        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):

            # Secure constant-time comparison

            if hmac.compare_digest(password.encode('utf-8'), password.encode('utf-8')):

                return jsonify(result='true'), 200

    

    return jsonify(result='false'), 401



if __name__ == '__main__':

=======
from flask import Flask, request, jsonify

import bcrypt

import hmac

import re

import secrets



app = Flask(__name__)



# Secure random secret key

app.secret_key = secrets.token_hex(16)



# Example user data (for demonstration purposes, normally this would be stored securely in a database)

users = {

    "user1": bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt()),

    "user2": bcrypt.hashpw("mypassword".encode('utf-8'), bcrypt.gensalt())

}



def validate_input(username, password):

    """Validates the username and password format."""

    username_re = re.compile(r'^[a-zA-Z0-9_]{3,30}$')

    password_re = re.compile(r'^[a-zA-Z0-9@#$%^&+=]{8,30}$')

    if not username_re.match(username) or not password_re.match(password):

        return False

    return T 



@app.route('/check_mod', methods=['GET'])

def check_mod():

    username = request.args.get('username')

    password = request.args.get('password')

    

    # Input validation

    if not username or not password or not validate_input(username, password):

        return jsonify(result='false'), 400

    

    # User existence check and password verification

    if username in users:

        stored_password_hash = users[username]

        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):

            # Secure constant-time comparison

            if hmac.compare_digest(password.encode('utf-8'), password.encode('utf-8')):

                return jsonify(result='true'), 200

    

    return jsonify(result='false'), 401



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(  )