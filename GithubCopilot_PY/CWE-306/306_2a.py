from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy credentials
USERNAME = 'admin'
PASSWORD = 'password'

def is_logged_in():
    return 'username' in session

def is_admin():
    return session.get('username') == USERNAME

@app.route('/')
def index():
    if is_logged_in():
        if is_admin():
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if do_login(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/user')
def user_page():
    if not is_logged_in():
        return redirect(url_for('login'))
    return '<h1>Welcome to the User Page</h1>'

@app.route('/admin')
def admin_page():
    if not is_logged_in():
        return redirect(url_for('login'))
    if not is_admin():
        return redirect(url_for('user_page'))
    return '<h1>Welcome to the Admin Page</h1>'

def do_login(username, password):
    return username == USERNAME and password == PASSWORD

if __name__ == '__main__':
    app.run(debug=True)