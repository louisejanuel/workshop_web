from app_init import mydb

def get_matches_by_title(user_id):
    cursor = mydb.cursor()
    query = """
        SELECT U.userName, GROUP_CONCAT(DISTINCT M.title SEPARATOR ', ') AS titles
        FROM LIKED L
        JOIN USER U ON U.idUser = L.idUser
        JOIN MUSIC M ON L.idMusic = M.idMusic
        WHERE L.idMusic IN (
            SELECT idMusic FROM LIKED WHERE idUser = %s
        )
        AND U.idUser != %s
        GROUP BY U.userName
        ORDER BY titles
    """
    cursor.execute(query, (user_id, user_id))
    return cursor.fetchall()

def get_matches_by_artist(user_id):
    cursor = mydb.cursor()
    query = """
        SELECT U.userName, GROUP_CONCAT(DISTINCT A.artistName SEPARATOR ', ') AS artists
        FROM LIKED L
        JOIN USER U ON U.idUser = L.idUser
        JOIN MUSIC M ON L.idMusic = M.idMusic
        JOIN COMPOSED C ON M.idMusic = C.idMusic
        JOIN ARTIST A ON C.idArtist = A.idArtist
        WHERE C.idArtist IN (
            SELECT C2.idArtist
            FROM LIKED L2
            JOIN COMPOSED C2 ON L2.idMusic = C2.idMusic
            WHERE L2.idUser = %s
        )
        AND U.idUser != %s
        GROUP BY U.userName
        ORDER BY artists
    """
    cursor.execute(query, (user_id, user_id))
    return cursor.fetchall()


def get_matches_by_genre(user_id):
    cursor = mydb.cursor()
    query = """
        SELECT U.userName, GROUP_CONCAT(DISTINCT G.genreName SEPARATOR ', ') AS genres
        FROM LIKED L
        JOIN USER U ON U.idUser = L.idUser
        JOIN MUSIC M ON L.idMusic = M.idMusic
        JOIN GENRE G ON M.idGenre = G.idGenre
        WHERE M.idGenre IN (
            SELECT M2.idGenre
            FROM LIKED L2
            JOIN MUSIC M2 ON L2.idMusic = M2.idMusic
            WHERE L2.idUser = %s
        )
        AND U.idUser != %s
        GROUP BY U.userName
        ORDER BY genres
    """
    cursor.execute(query, (user_id, user_id))
    return cursor.fetchall()
