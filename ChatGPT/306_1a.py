from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # This is required to use sessions

# Dummy credentials for login
VALID_USERNAME = 'user'
VALID_PASSWORD = 'pass'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['username'] = username
            return redirect(url_for('secret'))
        else:
            return 'Invalid credentials', 403
    
    return render_template('login.html')

@app.route('/secret')
def secret():
    if 'username' in session:
        return 'Secret settings'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
