from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to simulate user roles
users = {
    'user1': {'password': 'pass1', 'session': 'sess1', 'is_mod': True},
    'user2': {'password': 'pass2', 'session': 'sess2', 'is_mod': False}
}

def auth_mod(username, password, session):
    """Authenticate if the user is a moderator."""
    user = users.get(username)
    if user and user['password'] == password and user['session'] == session:
        return user['is_mod']
    return False

@app.route('/check_mod', methods=['GET'])
def check_mod():
    """Check if the user is a moderator."""
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')
    
    if username is None or password is None or session is None:
        return jsonify({'error': 'Missing parameters'}), 400
    
    is_mod = auth_mod(username, password, session)
    return jsonify({'is_moderator': is_mod})

if __name__ == '__main__':
    app.run( )
