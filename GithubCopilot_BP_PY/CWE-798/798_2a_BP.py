from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configure database securely
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Define a route and a function to be called when the route is accessed
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Input validation and sanitization
        user_id = max(int(user_id), 1)  # Basic sanitization

        # Execute a query
        user = User.query.filter_by(id=user_id).first()

        # Check if user exists
        if user:
            # Return the result of the query
            return jsonify({'id': user.id, 'name': user.name}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    except ValueError as ve:
        logger.error(f"Value Error: {ve}")
        return jsonify({'error': 'Invalid input'}), 400
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database error'}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Error handling
@app.errorhandler(404)
def not_found(error):
    logger.error(f"404 error: {error}")
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    db.create_all()  # Create the database tables if they don't exist
    app.run( )  # Run the app