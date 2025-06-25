from flask import render_template, request, redirect, url_for, session
from app_init import app
from models.saisie_model import get_musics, insert_likes

@app.route('/saisie', methods=['GET', 'POST'])
def saisie():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))

    musics = get_musics()

    if request.method == 'POST':
        idmusics = request.form.getlist("idMusic")
        insert_likes(user_id, idmusics)
        return redirect(url_for('profile'))

    return render_template('saisie.html', musics=musics)
