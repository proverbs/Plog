from flask import render_template, request, redirect, url_for, current_app, flash
from ..models import Article, Tag, User, PlogInfo
from .. import db
from . import user
from flask.ext.login import login_user, current_user, logout_user, login_required
from .forms import PersonalForm, ArticleForm

@user.route('/')
@login_required
def user_index():
	plog_info = PlogInfo.query.first()
	return render_template('user/user-index.html', plog_info = plog_info, current_user = current_user, 
		endpoint = '.user_index')


@user.route('/user-modify', methods = ['GET', 'POST'])
@login_required
def user_modify():
	plog_info = PlogInfo.query.first()
	form = PersonalForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = current_user.email).first()
		user.modify(username = form.username.data, gravatar_hash = form.gravatar_hash.data, 
			password = form.password.data)
		logout_user()
		return redirect(request.args.get('next') or url_for('main.index'))
	return render_template('user/user-modify.html', plog_info = plog_info, current_user = current_user, 
		 form = form, endpoint = '.user_modify')


@user.route('/tag')
@login_required
def tag_manage():
	plog_info = PlogInfo.query.first()
	tags = Tag.query.all()
	return render_template('user/tag-manage.html', plog_info = plog_info, current_user = current_user, 
		tags = tags, endpoint = '.tag_manage')


@user.route('/article')
@login_required
def article_manage():
	plog_info = PlogInfo.query.first()
	articles = Article.query.all()
	return render_template('user/article-manage.html', plog_info = plog_info, current_user = current_user, 
		articles = articles, endpoint = '.article_manage')



@user.route('/write', methods = ['GET', 'POST'])
@login_required
def write_article():
	plog_info = PlogInfo.query.first()
	form = ArticleForm()
	if form.validate_on_submit():
		tag = Tag.query.filter_by(tag_name = form.tag.data).first()
		if tag is None:
			tag = Tag(tag_name = form.tag.data)
			db.session.add(tag)
			db.session.commit()
		#!!!it may be duplicate
		a = Article(user_id = current_user.id, tag_id = tag.id, title = form.title.data, 
			content = form.content.data, summary = form.summary.data)
		db.session.add(a)
		db.session.commit()

		return redirect(url_for('user.user_index'))
	#print(form.title.data, '---------', form.content.data, '-------', form.tag.data, '---------', form.summary.data)
	return render_template('user/user-write.html', plog_info = plog_info, current_user = current_user, 
		form = form, endpoint = '.write_article')
	


@user.route('/edit-about')
@login_required
def edit_about():
	pass



