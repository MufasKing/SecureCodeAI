import mysql.connector

def is_moderator(user_id: int) -> bool:
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database="my_database"
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Query the database to check if the user is a moderator
    sql = "SELECT * FROM users WHERE user_id = %s AND is_moderator = 1"
    cursor.execute(sql, (user_id,))

    # Check if the user is a moderator
    if cursor.rowcount > 0:
        return True
    else:
        return False

    # Close the cursor and the database connection
    cursor.close()
    db.close()