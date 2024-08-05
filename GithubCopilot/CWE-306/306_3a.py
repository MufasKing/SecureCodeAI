from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for demonstration
users = {
    'user1': {
        'email': 'user1@example.com',
        'password': 'hashed_password'  # Assume this is a hashed password
    }
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for user, data in users.items():
            if data['email'] == email and check_password_hash(data['password'], password):
                session['user'] = user
                return redirect(url_for('change_email'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        
        user = session['user']
        user_data = users[user]
        
        if old_email != user_data['email']:
            flash('Old email does not match')
        elif new_email == old_email:
            flash('New email must be different from old email')
        elif not check_password_hash(user_data['password'], confirm_password):
            flash('Incorrect password')
        else:
            users[user]['email'] = new_email
            flash('Email changed successfully')
            return redirect(url_for('change_email'))
    
    return render_template('change_email.html')

if __name__ == '__main__':
    app.run(debug=True)