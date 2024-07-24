from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired, Length, Regexp

from flask_limiter import Limiter

from flask_limiter.util import get_remote_address

from flask_talisman import Talisman

from werkzeug.security import generate_password_hash, check_password_hash

import os

import hashlib



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

talisman = Talisman(app, content_security_policy={'default-src': "'self'"})



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(150), nullable=False, unique=True)

    password = db.Column(db.String(300), nullable=False)

    salt = db.Column(db.String(32), nullable=False)



class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[

        DataRequired(),

        Length(min=3, max=150),

        Regexp(r'^\w+$', message="Username must contain only letters, numbers, or underscore")

    ])

    password = PasswordField('Password', validators=[

        DataRequired(),

        Length(min=6)

    ])



@app.route('/register', methods=['GET', 'POST'])

@limiter.limit("5 per minute")

def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data

        password = form.password.data

        salt = os.urandom(16).hex()

        hashed_password = generate_password_hash(password + salt)

        

        new_user = User(username=username, password=hashed_password, salt=salt)

        try:

            db.session.add(new_user)

            db.session.commit()

            flash('Registration successful!', 'success')

            return redirect(url_for('login'))

        except Exception as e:

            db.session.rollback()

            flash(f'Error: {str(e)}', 'danger')

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])

@limiter.limit("5 per minute")

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        

        user = User.query.filter_by(username=username).first()

        if user:

            if check_password_hash(user.password, password + user.salt):

                flash('Login successful!', 'success')

                return redirect(url_for('dashboard'))

            else:

                flash('Invalid username or password', 'danger')

        else:

            flash('Invalid username or password', 'danger')

    return render_template('login.html')



@app.route('/dashboard')

def dashboard():

    return "Welcome to your dashboard!"



if __name__ == '__main__':

    db.create_all()

    app.run(ssl_context=('cert.pem', 'key.pem'))