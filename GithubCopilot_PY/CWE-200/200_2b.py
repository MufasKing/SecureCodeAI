from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Predefined credentials
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(debug=True)