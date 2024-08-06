from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from flask_login import LoginManager, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Database model
class StockOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    stock_name = db.Column(db.String(80), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

# Form for stock order
class StockOrderForm(FlaskForm):
    stock_name = StringField('Stock Name', [validators.Length(min=1, max=80)])
    stock_quantity = IntegerField('Quantity', [validators.NumberRange(min=1)])

@login_manager.user_loader
def load_user(user_id):
    # Implement user loader
    pass

@app.route('/buy_stock', methods=['GET', 'POST'])
@login_required
def buy_stock():
    form = StockOrderForm()
    if form.validate_on_submit():
        # Input validation and sanitization is handled by WTForms
        stock_name = form.stock_name.data
        stock_quantity = form.stock_quantity.data
        username = current_user.username  # Assuming current_user is authenticated and loaded
        
        # Insert buy order into the database
        try:
            order = StockOrder(username=username, stock_name=stock_name, stock_quantity=stock_quantity)
            db.session.add(order)
            db.session.commit()
            flash('Stock order placed successfully!')
        except Exception as e:
            db.session.rollback()
            flash('Error placing stock order.')
        
        return redirect(url_for('profile'))
    
    return render_template('buy_stock.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(ssl_context='adhoc')  # This runs the app over HTTPS. For production, use a proper SSL certificate.