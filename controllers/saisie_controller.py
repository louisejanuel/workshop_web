from flask import render_template, request, redirect, url_for, session, jsonify
from app_init import app
from models.saisie_model import get_musics, insert_likes, get_liked_musics, insert_like, remove_like

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

@app.route('/api/musics', methods=['GET'])
def get_musics_api():
    user_id = session.get('idUser')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    all_musics = get_musics()
    liked_musics = get_liked_musics(user_id)

    liked_ids = {music[0] for music in liked_musics}
    liked = [music for music in all_musics if music[0] in liked_ids]
    not_liked = [music for music in all_musics if music[0] not in liked_ids]

    return jsonify({'liked': liked, 'not_liked': not_liked})

@app.route('/api/musics/<int:music_id>/like', methods=['POST'])
def like_music(music_id):
    user_id = session.get('idUser')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    insert_like(user_id, music_id)
    return jsonify({'success': True})

@app.route('/api/musics/<int:music_id>/unlike', methods=['POST'])
def unlike_music(music_id):
    user_id = session.get('idUser')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    remove_like(user_id, music_id)
    return jsonify({'success': True})
