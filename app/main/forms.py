from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional


class CommentForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('e-mail', validators=[DataRequired(), Length(1, 64), Email()])
    content = TextAreaField('content', validators=[DataRequired(), Length(1, 1024)])
    follow = StringField(validators=[DataRequired()])
