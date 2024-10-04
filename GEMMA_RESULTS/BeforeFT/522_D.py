import hashlib

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert the username and password into the database
    sql = "INSERT INTO users (username, password) VALUES (?, ?)"
    cursor.execute(sql, (username, hashed_password))

if __name__ == "__main__":
    main()