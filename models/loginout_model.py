from app_init import mydb

def register_user(firstName, lastName, userName, password):
    cursor = mydb.cursor()
    cursor.execute("""
        INSERT INTO USER (firstName, lastName, userName, password)
        VALUES (%s, %s, %s, SHA1(%s))
    """, (firstName, lastName, userName, password))
    mydb.commit()

def login_user(userName, password):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT * FROM USER WHERE userName = %s AND password = SHA1(%s)
    """, (userName, password))
    return cursor.fetchone()

def user_likes_user(user_id):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT MUSIC.title
        FROM LIKED
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic
        WHERE LIKED.idUser = %s
    """, (user_id,))
    return cursor.fetchall()
