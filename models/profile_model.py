from app_init import mydb

def user_likes_user(user_id):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT MUSIC.title, GROUP_CONCAT(DISTINCT ARTIST.artistName SEPARATOR ', ') AS artists, GENRE.genreName
        FROM LIKED
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic
        JOIN COMPOSED ON MUSIC.idMusic = COMPOSED.idMusic
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist
        JOIN GENRE ON MUSIC.idGenre = GENRE.idGenre
        WHERE LIKED.idUser = %s
        GROUP BY MUSIC.title, GENRE.genreName
    """, (user_id,))
    return cursor.fetchall()

def update_profile(user_id, userName, password):
    cursor = mydb.cursor()
    cursor.execute("""
        UPDATE USER SET userName = %s, password = SHA1(%s) WHERE idUser = %s
    """, (userName, password, user_id))
    mydb.commit()
    