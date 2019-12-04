from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class UserPost(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    submit = SubmitField('Submit')
