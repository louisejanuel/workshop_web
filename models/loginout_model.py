from app_init import mydb

def get_user_by_username(userName):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM USER WHERE userName = %s", (userName,))
    return cursor.fetchone()

def insert_user(firstName, lastName, userName, password):
    cursor = mydb.cursor()
    cursor.execute(
        "INSERT INTO USER (firstName, lastName, userName, password) VALUES (%s, %s, %s, SHA1(%s))",
        (firstName, lastName, userName, password)
    )
    mydb.commit()

def login_user(userName, password):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT * FROM USER WHERE userName = %s AND password = SHA1(%s)
    """, (userName, password))
    return cursor.fetchone()