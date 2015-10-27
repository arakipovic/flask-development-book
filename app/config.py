import os


basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = 'test-app'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'data.sqlite'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
