import click
from flask import Flask

from speed_tst.data.models import db
from speed_tst import app
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

@app.cli.command("migrate")
def migrate(name):
    MigrateCommand(db)