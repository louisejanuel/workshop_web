import mysql.connector
from flask import Flask
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
