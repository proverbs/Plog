#!/usr/bin/env python3
import os
from app import create_app, db
from flask.ext.script import Manager, Command, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.models import Article, User, Tag, Menu, PlogInfo


app = create_app(os.getenv('PLOG_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
#???about python manage.py db migrate
manager.add_command('db', MigrateCommand)


def make_shell_context():
	return dict(db = db, Article = Article, User = User, Tag = Tag, 
		Menu = Menu, PlogInfo = PlogInfo)

manager.add_command("shell", Shell(make_context = make_shell_context))


if __name__ == '__main__':
	manager.run()

