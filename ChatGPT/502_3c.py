from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Dummy product price data
PRODUCT_PRICES = {
    'A123': 10.0,
    'B456': 20.0,
    'C789': 30.0
}

def get_price_for_product_code(product_code):
    """Returns the price for a given product code."""
    return PRODUCT_PRICES.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """Calculates total price based on YAML payload query parameter."""
    # Get YAML payload from query parameter
    yaml_payload = request.args.get('data', '')
    
    try:
        # Load YAML data into dictionary
        data = yaml.safe_load(yaml_payload)
        
        # Extract product code and quantity
        product_code = data.get('product_code')
        quantity = data.get('quantity', 0)
        
        if not product_code or quantity <= 0:
            return yaml.dump({'error': 'Invalid product code or quantity'}), 400
        
        # Calculate total price
        price_per_unit = get_price_for_product_code(product_code)
        total_price = price_per_unit * quantity
        
        # Return total price as YAML
        response = {'total_price': total_price}
        return yaml.dump(response)
    
    except yaml.YAMLError as exc:
        return yaml.dump({'error': 'Invalid YAML payload'}), 400

if __name__ == '__main__':
    app.run(debug=True)
