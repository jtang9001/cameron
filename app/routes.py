from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    places = [
        {"name": "Cameron", "people": ["Jiayi"]},
        {"name": "CCIS", "people": []},
        {"name": "DICE", "people": ["Ameer", "Adam"]},
        {"name": "ECERF", "people": []},
        {"name": "ECHA", "people": []},
        {"name": "Education", "people": []},
        {"name": "NREF", "people": []}
    ]
    return render_template("index.html", places = places)