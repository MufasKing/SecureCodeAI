from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

def validate_email(email):
    # Simple regex for email validation
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    return re.match(regex, email) is not None

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')

    # Input validation
    if not email or not validate_email(email):
        return jsonify({'error': 'Invalid email address'}), 400

    try:
        # Database session management
        user = User.query.filter_by(email=email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'Successfully unsubscribed'}), 200
        else:
            return jsonify({'message': 'Email not found in our database'}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()

if __name__ == '__main__':
    app.run(debug=True)