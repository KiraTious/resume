import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'dragonet')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'dragonet')
    HOST = os.environ.get('POSTGRES_HOST', 'mydb')
    PORT = os.environ.get('POSTGRES_PORT', 5432)
    DB = os.environ.get('POSTGRES_DB', 'resume')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = '0'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
