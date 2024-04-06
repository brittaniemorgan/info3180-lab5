from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from wtforms.validators import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('File', 
                    validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
=======
from wtforms import StringField, PasswordField, TextArea
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    description = TextArea('Password', validators=[InputRequired()])
    poster = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

>>>>>>> 87c7118289aa95939fbc22c86df8c3dcac8967ec
