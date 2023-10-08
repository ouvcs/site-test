import flask
from flask import Flask, render_template, request, session, redirect, url_for, flash

from config import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route("/")
def index():
    return render_template(f"index.html")