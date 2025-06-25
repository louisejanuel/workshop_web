from config import app, mydb
from flask import render_template, request, redirect, url_for, session

cursor = mydb.cursor()

@app.route('/saisie', methods=['GET', 'POST'])
def saisie():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    
    cursor.execute("""SELECT COMPOSED.idMusic, title, GROUP_CONCAT(artistName SEPARATOR ', ') AS artists, genreName FROM COMPOSED \
        JOIN MUSIC ON COMPOSED.idMusic = MUSIC.idMusic \
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist \
        JOIN GENRE ON MUSIC.idGenre = GENRE.idGenre \
        GROUP BY idMusic, genreName""")
    musics = cursor.fetchall()
    if request.method == 'POST':
        idmusics = request.form.getlist("idMusic")
        # genre = request.form["genre"]
        for idmusic in idmusics :
            cursor.execute("INSERT INTO LIKED (idUser, idMusic) VALUES (%s, %s)", (user_id, idmusic))
        mydb.commit()

    return render_template('saisie.html', musics=musics)