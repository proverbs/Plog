from flask import render_template, request, redirect, url_for, current_app
from ..models import Article, Tag, Menu, User
from .. import db
from . import main

@main.route('/')
def index():
	#???uncompleted
	page = request.args.get('page', 1, type = int)
	#paging according to article create_time
	pagination = Article.query.order_by(Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	#!!!use pagination.items to get what we want
	articles = pagination.items
	#???what endpoint mean
	return render_template('index.html', articles = articles, pagination = pagination, 
		endpoint = '.index')


@main.route('/article-tags/<int:id>')
def article_tags(id):
	page = request.args.get('page', 1, type = int)
	#???articles is a relationship attribute in models, is it a list
	pagination = Tag.query.get_or_404(id).articles_tag.order_by(
		Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	articles = pagination.items
	#!!!i can change id to a string to better represent article type
	return render_template('index.html', articles = articles, pagination = pagination, 
		endpoint = '.article_tags', id = id)


@main.route('/article-menus/<int:id>')
def article_menus(id):
	page = request.args.get('page', 1, type = int)
	pagination = Menu.query.get_or_404(id).articles_menu.order_by(
		Article.create_time.desc()).paginate(
		page, per_page = current_app.config['ARTICLES_PER_PAGE'], error_out = False)
	articles = pagination.items
	return render_template('index.html', articles = articles, pagination = pagination, 
		endpoint = '.article_menus', id = id)


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
	return render_template('article_details.html', article = article, 
		endpoint = '.article_details', id = id)
