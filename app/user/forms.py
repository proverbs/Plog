from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class PersonalForm(Form):
	username = StringField('Username', validators=[DataRequired()])
	gravatar_hash = StringField('GravatarHash', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class ArticleForm(Form):
	title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
	content = TextAreaField('Content', validators=[DataRequired()])
	tag = StringField('Tag', validators=[DataRequired()])
	summary = TextAreaField('Summary', validators=[DataRequired()])
	submit = SubmitField('Submit')
