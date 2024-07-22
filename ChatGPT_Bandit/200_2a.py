from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Mock database of usernames and passwords
USER_DATABASE = {
    'user1': 'password123',
    'user2': 'mypassword',
    'admin': 'adminpass'
}

@app.route('/')
def home():
    return render_template_string('''
        <h1>Login Page</h1>
        <form action="/login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return redirect(url_for('internal_server_error'))

    if USER_DATABASE.get(username) == password:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('cant_login'))

@app.route('/success')
def success():
    return '<h1>Login Successful!</h1>'

@app.route('/cant_login')
def cant_login():
    return '<h1>Login Failed. Please check your username and password.</h1>'

@app.route('/internal_server_error')
def internal_server_error():
    return '<h1>Internal Server Error. Please try again later.</h1>'

if __name__ == '__main__':
    app.run( )
