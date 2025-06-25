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
