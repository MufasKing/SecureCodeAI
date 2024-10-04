import re
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# Dummy database of users
users = {
    "user1": {
        "old_email": "user1@example.com",
        "password_hash": generate_password_hash("password123")
    },
    "user2": {
        "old_email": "user2@example.com",
        "password_hash": generate_password_hash("password456")
    }
}

# Regular expressions for email validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@app.route('/update_email', methods=['POST'])
def update_email():
    # Get the user email and password from the request body
    data = request.get_json()
    user_email = data.get('new_email')
    password = data.get('password')

    # Input Validation
    if not user_email or not password:
        return jsonify({"error": "Missing email or password"}), 400
    
    if not EMAIL_REGEX.match(user_email):
        return jsonify({"error": "Invalid email format"}), 400

    # Find the user in the database based on their old email
    for user, user_info in users.items():
        if user_info['old_email'] == data['old_email']:
            # Authenticate the user by checking the password hash
            if check_password_hash(user_info['password_hash'], password):
                # Update the user's email address
                users[user]['old_email'] = user_email
                return jsonify({"message": "Email updated successfully"}), 200
            else:
                return jsonify({"error": "Invalid password"}), 403
    
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)