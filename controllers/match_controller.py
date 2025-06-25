from flask import render_template, redirect, url_for, session
from app_init import app
from models.match_model import get_matches

@app.route('/match', methods=['GET'])
def match():
    user_id = session.get('idUser')
    if not user_id:
        return redirect(url_for('login'))

    results = get_matches(user_id)
    return render_template('match.html', data=results)