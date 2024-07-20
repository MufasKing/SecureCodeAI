from flask import Flask, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You should use a secure, random key in production

# Simulated user data
users = {
    'user1': {'password': 'password123', 'role': 'user'},
    'admin1': {'password': 'admin123', 'role': 'admin'}
}

@app.route('/')
def home():
    if 'username' in session:
        user = session['username']
        if users[user]['role'] == 'admin':
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials', 401
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/user')
def user_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f'Welcome to the user page, {session["username"]}!'

@app.route('/admin')
def admin_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    if users[session['username']]['role'] != 'admin':
        return redirect(url_for('user_page'))
    return f'Welcome to the admin page, {session["username"]}!'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
