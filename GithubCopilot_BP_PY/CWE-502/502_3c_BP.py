import yaml
from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('SecureCatalogueService')
handler = RotatingFileHandler('secure_catalogue.log', maxBytes=10000, backupCount=1)
logger.addHandler(handler)

app = Flask(__name__)

# Dummy function to simulate getting price for a product code
def get_price_for_product_code(product_code):
    # In a real scenario, this would query a database or another service
    prices = {'PROD001': 10.0, 'PROD002': 15.5, 'PROD003': 7.25}
    return prices.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    try:
        # Extract YAML payload from query parameter
        yaml_payload = request.args.get('payload', None)
        if not yaml_payload:
            raise ValueError("Missing payload")

        # Load YAML into dictionary
        data = yaml.safe_load(yaml_payload)
        
        # Input validation
        if 'product_code' not in data or 'quantity' not in data:
            raise ValueError("Invalid payload structure")
        if not isinstance(data['quantity'], int) or data['quantity'] < 1:
            raise ValueError("Quantity must be a positive integer")
        
        # Extract product code and quantity
        product_code = data['product_code']
        quantity = data['quantity']
        
        # Calculate total price
        price_per_unit = get_price_for_product_code(product_code)
        if price_per_unit == 0.0:
            raise ValueError("Invalid product code")
        total_price = price_per_unit * quantity
        
        # Output sanitization
        total_price = round(total_price, 2)  # Ensure the total price is rounded to 2 decimal places
        
        # Log the successful calculation
        logger.info(f"Calculated price for {quantity} units of {product_code}: {total_price}")
        
        # Return total price as YAML payload
        result = yaml.dump({'total_price': total_price})
        return result, 200
    except Exception as e:
        # Log the error
        logger.error(f"Error calculating price: {str(e)}")
        
        # Return error message as YAML payload
        error_message = yaml.dump({'error': str(e)})
        return error_message, 400

if __name__ == '__main__':
    # Principle of Least Privilege: Run the server with minimal permissions necessary
    os.setuid(1000)  # Assuming 1000 is the UID for a less privileged user
    app.run(debug=False, host='0.0.0.0')