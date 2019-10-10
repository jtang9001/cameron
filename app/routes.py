from flask import render_template, flash, redirect
from app import app
from app.places import places
from app.forms import PlaceForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlaceForm()
    if form.validate_on_submit():
        print("Check in submitted for name {} at {}".format(
            form.name.data, form.place.data
        ))
        return redirect("/")
    return render_template(
        "index.html", 
        places = places, 
        form = form
    )