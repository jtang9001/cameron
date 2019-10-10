from flask import render_template
from app import app
from app.places import places
from app.forms import PlaceForm


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        "index.html", 
        places = places, 
        form = PlaceForm()
    )