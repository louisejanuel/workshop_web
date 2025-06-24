from config import app, mydb
from flask import render_template, request, redirect, url_for, session

cursor = mydb.cursor()


@app.route('/saisie', methods=['GET', 'POST'])
def saisie():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    
    cursor.execute("""SELECT title, GROUP_CONCAT(artistName SEPARATOR ', ') AS artists, genreName FROM COMPOSED \
        JOIN MUSIC ON COMPOSED.idMusic = MUSIC.idMusic \
        JOIN ARTIST ON COMPOSED.idArtist = ARTIST.idArtist \
        JOIN GENRE ON MUSIC.idGenre = GENRE.idGenre \
        GROUP BY title, genreName""", (user_id,))
    musics = cursor.fetchone()
    if request.method == 'POST':
        idmusics = request.form["title"]
        genre = request.form["genre"]
        for i in idmusics :
            cursor.execute("INSERT INTO USER (idUser, idMusic) VALUES (%s, %s)", (user_id, idmusics[i]))
        mydb.commit()

    return render_template('saisie.html', musics=musics)