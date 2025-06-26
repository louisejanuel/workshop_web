from flask import render_template, redirect, url_for, session, request
from app_init import app
from models.match_model import get_matches_by_title, get_matches_by_artist, get_matches_by_genre
from controllers.saisie_controller import get_liked_musics

@app.route('/match')
def match():
    if not session.get('idUser'):
        return redirect(url_for('login'))
    return render_template('match.html')


@app.route('/match_ajax')
def match_ajax():
    user_id = session.get('idUser')
    if not user_id:
        return "Non connecté", 401
    
    liked_musics = get_liked_musics(user_id)
    if not liked_musics:
        return render_template('redirect_likes.html')
    

    sort = request.args.get('sort')
    if sort == 'artist':
        results = get_matches_by_artist(user_id)
    elif sort == 'genre':
        results = get_matches_by_genre(user_id)
    else:
        results = get_matches_by_title(user_id)

    return render_template('match_results.html', results=results, sort=sort)
