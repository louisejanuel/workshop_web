from config import app, mydb
from flask import render_template, redirect, url_for, session, request, jsonify

cursor = mydb.cursor()

@app.route('/updateprofile', methods=['GET', 'POST'])
def updateprofile():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        cursor.execute("""
        UPDATE USER SET userName = %s, password = SHA1(%s) WHERE idUser=%s""", 
        (userName, password, session.get('idUser')))
        mydb.commit()
        cursor.execute("SELECT * FROM USER WHERE userName=%s AND password=SHA1(%s)", (userName, password))
        user = cursor.fetchone()
        if user:
            session['user'] = userName
            session['idUser'] = user[0]

            return redirect(url_for('profile'))
    return render_template('updateprofile.html')
  


# SUPPRIMER COMPTE
# MODIFIER MOT DE PASSE & USERNAME
# PDP ?