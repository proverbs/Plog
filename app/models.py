from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from . import login_manager
from flask.ext.login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Article(db.Model):
	__tablename__ = 'articles'
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
	menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))

	title = db.Column(db.String(64), unique = True)
	content = db.Column(db.Text)
	summary = db.Column(db.Text)
	create_time = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	update_time = db.Column(db.DateTime, index = True, default = datetime.utcnow)


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(64), unique = True)
	username = db.Column(db.String(64), unique = True)
	password_hash = db.Column(db.String(128))
	avatar_hash = db.Column(db.String(32))

	#'Article' is class name, 'articles' is attibute
	user_articles = db.relationship('Article', backref = 'article_user', lazy = 'dynamic')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


class Tag(db.Model):
	__tablename__ = 'tags'
	id = db.Column(db.Integer, primary_key = True)
	tag_name = db.Column(db.String(64), unique = True)

	tag_articles = db.relationship('Article', backref = 'article_tag', lazy = 'dynamic')


class Menu(db.Model):
	__tablename__ = 'menus'
	id = db.Column(db.Integer, primary_key = True)
	menu_name = db.Column(db.String(64), unique = True)

	menu_articles = db.relationship('Article', backref = 'article_menu', lazy = 'dynamic')


class PlogInfo(db.Model):
	__tablename__ = 'plog_info'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(64))
	signature = db.Column(db.Text)
	navigation_bar = db.Column(db.String(64))

