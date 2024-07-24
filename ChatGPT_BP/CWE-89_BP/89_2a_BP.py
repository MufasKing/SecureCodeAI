from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import re

app = Flask(__name__)

# Secure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/stock_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

def sanitize_input(input_string):
    return re.sub(r'[^\w\s]', '', input_string)

def validate_quantity(quantity):
    return isinstance(quantity, int) and quantity > 0

@app.route('/buy', methods=['POST'])
def buy_stock():
    try:
        stock_name = sanitize_input(request.form.get('stock_name'))
        quantity = request.form.get('quantity')

        if not validate_quantity(int(quantity)):
            return jsonify({"error": "Invalid quantity"}), 400

        # Insert into database with parameterized queries
        new_stock = Stock(name=stock_name, quantity=quantity)
        db.session.add(new_stock)
        db.session.commit()

        buy_function(stock_name)

        return jsonify({"message": "Stock purchased successfully"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

def buy_function(stock_name):
    # Process the stock purchase
    print(f"Stock purchased: {stock_name}")
    # Here, add logic for buying the stock, like contacting a brokerage API

if __name__ == '__main__':
    # Ensure the app runs over HTTPS
    app.run(ssl_context=('cert.pem', 'key.pem'))