from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from flask_login import LoginManager, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secure Secret Key
app.config['SECRET_KEY'] = 'your_secure_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Stock Model
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(150), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Form for Stock Purchase
class StockForm(FlaskForm):
    stock_name = StringField('Stock Name', [validators.Length(min=1, max=150)])
    stock_quantity = IntegerField('Stock Quantity', [validators.NumberRange(min=1)])

# User Load Function for Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/buy_stock', methods=['GET', 'POST'])
@login_required
def buy_stock():
    form = StockForm()
    if form.validate_on_submit():
        stock_name = form.stock_name.data
        stock_quantity = form.stock_quantity.data
        
        # Input Validation and Sanitization
        if not stock_name.isalnum():
            flash('Stock name should be alphanumeric.', 'error')
            return redirect(url_for('buy_stock'))
        
        try:
            new_stock = Stock(stock_name=stock_name, stock_quantity=stock_quantity, user_id=current_user.id)
            db.session.add(new_stock)
            db.session.commit()
            flash('Stock purchased successfully!', 'success')
            return redirect(url_for('profile'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('buy_stock'))
    
    return render_template('buy_stock.html', form=form)

@app.route('/profile')
@login_required
def profile():
    return f'Welcome to your profile, {current_user.username}!'

if __name__ == '__main__':
    app.run(debug=True)