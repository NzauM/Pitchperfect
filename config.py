class Config:
    '''
    Configuration parent class
    '''
    pass

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


