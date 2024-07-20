from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Function to get database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Route to handle temperature query
@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    try:
        # Extract and validate input parameters
        lat = request.args.get('latitude')
        lon = request.args.get('longitude')
        year = request.args.get('year')
        month = request.args.get('month')
        day = request.args.get('day')
        grib_file = request.args.get('grib_file')

        if not all([lat, lon, year, month, day, grib_file]):
            return jsonify({"error": "Missing required parameters"}), 400

        # Input sanitization and validation
        try:
            lat = float(lat)
            lon = float(lon)
            year = int(year)
            month = int(month)
            day = int(day)
        except ValueError:
            return jsonify({"error": "Invalid input types"}), 400

        # Secure database query
        query = """
        SELECT MAX(temperature) as max_temp
        FROM temperatures
        WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s
        """

        # Database connection and query execution
        connection = get_db_connection()
        if connection is None:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (lat, lon, year, month, day, grib_file))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "No data found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)