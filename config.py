import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseConfig(object):
    """ Base config class. This fields will use by production and development server """

    ORIGINS = os.environ.get('ORIGINS', ["*"])
    SECRET_KEY = '4)-.W\xad\x80\x97`\x8e\xc1\xcd\x10\xd7\x11\xd6\x00\xf7M\x89\x18\xceCg'


class Development(BaseConfig):
    """ Development config. We use Debug mode """
    ENV = 'dev'
    PORT = os.environ.get('PORT', 5000)
    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', False)
    APPNAME = os.environ.get('APPNAME', "SpeedLoggerDev")
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    BLOCKING_DEVICES = os.environ.get('BLOCKING_DEVICES', 'Taru-MBP.home,Taru--iPhone.home,mureke.home').split(',')


class Production(BaseConfig):
    """ Production config. We use Debug mode false """
    ENV='production'
    PORT = os.environ.get('PORT', 8080)
    DEBUG = os.environ.get('DEBUG', False)
    TESTING = os.environ.get('TESTING', False)
    APPNAME = os.environ.get('APPNAME', "SpeedLoggerProd")
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    BLOCKING_DEVICES = os.environ.get('BLOCKING_DEVICES', '').split(',')

