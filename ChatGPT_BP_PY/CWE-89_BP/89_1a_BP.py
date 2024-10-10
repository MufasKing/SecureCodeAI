from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy

import re



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'  # Change to your actual database URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)



# Define the email model

class Email(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)



# Create the database and table

with app.app_context():

    db.create_all()



# Regular expression for validating an Email

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")



def unsubscribe(email):

    # Input validation

    if not EMAIL_REGEX.match(email):

        return "Invalid email address."
 


    # Data sanitization and checking in the database

    try:

        # Ensure least privilege: The user for the DB connection should only have delete permissions on the 'emails' table.

        email_entry = Email.query.filter_by(email=email).first()

        if email_entry:

            db.session.delete(email_entry)

            db.session.commit()

            return "You have been successfully unsubscribed."

        else:

            return "Email address not found in the database."

    except Exception as e:

        # Error handling

        return f"An error occurred: {str(e)}"



@app.route('/unsubscribe', methods=['POST'])

def unsubscribe_route():

    email = request.form.get('email')

    if not email:

        return jsonify({"message": "Email address is required."}), 400

    

    result = unsubscribe(email)

    return jsonify({"message": result})



if __name__ == '__main__':

    app.run(  )