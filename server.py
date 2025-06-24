# -*- coding: utf-8 -*-
import random
import mysql.connector
from flask import Flask,request,render_template, jsonify
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
CORS(app)


@app.route("/")
def form():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
