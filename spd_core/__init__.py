import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from config import BaseConfig
from spd_core.data.models import db
from flask_migrate import Migrate

config = {
    "dev": "config.Development",
    "prod": "config.Production"
}

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
app = Flask(__name__)
env = os.getenv("ENV")

app.config.from_object(config.get(env))

db.init_app(app)
migrate = Migrate(app, db)

""" Cors settings will be here. We maybe use this endpoint later. """
cors = CORS(app, resources={
    r'/api/*': {
        'origins': BaseConfig.ORIGINS
    }
})

from spd_core.api.log.controllers import log
app.url_map.strict_slashes = False
app.register_blueprint(log, url_prefix='/api/logs')

from spd_core.manage import commands
app.register_blueprint(commands, cli_group='commands')
