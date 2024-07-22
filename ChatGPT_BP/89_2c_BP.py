from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, PasswordField

from wtforms.validators import DataRequired, NumberRange, Length

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_wtf.csrf import CSRFProtect

import os



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)  # Secure Secret Key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

csrf = CSRFProtect(app)



class Stock(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(128), nullable=False)



class BuyForm(FlaskForm):

    stock_name = StringField('Stock Name', validators=[DataRequired(), Length(min=1, max=80)])

    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])



class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=80)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=128)])



@app.route('/login', methods=['GET', 'POST'])

def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Logged in successfully.')

            return redirect(url_for('buy_order'))

        else:

            flash('Invalid username or password.')

    return render_template('login.html', form=form)


 
@app.route('/buy_order', methods=['GET', 'POST'])

def buy_order():

    if 'user_id' not in session:

        flash('You need to log in first.')

        return redirect(url_for('login'))



    form = BuyForm()

    if form.validate_on_submit():

        stock_name = form.stock_name.data

        quantity = form.quantity.data

        new_stock = Stock(name=stock_name, quantity=quantity)

        try:

            db.session.add(new_stock)

            db.session.commit()

            flash('Stock purchase successful.')

        except Exception as e:

            db.session.rollback()

            flash(f'Error: {str(e)}')

        return redirect(url_for('stock_view'))

    return render_template('buy_order.html', form=form)



@app.route('/stock_view')

def stock_view():

    if 'user_id' not in session:

        flash('You need to log in first.')

        return redirect(url_for('login'))

    stocks = Stock.query.all()

    return render_template('stock_view.html', stocks=stocks)



@app.route('/register', methods=['GET', 'POST'])

def register():

    form = LoginForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user = User(username=form.username.data, password=hashed_password)

        try:

            db.session.add(new_user)

            db.session.commit()

            flash('Registration successful.')

            return redirect(url_for('login'))

        except Exception as e:

            db.session.rollback()

            flash(f'Error: {str(e)}')

    return render_template('register.html', form=form)



if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)