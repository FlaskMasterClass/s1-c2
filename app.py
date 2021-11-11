from flask import Flask 
from config import ProductionConfig
from config import DevelopmentConfig
from config import TestingConfig


profiles = {
    'dev': DevelopmentConfig(),
    'production': ProductionConfig(),
    'testing': TestingConfig()
}


def create_app(profile):
    app = Flask(__name__)
    app.config.from_object(profiles[profile])
    return app


if __name__ == '__main__':
    app = create_app('production')
    app.run()