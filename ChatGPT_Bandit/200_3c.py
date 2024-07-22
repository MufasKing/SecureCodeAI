from flask import Flask, session, jsonify, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required to use sessions

@app.route('/info', methods=['GET'])
def info():
    # Retrieve user details from session
    username = session.get('username', 'Not set')
    email = session.get('email', 'Not set')
    ssn = session.get('ssn', 'Not set')

    # Return user details as a JSON response
    return jsonify({
        'username': username,
        'email': email,
        'ssn': ssn
    })

if __name__ == '__main__':
    app.run( )
