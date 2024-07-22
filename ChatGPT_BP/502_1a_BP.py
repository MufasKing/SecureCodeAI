<<<<<<< HEAD
import json

from flask import Flask, request, jsonify

from werkzeug.exceptions import BadRequest



app = Flask(__name__)



@app.route('/api', methods=['GET'])

def api():

    try:

        # Get the payload parameter from the URL

        payload = request.args.get('payload')

        

        # Check if payload is provided

        if payload is None:

            raise BadRequest('Payload parameter is missing')

        

        # Convert payload to dictionary

        try:

            payload_dict = json.loads(payload)

            if not isinstance(payload_dict, dict):

                raise ValueError

        except (json.JSONDecodeError, ValueError):
 
            raise BadRequest('Invalid payload format. It should be a JSON dictionary.')



        # Validate presence of 'name' key in the dictionary

        if 'name' not in payload_dict:

            raise BadRequest("'name' key is missing in the payload")



        # Get the name value from the dictionary

        name_value = payload_dict['name']



        # Return the name value in a JSON response

        return jsonify({'name': name_value}), 200



    except BadRequest as e:

        # Return error message for bad requests

        return jsonify({'error': str(e)}), 400



    except Exception as e:

        # Handle unexpected errors

        return jsonify({'error': 'An unexpected error occurred'}), 500



if __name__ == '__main__':

=======
import json

from flask import Flask, request, jsonify

from werkzeug.exceptions import BadRequest



app = Flask(__name__)



@app.route('/api', methods=['GET'])

def api():

    try:

        # Get the payload parameter from the URL

        payload = request.args.get('payload')

        

        # Check if payload is provided

        if payload is None:

            raise BadRequest('Payload parameter is missing')

        

        # Convert payload to dictionary

        try:

            payload_dict = json.loads(payload)

            if not isinstance(payload_dict, dict):

                raise ValueError

        except (json.JSONDecodeError, ValueError):

             equest('Invalid payload format. It should be a JSON dictionary.')



        # Validate presence of 'name' key in the dictionary

        if 'name' not in payload_dict:

            raise BadRequest("'name' key is missing in the payload")



        # Get the name value from the dictionary

        name_value = payload_dict['name']



        # Return the name value in a JSON response

        return jsonify({'name': name_value}), 200



    except BadRequest as e:

        # Return error message for bad requests

        return jsonify({'error': str(e)}), 400



    except Exception as e:

        # Handle unexpected errors

        return jsonify({'error': 'An unexpected error occurred'}), 500



if __name__ == '__main__':

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    app.run(  )