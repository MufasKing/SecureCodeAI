from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_temperature_from_db(lat, lon, date):
    # Connect to the SQLite database
    conn = sqlite3.connect('Sensor.db')
    cursor = conn.cursor()

    # Execute a query to retrieve the temperature for the given location and date
    query = '''
    SELECT temperature
    FROM temperature_data
    WHERE latitude = ? AND longitude = ? AND date = ?
    '''
    cursor.execute(query, (lat, lon, date))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    # Check if a result was found
    if result:
        return result[0]
    else:
        return None

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Get JSON data from the request
    data = request.json
    
    # Extract latitude, longitude, and date from the JSON data
    lat = data.get('latitude')
    lon = data.get('longitude')
    date = data.get('date')
    
    if lat is None or lon is None or date is None:
        return jsonify({"error": "Missing data"}), 400
    
    # Retrieve temperature from the database
    temperature = get_temperature_from_db(lat, lon, date)
    
    if temperature is not None:
        return jsonify({"temperature": temperature}), 200
    else:
        return jsonify({"error": "No temperature data found for the given parameters"}), 404

if __name__ == '__main__':
    app.run(debug=True)
