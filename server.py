# -*- coding: utf-8 -*-
import random
import mysql.connector
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv('password.env')

mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

app = Flask(__name__)
app.secret_key = "chatlunetourte"
CORS(app)

cursor = mydb.cursor()


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['userName']
        password = request.form['password']
        cursor.execute("INSERT INTO USER (firstName, lastName, userName, password) VALUES (%s, %s, %s, SHA1(%s))", (firstName, lastName, userName, password))
        mydb.commit()
        return render_template('profile.html')
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
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", debug=True)