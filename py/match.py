from config import app, mydb
from flask import render_template, redirect, url_for, session

cursor = mydb.cursor()

@app.route('/match', methods=['GET'])
def match():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    cursor.execute("""
    SELECT DISTINCT 
        MUSIC.title, 
        USER.userName 
        FROM LIKED 
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic 
        JOIN USER ON LIKED.idUser = USER.idUser
        WHERE USER.idUser != %s
    """, (user_id,))
    results = cursor.fetchall()
    print(results)
    return render_template('match.html', data=results)