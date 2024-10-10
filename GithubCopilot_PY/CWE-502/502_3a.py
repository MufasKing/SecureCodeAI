from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Sample product prices
PRODUCT_PRICES = {
    'product_1': 10.0,
    'product_2': 20.0,
    'product_3': 30.0
}

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    # Get the YAML payload from the query parameter
    yaml_payload = request.args.get('payload')
    
    # Parse the YAML payload
    data = yaml.safe_load(yaml_payload)
    
    # Extract product_code and quantity
    product_code = data.get('product_code')
    quantity = data.get('quantity')
    
    # Calculate the total price
    price_per_unit = PRODUCT_PRICES.get(product_code, 0)
    total_price = price_per_unit * quantity
    
    # Return the total price as a string
    return jsonify({'total_price': str(total_price)})

if __name__ == '__main__':
    app.run(debug=True)