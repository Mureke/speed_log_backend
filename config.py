from flask import Flask

app = Flask(__name__)

class BaseConfig(object):
    """ Base config class. This fields will use by production and development server """
    ORIGINS = ["*"] # for api calls
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


class Development(BaseConfig):
    """ Development config. We use Debug mode """

    PORT = 1000
    DEBUG = True
    TESTING = False
    ENV = 'dev'


# Currently we only have development config.
# If you have production, you will need to pass it to here.
config = {
    'development': 'config.Development'
}


def configure_app(app):
    """
        App configuration will be here.

        Parameters
        ----------

        app : Flask
            app instance
    """

    app.config.from_object(config['development'])