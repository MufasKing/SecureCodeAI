from flask import Flask, request, jsonify

app = Flask(__name__)

# Example credentials (In a real application, use a secure method for storing and validating credentials)
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

@app.route('/check_mod', methods=['GET'])
def check_mod():
    # Extract username and password from query parameters
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Check if both username and password are provided
    if username is None or password is None:
        return 'false', 400  # Bad request if parameters are missing

    # Validate credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run( )
