import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'a hard to guess string'
	
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True #this setting has been removed in new version
	SQLALCHEMY_TRACK_MODIFICATIONS = True #?

	PLOG_MAIL_SUBJECT_PREFFIX = '[PLOG]'
	PLOG_MAIL_SENDER = 'PLOG Admin <proverbsonly@aliyun.com>'
	PLOG_ADMIN = os.environ.get('PLOG_ADMIN')

	ARTICLES_PER_PAGE = 10
	COMMENTS_PER_PAGE = 10

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config): #extends from Config class
	DEBUG = True #used in unittest
	
	MAIL_SERVER = 'smtp.aliyun.com'
	MAIL_USE_TLS = True
	MAIL_PORT = 587
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
	TESTING = True #used in unittest
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
}



