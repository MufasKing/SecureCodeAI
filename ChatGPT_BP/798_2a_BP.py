from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from wtforms import Form, StringField, validators
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for example (replace with your actual model)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Define a form for input validation
class UserForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])

# Define a route
@app.route('/add_user', methods=['POST'])
def add_user():
    form = UserForm(request.form)
    if form.validate():
        try:
            # Input sanitization and validation
            name = form.name.data

            # Execute a query
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()

            # Return the result
            return jsonify({'message': 'User added successfully', 'user_id': new_user.id}), 201
        except Exception as e:
            logger.error(f"Error adding user: {e}")
            db.session.rollback()
            return jsonify({'error': 'Failed to add user'}), 500
    else:
        logger.warning(f"Validation failed: {form.errors}")
        return jsonify({'errors': form.errors}), 400

# Error handling
@app.errorhandler(404)
def not_found(error):
    logger.error(f"404 error: {error}")
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}")
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)