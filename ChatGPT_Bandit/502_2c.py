from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('weather_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    # Extract parameters from the request
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    if not latitude or not longitude or not date:
        return jsonify({'error': 'Missing parameters'}), 400

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Execute the query to get the temperature for the given latitude, longitude, and date
        query = '''
        SELECT temperature
        FROM weather
        WHERE latitude = ? AND longitude = ? AND date = ?
        '''
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()
        
        if result:
            temperature = result['temperature']
            return jsonify({'temperature': temperature}), 200
        else:
            return jsonify({'error': 'No data found for the given parameters'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run( )
