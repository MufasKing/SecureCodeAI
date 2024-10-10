from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
import secrets

app = Flask(__name__)

# Secret Key Generation
app.secret_key = secrets.token_hex(16)

# Security Headers
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Mock product prices
product_prices = {
    'P001': 10.0,
    'P002': 20.0,
    'P003': 30.0
}

# Function to get price for a product code
def get_price(product_code):
    return product_prices.get(product_code, None)

# Input Validation
def validate_input(data):
    if 'product_code' not in data or 'quantity' not in data:
        return False, "Missing 'product_code' or 'quantity'"
    if not isinstance(data['product_code'], str) or not isinstance(data['quantity'], int):
        return False, "'product_code' must be a string and 'quantity' must be an integer"
    return True, None

# Route to calculate price
@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    data = request.get_json()
    
    # Input Validation
    is_valid, error_message = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    product_code = data['product_code']
    quantity = data['quantity']
    
    price = get_price(product_code)
    if price is None:
        return jsonify({'error': 'Invalid product code'}), 404
    
    total_price = price * quantity
    return jsonify({'total_price': total_price})

# Error Handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({'error': e.description})
    response.content_type = "application/json"
    return response

# Reverse Proxy Support
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True)