import flask
from flask import Flask, render_template, request, session, redirect, url_for, flash
from hashlib import md5

from config import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route("/")
def index():
    return render_template(f"index.html")

@app.before_request
def before():
    if (not "hash" in session) or (session["hash"] == None) or (session["hash"] != md5((session["id"]+config.SECRET_KEY).encode()).hexdigest()):
        session["id"] = "000000000"
        session["account"] = {
            "name": "Профиль",
            "photo": "https://i.ibb.co/djkrZHs/profile.png",
            "theme": "light"
        }
        session["hash"] = md5((session["id"]+config.SECRET_KEY).encode()).hexdigest()