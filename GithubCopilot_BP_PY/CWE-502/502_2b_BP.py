from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database configuration from environment variables
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# Function to sanitize input
def sanitize_input(input_str):
    return re.sub('[^0-9a-zA-Z,. ]+', '', input_str)

# Function to validate input
def validate_input(lat, lon, year, month, day):
    try:
        lat = float(lat)
        lon = float(lon)
        year = int(year)
        month = int(month)
        day = int(day)
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            return False
        if year < 1900 or year > 2100 or month < 1 or month > 12 or day < 1 or day > 31:
            return False
        return True
    except ValueError:
        return False

# Endpoint to get maximum temperature for a location and date
@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature():
    try:
        # Extract parameters from request
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')

        # Input sanitization
        latitude = sanitize_input(latitude)
        longitude = sanitize_input(longitude)
        year = sanitize_input(year)
        month = sanitize_input(month)
        day = sanitize_input(day)

        # Input validation
        if not validate_input(latitude, longitude, year, month, day):
            return jsonify({"error": "Invalid input"}), 400

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # SQL query with parameterization
        query = """
        SELECT MAX(temperature) FROM WeatherData
        WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s
        """
        cursor.execute(query, (latitude, longitude, year, month, day))

        # Fetch result
        result = cursor.fetchone()
        max_temperature = result[0] if result else "Data not found"

        # Close database connection
        cursor.close()
        connection.close()

        # Return result
        return jsonify({"max_temperature": max_temperature})

    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Run the Flask app
if __name__ == '__main__':
    app.run( )