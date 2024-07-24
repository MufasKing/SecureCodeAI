from flask import Flask, request, redirect, url_for, session, render_template, flash

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from werkzeug.exceptions import BadRequestKeyError

import re



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)



# User model

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(150), unique=True, nullable=False)

    password = db.Column(db.String(150), nullable=False)



# Create the database and the user table

with app.app_context():

    db.create_all()



@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        try:

            username = request.form['username']

            password = request.form['password']

        except BadRequestKeyError:

            flash('Invalid input. Please try again.', 'error')

            return redirect(url_for('login'))



        # Input validation

        if not re.match(r'^[a-zA-Z0-9_]+$', username):

            flash('Username must contain only letters, numbers, and underscores.', 'error')

            return redirect(url_for('login'))



        user = User.query.filter_by(username=username).first()



        if user:

            if check_password_hash(user.password, password):

                session['user_id'] = user.id

                flash('Login successful!', 'success')

                return redirect(url_for('home'))

            else:

                flash('Incorrect password. Please try again.', 'error')

                return redirect(url_for('login'))

        else:

            flash('Username does not exist.', 'error')

            return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/home')

def home():

    if 'user_id' not in session:

        flash('Please log in first.', 'error')

        return redirect(url_for('login'))

    return render_template('home.html')



@app.route('/logout')

def logout():

    session.pop('user_id', None)

    flash('You have been logged out.', 'success')

    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])

def register():

    if request.method == 'POST':

        try:

            username = request.form['username']

            password = request.form['password']

        except BadRequestKeyError:

            flash('Invalid input. Please try again.', 'error')

            return redirect(url_for('register'))



        # Input validation

        if not re.match(r'^[a-zA-Z0-9_]+$', username):

            flash('Username must contain only letters, numbers, and underscores.', 'error')

            return redirect(url_for('register'))



        if User.query.filter_by(username=username).first():

            flash('Username already exists. Please choose another one.', 'error')

            return redirect(url_for('register'))



        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)

        db.session.commit()

        flash('Registration successful! Please log in.', 'success')

        return redirect(url_for('login'))

    return render_template('register.html')



if __name__ == '__main__':

    app.run(  )