from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Mock database
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users_db and users_db[username] == password:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_page'))

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

@app.route('/login_page')
def login_page():
    return "Invalid credentials, please try again."

if __name__ == '__main__':
    app.run(debug=True)