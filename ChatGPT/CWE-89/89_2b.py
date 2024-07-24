from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock_orders.db'  # Example database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StockOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    stock_name = db.Column(db.String(120), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Retrieve data from form
    username = request.form['username']
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    # Create new stock order record
    new_order = StockOrder(username=username, stock_name=stock_name, stock_quantity=int(stock_quantity))

    # Insert record into the database
    db.session.add(new_order)
    db.session.commit()

    # Redirect to profile page
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    # Fetch user data and render profile page
    return 'Profile Page - User information and orders would be displayed here.'

if __name__ == '__main__':
    app.run( )
