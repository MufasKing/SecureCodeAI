from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials for demonstration purposes
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('session'))
    else:
        return "Username or password is incorrect"

@app.route('/session')
def session():
    return "Welcome to the session page!"

if __name__ == '__main__':
    app.run(debug=True)