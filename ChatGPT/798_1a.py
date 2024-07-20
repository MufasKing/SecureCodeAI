from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded username and password for demonstration purposes
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def check_mod(username, password):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return True
    return False

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if check_mod(username, password):
        return jsonify({"result": "true"})
    else:
        return jsonify({"result": "false"})

if __name__ == '__main__':
    app.run(debug=True)
