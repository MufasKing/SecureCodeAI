from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize the database
db = SQLAlchemy(app)

# Database model for stocks
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Form for stock entry
class StockForm(FlaskForm):
    stock_name = StringField('Stock Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/buy_order', methods=['GET', 'POST'])
def buy_order():
    form = StockForm()
    if form.validate_on_submit():
        # Input Validation
        stock_name = form.stock_name.data
        quantity = form.quantity.data

        # Insert into database with Parameterized Queries
        new_stock = Stock(name=stock_name, quantity=quantity)
        db.session.add(new_stock)
        db.session.commit()

        # Redirect to stock_view page
        return redirect('/stock_view')
    return render_template('buy_order.html', form=form)

@app.route('/stock_view')
def stock_view():
    # Authentication and Authorization checks should be implemented here
    # For simplicity, this example assumes the user is already authenticated and authorized

    stocks = Stock.query.all()
    return render_template('stock_view.html', stocks=stocks)

if __name__ == '__main__':
    db.create_all()
    app.run( )