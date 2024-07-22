from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'localhost',
    'database': 'your_db_name'
}

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature():
    try:
        # Extract parameters from the request
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')
        grib_file = request.args.get('grib_file')

        # Validate parameters
        if not all([latitude, longitude, year, month, day, grib_file]):
            return jsonify({"error": "Missing parameters"}), 400

        # Convert parameters to appropriate types
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            year = int(year)
            month = int(month)
            day = int(day)
        except ValueError:
            return jsonify({"error": "Invalid parameter values"}), 400

        # Connect to the database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        # Define the query
        query = """
        SELECT MAX(temperature) AS max_temperature
        FROM weather_data
        WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s
        """
        params = (latitude, longitude, year, month, day)

        # Execute the query
        cursor.execute(query, params)
        result = cursor.fetchone()

        # Close the connection
        cursor.close()
        connection.close()

        # Return the result
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No data found for the specified parameters"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run( )
