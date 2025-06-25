from app_init import mydb

def get_matches(user_id):
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT DISTINCT
            U.userName,
            M.title,
            GROUP_CONCAT(DISTINCT A.artistName SEPARATOR ', ') AS artists,
            G.genreName
        FROM LIKED L
        JOIN USER U ON U.idUser = L.idUser
        JOIN MUSIC M ON L.idMusic = M.idMusic
        JOIN GENRE G ON M.idGenre = G.idGenre
        JOIN COMPOSED C ON M.idMusic = C.idMusic
        JOIN ARTIST A ON C.idArtist = A.idArtist
        WHERE (
            L.idMusic IN (
                SELECT idMusic FROM LIKED WHERE idUser = %s
            )
            OR C.idArtist IN (
                SELECT C2.idArtist
                FROM LIKED L2
                JOIN COMPOSED C2 ON L2.idMusic = C2.idMusic
                WHERE L2.idUser = %s
            )
            OR M.idGenre IN (
                SELECT M2.idGenre
                FROM LIKED L2
                JOIN MUSIC M2 ON L2.idMusic = M2.idMusic
                WHERE L2.idUser = %s
            )
        )
        AND U.idUser != %s
        GROUP BY U.userName, M.title, G.genreName
    """, (user_id, user_id, user_id, user_id))
    return cursor.fetchall()
