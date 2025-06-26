from flask import render_template, session, jsonify
from app_init import app
from models.confirm_delete_model import delete_user_and_related_data
from app_init import mydb

@app.route('/confirmdelete', methods=['GET'])
def confirm_delete():
    return render_template('confirm_delete.html')

@app.route('/api/deleteaccount', methods=['DELETE'])
def delete_account():
    user_id = session.get('idUser')
    if not user_id:
        return jsonify({'success': False, 'message': "Utilisateur non connecté."}), 401

    success, message = delete_user_and_related_data(user_id)
    
    if success:
        session.clear()
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': message}), 500
