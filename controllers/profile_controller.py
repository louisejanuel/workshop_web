from flask import render_template, redirect, url_for, session, request
from app_init import app
from models.profile_model import update_profile
from models.loginout_model import login_user

@app.route('/updateprofile', methods=['GET', 'POST'])
def updateprofile():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))

    if request.method == 'POST':   
        userName = request.form['userName']
        password = request.form['password']

        update_profile(user_id, userName, password)

        user = login_user(userName, password)
        if user:
            session['user'] = userName
            session['idUser'] = user[0]
            return redirect(url_for('profile'))

    return render_template('updateprofile.html')
