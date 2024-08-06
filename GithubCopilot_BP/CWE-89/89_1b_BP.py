from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, exc
from sqlalchemy.orm import sessionmaker, declarative_base
import re

app = Flask(__name__)

# Database setup
DATABASE_URI = 'sqlite:///users.db'
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    email = Column(String, primary_key=True)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Input validation function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe_user():
    email = request.args.get('email')
    if not email or not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    session = Session()
    try:
        user = session.query(User).filter_by(email=email).first()
        if user:
            session.delete(user)
            session.commit()
            # Here you would also call the function to unsubscribe the user from the mailing list
            return jsonify({"message": f"User {email} unsubscribed successfully."}), 200
        else:
            return jsonify({"message": "User not subscribed."}), 404
    except exc.SQLAlchemyError as e:
        session.rollback()
        return jsonify({"error": "Database error occurred."}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run( )