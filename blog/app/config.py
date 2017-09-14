class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@192.168.1.83:5432/blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
