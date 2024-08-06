from flask import Flask, request, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import json

app = Flask(__name__)

# Environment Variables
DATABASE_URL = os.environ.get('DATABASE_URL', 'dbname=Sensor user=postgres')

# Database Setup
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Input Validation
def validate_input(data):
    try:
        # Ensure latitude, longitude, and date are present
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        # Validate date format
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        return latitude, longitude, date
    except (ValueError, KeyError):
        return None

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    data = request.json
    validated_input = validate_input(data)
    if not validated_input:
        return jsonify({'error': 'Invalid input'}), 400
    
    latitude, longitude, date = validated_input
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = """
        SELECT temperature FROM temperature_data
        WHERE latitude = %s AND longitude = %s AND date = %s;
        """
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Temperature not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run( )