from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from wtforms.validators import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('File', 
                    validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])