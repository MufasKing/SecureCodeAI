from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials for demonstration purposes
USERNAME = 'user'
PASSWORD = 'pass'

# HTML template for login page
login_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Login Page</title>
  </head>
  <body>
    <h2>Login</h2>
    <form method="post" action="/login">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required><br><br>
      <input type="submit" value="Login">
    </form>
    {% if error %}
      <p style="color: red;">{{ error }}</p>
    {% endif %}
  </body>
</html>
'''

# HTML template for session page
session_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Session Page</title>
  </head>
  <body>
    <h2>Welcome to the Session Page!</h2>
    <p>You are logged in successfully.</p>
  </body>
</html>
'''

@app.route('/', methods=['GET'])
def login():
    return render_template_string(login_template, error=None)

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return render_template_string(session_template)
    else:
        return render_template_string(login_template, error='Username or Password is incorrect.')

if __name__ == '__main__':
    app.run(debug=True)
