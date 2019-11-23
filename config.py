class Config:
    '''
    Configuration parent class
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Moringa@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):

    '''
    Production configuration child class
    '''

    pass

class DevConfig(Config):

    '''
    Production configuration child class
    '''

    DEBUG = True

Config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}


