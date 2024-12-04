from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired

class UserInput(FlaskForm):
    value = StringField(label='Search for Movies', validators=[DataRequired()])
    count = IntegerField(label='Number of recommendations', validators=[DataRequired()], default=24)
    category = RadioField(label='Choose the search category:', choices=['Name', 'Genre', 'Keyword', 'Cast'], validators=[DataRequired()], default='Name')
    submit = SubmitField(label='Recommend movies')