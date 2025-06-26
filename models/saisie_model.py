from app_init import mydb

def get_musics():
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT COMPOSED.idMusic, title, GROUP_CONCAT(artistName SEPARATOR ', ') AS artists, genreName
        FROM COMPOSED
        JOIN MUSIC ON COMPOSED.idMusic = MUSIC.idMusic
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist
        JOIN GENRE ON MUSIC.idGenre = GENRE.idGenre
        GROUP BY idMusic, genreName
    """)
    return cursor.fetchall()

def insert_likes(user_id, idmusics):
    cursor = mydb.cursor()
    for idmusic in idmusics:
        cursor.execute("INSERT INTO LIKED (idUser, idMusic) VALUES (%s, %s)", (user_id, idmusic))
    mydb.commit()

def get_liked_musics(user_id):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT MUSIC.idMusic, title, GROUP_CONCAT(artistName SEPARATOR ', ') AS artists, genreName
        FROM LIKED
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic
        JOIN COMPOSED ON MUSIC.idMusic = COMPOSED.idMusic
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist
        JOIN GENRE ON MUSIC.idGenre = GENRE.idGenre
        WHERE LIKED.idUser = %s
        GROUP BY MUSIC.idMusic, genreName
    """, (user_id,))
    return cursor.fetchall()

def insert_like(user_id, music_id):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO LIKED (idUser, idMusic) VALUES (%s, %s)", (user_id, music_id))
    mydb.commit()

def remove_like(user_id, music_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM LIKED WHERE idUser = %s AND idMusic = %s", (user_id, music_id))
    mydb.commit()
