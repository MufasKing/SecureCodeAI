from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user
from flask_sslify import SSLify
import bleach

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
sslify = SSLify(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)

class BuyOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    stock_name = db.Column(db.String(150), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

class BuyOrderForm(FlaskForm):
    stock_name = StringField('Stock Name', validators=[DataRequired()])
    stock_quantity = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Buy')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/buy', methods=['GET', 'POST'])
@login_required
def buy_stock():
    form = BuyOrderForm()
    if form.validate_on_submit():
        stock_name = bleach.clean(form.stock_name.data)
        stock_quantity = form.stock_quantity.data
        try:
            new_order = BuyOrder(username=current_user.username, stock_name=stock_name, stock_quantity=stock_quantity)
            db.session.add(new_order)
            db.session.commit()
            flash('Buy order placed successfully!', 'success')
            return redirect(url_for('profile'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
    return render_template('buy.html', form=form)

@app.route('/profile')
@login_required
def profile():
    return f'Welcome to your profile, {current_user.username}!'

if __name__ == '__main__':
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'))