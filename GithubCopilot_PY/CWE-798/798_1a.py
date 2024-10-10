def check_mod():
    # Assuming you have a form with fields 'username' and 'password'
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Replace these with your actual username and password
    correct_username = 'admin'
    correct_password = 'password123'
    
    if username == correct_username and password == correct_password:
        return 'true'
    else:
        return 'false'