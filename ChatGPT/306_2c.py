from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# This would normally be replaced with actual user authentication logic
users = {'user': 'password'}

# 1. The login function (GET request)
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# 2. The do_login function (POST request)
@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if users.get(username) == password:
        # You would typically set up user sessions here
        return redirect(url_for('index'))
    else:
        return "Login failed", 401

# 3. The index function (GET request)
@app.route('/')
def index():
    return "Welcome to the home page!"

# 4. The user_page function (GET request)
@app.route('/user_page')
def user_page():
    return "Welcome to the user page!"

# 5. The admin_page function (GET request)
@app.route('/admin_page')
def admin_page():
    return "Welcome to the admin page!"

if __name__ == '__main__':
    app.run(debug=True)
