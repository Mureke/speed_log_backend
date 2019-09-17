import click

from spd_core.data.models import db, SpeedLog
from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

db.init_app(app)
migrate = Migrate(app, db)

commands = Blueprint('commands', __name__)


@commands.cli.command('create')
@click.argument('name')
def create(name):
    print(name)
    db.init_app(app)
