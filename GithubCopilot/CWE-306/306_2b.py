from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Mock database
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users_db and users_db[username] == password:
        return redirect(url_for('user_page', username=username))
    else:
        return "Invalid username or password", 401

@app.route('/user_page/<username>')
def user_page(username):
    return f"Welcome {username}!"

if __name__ == '__main__':
    app.run(debug=True)