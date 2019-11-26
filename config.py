import os
class Config:
    '''
    Configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Moringa@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'M8742'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):

    '''
    Production configuration child class
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_BLACK_URL")

class DevConfig(Config):

    '''
    Production configuration child class
    '''

    DEBUG = True

Config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}


