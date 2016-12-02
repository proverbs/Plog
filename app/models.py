from datetime import datetime
from . import db


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


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(64), unique = True)
	username = db.Column(db.String(64), unique = True)
	password_hash = db.Column(db.String(128))
	avatar_hash = db.Column(db.String(32))

	#'Article' is class name, 'articles' is attibute
	relationship_articles = db.relationship('Article', backref = 'articles_user', lazy = 'dynamic')


class Tag(db.Model):
	__tablename__ = 'tags'
	id = db.Column(db.Integer, primary_key = True)
	tag_name = db.Column(db.String(64), unique = True)

	relationship_tags = db.relationship('Article', backref = 'articles_tag', lazy = 'dynamic')


class Menu(db.Model):
	__tablename__ = 'menus'
	id = db.Column(db.Integer, primary_key = True)
	menu_name = db.Column(db.String(64), unique = True)

	relationship_menus = db.relationship('Article', backref = 'articles_menu', lazy = 'dynamic')


class PlogInfo(db.Model):
	__tablename__ = 'plog_info'
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(64))
	signature = db.Column(db.Text)
	navigation_bar = db.Column(db.String(64))

