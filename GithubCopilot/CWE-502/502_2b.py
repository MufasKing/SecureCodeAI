from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    # Extract parameters from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    grib_file = request.args.get('grib_file')

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT MAX(temperature) as max_temperature
                FROM temperature_data
                WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s
            """
            cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
            result = cursor.fetchone()
            max_temperature = result['max_temperature'] if result else None

            return jsonify({'max_temperature': max_temperature})

    except Error as e:
        return jsonify({'error': str(e)})

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)