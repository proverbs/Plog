from flask import render_template, request, redirect, url_for, current_app, flash
from ..models import Article, Tag, User, PlogInfo
from .. import db
from . import main
from .forms import LoginForm
from flask.ext.login import login_user, current_user, logout_user, login_required


@main.route('/')
def index():
	plog_info = PlogInfo.query.first()
	#???uncompleted
	page = request.args.get('page', 1, type = int)
	#paging according to article create_time
	pagination = Article.query.order_by(Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	#!!!use pagination.items to get what we want
	articles = pagination.items
	#???what endpoint mean
	return render_template('index.html', plog_info = plog_info, highlight = 'Home', 
		current_user = current_user, articles = articles, pagination = pagination, 
		endpoint = '.index')


@main.route('/article')
def article():
	#!!!it will cost a lot to query when redicting
	plog_info = PlogInfo.query.first()
	#???uncompleted
	page = request.args.get('page', 1, type = int)
	#paging according to article create_time
	pagination = Article.query.order_by(Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	#!!!use pagination.items to get what we want
	articles = pagination.items
	#???what endpoint mean
	return render_template('article.html', plog_info = plog_info, highlight = 'Article', 
		current_user = current_user, articles = articles, pagination = pagination, 
		endpoint = '.article')


@main.route('/about')
def about():
	plog_info = PlogInfo.query.first()
	return render_template('about.html', plog_info = plog_info, highlight = 'About', 
		current_user = current_user, endpoint = '.about')


@main.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#print('------------------------', form.email.data)
		user = User.query.filter_by(email = form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('.index'))
		#flash('Invalid username or password.')
	return render_template('login.html', highlight = 'Login', form = form, endpoint = '.login')


@main.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('.index'))


@main.route('/article-tags/<int:id>')
def article_tags(id):
	page = request.args.get('page', 1, type = int)
	#???articles is a relationship attribute in models, is it a list
	pagination = Tag.query.get_or_404(id).tag_articles.order_by(
		Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	articles = pagination.items
	#!!!i can change id to a string to better represent article type
	return render_template('index.html', articles = articles, pagination = pagination, 
		endpoint = '.article_tags', id = id)


@main.route('/article-users/<username>')
def article_users(username):
	pass

@main.route('/article-detials/<int:id>', methods = ['GET', 'POST'])
def article_details(id):
	#default form, no follow(reply to)
	#form = CommentForm(request.form, follow = -1)
	article = Article.query.get_or_404(id)
	
	#comment has been submit and it is validate
	#if form.validate_on_submit():
		#???the constructor of Comment
		#!!!use form.x.data to access data in form
		#use flask-disqus instead 
		#comment = Comment(article = article, content = form.content.data, 
			#author_name = form.name.data, author_email = form.email.data)
		#db.session.add(comment)
		#db.session.commit()
		#followed_id = int(form.follow.data)
		#reply to a user, not the author
		#if followed_id != -1:
			#followed = Comment.query.get_or_404(followed_id)
			#f = Follow(follower = comment, followed = followed)
			#comment.comment_type = 'reply'
			#comment.reply_to = followed.author_name
			#db.session.add(f)
			#modify comment
			#db.session.add(comment)
			#db.session.commit()
		#flash('comment successfully ', 'success')
		#return redirect(url_for('.article_details', id = article.id, page = -1))
	#if form.errors:
		#flash('comment failed', 'danger')

	#page = request.args.get('page', 1, type = int)
	#if page == -1:
		#page = (article.comments.count() - 1) // current_app.config['COMMENTS_PER_PAGE'] + 1
	#pagination = article.comments.order_by(Comment.timestamp.asc()).paginate(
		#page, per_page = current_app.config['COMMENTS_PERPAGE'], error_out = False)
	#comments = pagination.items
	#???User 
	#return render_template('article_details.html', User = User, article = article, 
		#comments = comments, pagination = pagination, page = page, form = form, 
		#endpoint = '.article_details', id = article.id)
	plog_info = PlogInfo.query.first()
	return render_template('article-details.html', article = article, 
		highlight = 'Article', plog_info = plog_info, endpoint = '.article_details', id = id)
