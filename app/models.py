from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextArea
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    description = TextArea('Password', validators=[InputRequired()])
    poster = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

