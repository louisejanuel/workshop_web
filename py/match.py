from config import app, mydb
from flask import render_template, redirect, url_for, session

cursor = mydb.cursor()

@app.route('/match', methods=['GET'])
def match():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))

    cursor.execute("""
        SELECT 
            MUSIC.title,
            GROUP_CONCAT(DISTINCT ARTIST.artistName SEPARATOR ', ') AS artists,
            USER.userName
        FROM LIKED
        JOIN USER ON USER.idUser = LIKED.idUser
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic
        JOIN COMPOSED ON MUSIC.idMusic = COMPOSED.idMusic
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist
        WHERE LIKED.idMusic IN (
            SELECT idMusic FROM LIKED WHERE idUser = %s
        )
        AND USER.idUser != %s
        GROUP BY MUSIC.title, USER.userName
    """, (user_id, user_id))

    results = cursor.fetchall()
    return render_template('match.html', data=results)

