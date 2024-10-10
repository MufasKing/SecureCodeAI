from flask import Flask, request, jsonify

import yaml

from yaml.loader import SafeLoader

import os



app = Flask(__name__)



# Secure product catalog

PRODUCT_CATALOG = {

    'P001': 29.99,

    'P002': 49.99,

    'P003': 9.99,

}



def get_product_price(product_code):

    # Separation of concerns: Product price retrieval

    return PRODUCT_CATALOG.get(product_code)



def calculate_total_price(product_code, quantity):

    # Separation of concerns: Total price calculation

    price = get_product_price(product_code)

    if price is None:

        raise ValueError("Invalid product code")

    return price * quantity



@app.route('/calculate_price', methods=['GET'])

def calculate_price():

    # Entry point for the API

    try:

        yaml_payload = request.args.get('payload')

        if not yaml_payload:
 
            raise ValueError("Missing 'payload' query parameter")

        

        # Secure YAML Parsing

        try:

            data = yaml.safe_load(yaml_payload)

        except yaml.YAMLError as e:

            raise ValueError(f"Invalid YAML payload: {str(e)}")



        # Input Validation

        if not isinstance(data, dict):

            raise ValueError("Payload must be a dictionary")

        if 'product_code' not in data or 'quantity' not in data:

            raise ValueError("Payload must contain 'product_code' and 'quantity'")

        product_code = data['product_code']

        quantity = data['quantity']

        if not isinstance(product_code, str) or not isinstance(quantity, int):

            raise ValueError("'product_code' must be a string and 'quantity' must be an integer")

        if quantity <= 0:

            raise ValueError("'quantity' must be a positive integer")



        # Calculate total price

        total_price = calculate_total_price(product_code, quantity)

        return jsonify({"total_price": f"{total_price:.2f}"})

    

    except ValueError as e:

        return jsonify({"error": str(e)}), 400

    except Exception as e:

        return jsonify({"error": "An unexpected error occurred"}), 500



if __name__ == '__main__':

    app.run(  )