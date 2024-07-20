import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from datetime import datetime
from flask_session import Session

# Load environment variables from .env file
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Secure Flask configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///sensor.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize session management
Session(app)

# Initialize database
db = SQLAlchemy(app)

# Define the Sensor model
class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sensor {self.id} - {self.temperature}C>'

# Create the database tables
with app.app_context():
    db.create_all()

# Utility function to validate and parse date
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None

# Endpoint to get temperature for a given location and date
@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    data = request.json
    
    # Input validation
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date_str = data.get('date')

    if latitude is None or longitude is None or date_str is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude format'}), 400

    date = parse_date(date_str)
    if date is None:
        return jsonify({'error': 'Invalid date format. Expected YYYY-MM-DD'}), 400

    # Database query
    try:
        sensor_data = Sensor.query.filter_by(latitude=latitude, longitude=longitude, date=date).first()
        if sensor_data:
            return jsonify({'temperature': sensor_data.temperature}), 200
        else:
            return jsonify({'error': 'Data not found for the given parameters'}), 404
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
