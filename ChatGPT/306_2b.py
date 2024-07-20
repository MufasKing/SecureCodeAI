from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
# In a real application, you would query your database
users_db = {
    "username": "password123"  # Example username and password
}

@app.route('/login', methods=['GET'])
def login():
    # Render the login form
    return '''
        <form action="/do_login" method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if username and password are correct
    if username in users_db and users_db[username] == password:
        return redirect(url_for('user_page'))
    else:
        return 'Invalid credentials. Please try again.', 403

@app.route('/user_page')
def user_page():
    return 'Welcome to your user page!'

if __name__ == '__main__':
    app.run(debug=True)
