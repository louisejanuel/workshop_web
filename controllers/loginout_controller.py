from flask import render_template, request, redirect, url_for, session
from app_init import app
from models.loginout_model import register_user, login_user, user_likes_user

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_user(
            request.form['firstName'],
            request.form['lastName'],
            request.form['userName'],
            request.form['password']
        )
        user = login_user(
            request.form['userName'],
            request.form['password']
        )
        if user:
            session['user'] = user[3]
            session['idUser'] = user[0]
            return redirect(url_for('profile'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = login_user(
            request.form['userName'],
            request.form['password']
        )
        if user:
            session['user'] = user[3]
            session['idUser'] = user[0]
            return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/profile', methods=['GET'])
def profile():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))
    results = user_likes_user(user_id)
    return render_template('profile.html', data=results)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('idUser', None)
    return redirect(url_for('home'))