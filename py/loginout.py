from config import app, mydb
from flask import render_template, request, redirect, url_for, session

cursor = mydb.cursor()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['userName']
        password = request.form['password']
        cursor.execute("INSERT INTO USER (firstName, lastName, userName, password) VALUES (%s, %s, %s, SHA1(%s))", (firstName, lastName, userName, password))
        mydb.commit()
        return redirect(url_for('profile'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        cursor.execute("SELECT * FROM USER WHERE userName=%s AND password=SHA1(%s)", (userName, password))
        user = cursor.fetchone()
        if user:
            session['user'] = userName
            session['idUser'] = user[0]
            return redirect(url_for('profile'))
    return render_template('login.html')
  

@app.route('/profile', methods=['GET'])
def profile():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    cursor.execute("""
        SELECT MUSIC.title 
        FROM LIKED 
        JOIN MUSIC ON LIKED.idMusic = MUSIC.idMusic 
        WHERE LIKED.idUser = %s
    """, (user_id,))
    results = cursor.fetchall()
    print(results)
    return render_template('profile.html', data=results)



@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('idUser', None)    
    return redirect(url_for('home'))
