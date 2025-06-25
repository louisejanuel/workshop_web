from app_init import mydb

def update_profile(user_id, userName, password):
    cursor = mydb.cursor()
    cursor.execute("""
        UPDATE USER SET userName = %s, password = SHA1(%s) WHERE idUser = %s
    """, (userName, password, user_id))
    mydb.commit()
    