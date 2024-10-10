from flask import Flask, request, jsonify
import yaml
import logging
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# Mock function to get price for a product code
def get_price_for_product_code(product_code):
    # Simulated product prices
    product_prices = {
        'A001': 10.0,
        'A002': 20.0,
        'A003': 30.0
    }
    return product_prices.get(product_code)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    # Validate query parameter
    yaml_payload = request.args.get('payload')
    if not yaml_payload:
        logging.error("No YAML payload provided")
        return jsonify({"error": "No YAML payload provided"}), 400

    try:
        # Load YAML payload into a dictionary
        data = yaml.safe_load(yaml_payload)
        
        # Input validation
        if not isinstance(data, dict):
            raise ValueError("Invalid payload format. Expected a dictionary.")
        
        product_code = data.get('product_code')
        quantity = data.get('quantity')

        if not product_code or not isinstance(product_code, str):
            raise ValueError("Invalid or missing product code.")
        
        if not quantity or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid or missing quantity.")
        
        # Calculate total price
        price_per_unit = get_price_for_product_code(product_code)
        if price_per_unit is None:
            raise ValueError("Invalid product code.")
        
        total_price = price_per_unit * quantity

        # Output sanitization
        response = {
            'product_code': product_code,
            'quantity': quantity,
            'total_price': round(total_price, 2)
        }

        # Log the successful operation
        logging.info(f"Price calculated successfully for product {product_code} with quantity {quantity}")

        # Return the total price as a YAML payload
        return yaml.safe_dump(response), 200

    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML payload: {e}")
        return jsonify({"error": "Invalid YAML payload"}), 400
    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='127.0.0.1', port=5000, debug=False)