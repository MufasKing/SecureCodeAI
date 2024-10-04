from flask import Flask, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define a User model with username and hashed password
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define an Order model with stock name, quantity, and user ID
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Input validation
    if not username or not password:
        return "Username and password are required.", 400
    if not (re.match(r'^[a-zA-Z0-9_]+$', username) and len(password) >= 8):
        return "Invalid username or password.", 400

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "Username already exists.", 409

    # Create a new user
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    session['username'] = username
    return redirect(url_for('profile'))

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Input validation
    if not username or not password:
        return "Username and password are required.", 400

    # Check if the user exists and verify the password
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('profile'))
    else:
        return "Invalid username or password.", 401

# Route for placing an order
@app.route('/place_order', methods=['POST'])
def place_order():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')

    # Input validation
    if not stock_name or not stock_quantity:
        return "Stock name and quantity are required.", 400
    if not re.match(r'^[a-zA-Z0-9 ]+$', stock_name) or not re.match(r'^-?\d+$', stock_quantity):
        return "Invalid stock name or quantity.", 400

    user_id = session.get('user_id')
    if not user_id:
        return "User not logged in.", 403

    try:
        new_order = Order(stock_name=stock_name, quantity=int(stock_quantity), user_id=user_id)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('profile'))
    except Exception as e:
        db.session.rollback()
        return f"Error: {str(e)}", 500

# Route for user profile
@app.route('/profile')
def profile():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    # Simulate recent activities (replace with actual logic)
    recent_activities = ["Purchased 100 shares of AAPL", "Sold 50 shares of MSFT"]

    return f"Welcome, {username}!
Recent activities:
{''.join(recent_activities)}"

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return "The page you are looking for could not be found.", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "An internal server error occurred.", 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)