# -*- coding: utf-8 -*-
import random
import mysql.connector
from flask import Flask,request,render_template, jsonify
from flask_cors import CORS

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ganache.80!!",
    database="archilog"
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def form():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
