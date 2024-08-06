import os
import logging
import psycopg2
from psycopg2 import sql
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection parameters from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def get_db_connection():
    """Create and return a new database connection."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to the database: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Input validation
    try:
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        date = request.args.get('date')
    except ValueError as e:
        return jsonify({"error": "Invalid input parameters"}), 400

    # Connect to the database
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        # Parameterized query to prevent SQL injection
        query = sql.SQL("SELECT temperature FROM weather_data WHERE latitude = %s AND longitude = %s AND date = %s;")
        cursor = conn.cursor()
        cursor.execute(query, (latitude, longitude, date))
        
        # Fetch the result
        result = cursor.fetchone()
        if result:
            temperature = result[0]
            return jsonify({"temperature": temperature}), 200
        else:
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        logging.error(f"Failed to fetch temperature: {e}")
        return jsonify({"error": "Failed to fetch temperature"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run( )