#!/usr/bin/env python3
import os
from app import create_app, db
from flask.ext.script import Manager, Command, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app.models import Article, User, Tag, PlogInfo


app = create_app(os.getenv('PLOG_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
#???about python manage.py db migrate
manager.add_command('db', MigrateCommand)


def make_shell_context():
	return dict(db = db, Article = Article, User = User, Tag = Tag, 
		PlogInfo = PlogInfo)

manager.add_command("shell", Shell(make_context = make_shell_context))


#python shell deploy database with simple data case
@manager.command
def deploy():
	from flask.ext.migrate import upgrade

	upgrade()

	u = User(email = '379548839@qq.com', username = 'proverbs')
	u.password = 'xuhao'
	u.gravatar_hash = '3ba386c9bd7c66d78447def6b3c4b352'
	db.session.add(u)
	db.session.commit()

	t = Tag(tag_name = 'tag1')
	db.session.add(t)
	db.session.commit()

	pi = PlogInfo(title = 'Plog | Beautiful and Minimal Blog')
	db.session.add(pi)
	db.session.commit()



if __name__ == '__main__':
	manager.run()

