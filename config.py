import os


class Config:
    TESTING = False
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    ENV_VAR = os.environ.get('ENV_VAR')

class ProductionConfig(Config):
    FAV_FLOWER = 'rose'

class DevelopmentConfig(Config):
    FAV_FLOWER = 'sunflower'

class TestingConfig(Config):
    FAV_FLOWER = 'moonlight petal'
    TESTING = True