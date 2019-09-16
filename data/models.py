from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)


class SpeedLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    download = db.Column(db.Float())
    upload = db.Column(db.Float())
    ping = db.Column(db.Float())
    time = db.Column(db.DateTime(), server_default=func.now())

    def __init__(self,  download, upload, ping, time, created_at):
        self.download = download
        self.upload = upload
        self.ping = ping
        self.time = time
        self.created_at = created_at

