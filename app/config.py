import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'xsm secret key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SMS_API_HOST = r'http://sms-api.luosimao.com/v1/send.json'
    SMS_API_KEY = r'key-4efc7922b1bc90b949a2fa073519eb61'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'xsm secret key for development'
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://root:root@localhost:3306/development_database'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'xsm secret key for production'
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://user:password@localhost:3306/production_database'


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
