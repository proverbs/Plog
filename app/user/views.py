from flask import render_template, request, redirect, url_for, current_app, flash
from ..models import Article, Tag, Menu, User, PlogInfo
from .. import db
from . import user
from flask.ext.login import login_user, current_user, logout_user, login_required

@user.route('/')
@login_required
def user_index():
	plog_info = PlogInfo.query.first()
	return render_template('user/user-index.html', plog_info = plog_info, current_user = current_user, 
		endpoint = '.user_index')


@user.route('/user_modify')
@login_required
def user_modify():
	pass


@user.route('/tag')
@login_required
def tag_manage():
	pass


@user.route('/article')
@login_required
def article_manage():
	pass


@user.route('/write')
@login_required
def write_article():
	pass


