from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Secret Key Generation
app.secret_key = os.urandom(24)

# Security Headers
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Sample data for product prices
product_prices = {
    "P001": 19.99,
    "P002": 29.99,
    "P003": 9.99
}

# Function to get the price for a product code
def get_price(product_code):
    return product_prices.get(product_code, None)

# Input Validation Function
def is_valid_product_code(product_code):
    return product_code in product_prices

# Route to calculate the price for a product code and quantity
@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    try:
        data = request.get_json()
        if not data or 'product_code' not in data or 'quantity' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        product_code = data['product_code']
        quantity = data['quantity']

        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({'error': 'Quantity must be a positive integer'}), 400

        if not is_valid_product_code(product_code):
            return jsonify({'error': 'Invalid product code'}), 400

        price = get_price(product_code)
        total_price = price * quantity

        return jsonify({'product_code': product_code, 'quantity': quantity, 'total_price': total_price})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Reverse Proxy Support
@app.before_request
def before_request():
    if request.headers.get('X-Forwarded-Proto') == 'https':
        request.environ['wsgi.url_scheme'] = 'https'

if __name__ == '__main__':
    app.run(port=5000)