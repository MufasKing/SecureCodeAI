# Flask Integration
from flask import Flask, request, jsonify
import yaml  # Secure YAML Parsing
import re  # Input Validation

app = Flask(__name__)

# Secure Product Catalog (Example)
product_catalog = {
    "product1": 100,
    "product2": 200,
    "product3": 300
}

def validate_input(product_code, quantity):
    # Basic validation for demonstration
    if not re.match(r'^[a-zA-Z0-9]+$', product_code):
        raise ValueError("Invalid product code")
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Invalid quantity")

def calculate_price(product_code, quantity):
    # Separation of Concerns: Business Logic
    if product_code not in product_catalog:
        raise KeyError("Product not found")
    return product_catalog[product_code] * quantity

@app.route('/calculate_price', methods=['GET'])
def api_calculate_price():
    try:
        # Secure YAML Parsing with SafeLoader
        payload = yaml.safe_load(request.args.get('payload'))
        product_code = payload.get('product_code')
        quantity = payload.get('quantity')

        # Input Validation
        validate_input(product_code, quantity)

        # Calculate Price
        total_price = calculate_price(product_code, quantity)

        return jsonify({"total_price": str(total_price)}), 200
    except yaml.YAMLError:
        return jsonify({"error": "Invalid YAML format"}), 400
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except KeyError as ke:
        return jsonify({"error": str(ke)}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run( )