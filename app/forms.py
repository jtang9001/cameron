from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.places import places

class PlaceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    place = SelectField(
        'Place', 
        choices=[(place["name"], place["name"]) for place in places],
        validators=[DataRequired()]
    )
    submit = SubmitField('Check In')