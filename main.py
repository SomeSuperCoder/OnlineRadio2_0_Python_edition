from flask import Flask, render_template
from waitress import serve
from database import DataBase


app = Flask(__name__)
database = DataBase("db.json")


@app.route("/")
def index():
    return render_template("index.html", current_audio_file=database.get_data("current_audio_file"))


@app.route("/get_current_audio_file")
def get_current_audio_file():
    pass


@app.route("/get_current_second")
def get_current_second():
    pass


serve(app, port=8080)
