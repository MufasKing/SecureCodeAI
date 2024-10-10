from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to return the price for a product code
def get_price(product_code):
    # Example product prices
    prices = {
        'A001': 10.0,
        'A002': 15.0,
        'A003': 20.0
    }
    return prices.get(product_code, 0.0)

# Route to calculate the price for a product code and quantity
@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity', 1))
    price_per_unit = get_price(product_code)
    total_price = price_per_unit * quantity
    return jsonify({'product_code': product_code, 'quantity': quantity, 'total_price': total_price})

if __name__ == '__main__':
    app.run(port=5000)