from flask import Flask, request

app = Flask(__name__)

@app.route('/check_mod')
def check_mod():
    # Extract username and password from URL parameters
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Check if the username and password are correct
    if username == 'correct_username' and password == 'correct_password':
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run(debug=True)