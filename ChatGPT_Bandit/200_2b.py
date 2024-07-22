from flask import Flask, request, redirect, url_for, render_template_string, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a real secret key for production

def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = check_credentials(username, password)
        
        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    
    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Hello, {session["username"]}! Welcome to your dashboard.'
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run( )
