# -*- coding: utf-8 -*-
import random
import mysql.connector
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_cors import CORS

mydb = mysql.connector.connect(
    host="163.172.165.87",
    user="Uning",
    password="UnIGaN!!",
    database="Uning"
)

app = Flask(__name__)
CORS(app)

cursor = mydb.cursor()


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users (username, password) VALUES (%, SHA1(%))", (username, password))
        mydb.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=% AND password=%", (username, password))
        user = cursor.fetchone()
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Bienvenue {session['user']} ! <a href='/logout'>Se déconnecter</a>"
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)