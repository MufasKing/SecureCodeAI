from flask import Flask, request, render_template_string, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user data
users = {
    'user1': {
        'password': generate_password_hash('password123'),
        'email': 'user1@example.com'
    }
}

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('change_email'))
        else:
            flash('Invalid username or password')
    
    return render_template_string('''
        <h1>Login</h1>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
    ''')

# Change email page
@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        password = request.form['password']
        
        username = session['username']
        user = users.get(username)
        
        if not user:
            flash('User not found')
            return redirect(url_for('login'))
        
        if old_email != user['email']:
            flash('Old email is incorrect')
        elif new_email == old_email:
            flash('New email must be different from old email')
        elif not check_password_hash(user['password'], password):
            flash('Incorrect password')
        else:
            user['email'] = new_email
            flash('Email updated successfully')
            return redirect(url_for('login'))
    
    return render_template_string('''
        <h1>Change Email</h1>
        <form method="post">
            Old Email: <input type="email" name="old_email" required><br>
            New Email: <input type="email" name="new_email" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Change Email">
        </form>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
    ''')

if __name__ == '__main__':
    app.run(debug=True)
