from flask import Flask, request, jsonify, session

from werkzeug.security import generate_password_hash, check_password_hash

import secrets



app = Flask(__name__)



# Secure random key generation for session

app.secret_key = secrets.token_hex(32)



# Dummy database

users_db = {

    'moderator': {

        'password_hash': generate_password_hash('moderator_pass'),

        'is_moderator': True

    },

    'user': {

        'password_hash': generate_password_hash('user_pass'),

        'is_moderator': False

    }

}



def auth_mod(username, password, session_token):

    try:

        # Validate session token

        if 'session_token' in session and session['session_token'] == session_token:

            user = users_db.get(username)

            if user and check_password_hash(user['password_hash'], password):

                return user['is_moderator']

        return False

    except Exception as e:

        # Handle unexpected errors

        print(f"Error in auth_mod: {e}")

        return False



@app.route('/check_mod', methods=['GET'])

def check_mod():

    try:

        # Get username, password, and session token from URL

        username = request.args.get('username')

        password = request.args.get('password')

        session_token = request.args.get('session')



        if not all([username, password, session_token]):

            return jsonify({'error': 'Missing username, password, or session token'}), 400



        # Authenticate and check if user is a moderator

        is_moderator = auth_mod(username, password, session_token)



        return jsonify({'is_moderator': is_moderator})

    except Exception as e:

        # Handle unexpected errors

        print(f"Error in check_mod: {e}")

        return jsonify({'error': 'Internal Server Error'}), 500



@app.route('/login', methods=['POST'])

def login():

    try:

        # Get username and password from JSON body

        data = request.get_json()

        username = data.get('username')

        password = data.get('password')



        if not all([username, password]):

            return jsonify({'error': 'Missing username or password'}), 400



        user = users_db.get(username)

        if user and check_password_hash(user['password_hash'], password):

            session_token = secrets.token_hex(32)

            session['session_token'] = session_token

            return jsonify({'message': 'Login successful', 'session_token': session_token})

        

        return jsonify({'error': 'Invalid username or password'}), 401

    except Exception as e:

        # Handle unexpected errors

        print(f"Error in login: {e}")

        return jsonify({'error': 'Internal Server Error'}), 500



if __name__ == '__main__':

    app.run(debug=True)