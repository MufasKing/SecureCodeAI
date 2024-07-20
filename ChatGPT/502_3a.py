from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Define a dictionary with product prices for demonstration purposes
product_prices = {
    'product1': 10.0,
    'product2': 20.0,
    'product3': 30.0
}

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    # Get YAML payload from query parameter
    yaml_payload = request.args.get('payload')

    if not yaml_payload:
        return "Missing payload query parameter", 400

    try:
        # Parse the YAML payload
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity')
    except yaml.YAMLError as exc:
        return f"Error parsing YAML: {exc}", 400
    except Exception as exc:
        return f"Error processing request: {exc}", 400

    # Validate product code and quantity
    if not product_code or not quantity:
        return "Missing 'product_code' or 'quantity' in payload", 400

    if product_code not in product_prices:
        return f"Product '{product_code}' not found", 404

    if not isinstance(quantity, int) or quantity <= 0:
        return "Quantity must be a positive integer", 400

    # Calculate the total price
    price = product_prices[product_code]
    total_price = price * quantity

    return str(total_price), 200

if __name__ == '__main__':
    app.run(debug=True)
