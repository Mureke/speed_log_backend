from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# We didn't pass app instance here.
db = SQLAlchemy()


class SpeedLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    download = db.Column(db.Float())
    upload = db.Column(db.Float())
    ping = db.Column(db.Float())
    time = db.Column(db.DateTime(), server_default=func.now(), default=func.now())

    def __init__(self,  download, upload, ping):
        self.download = download
        self.upload = upload
        self.ping = ping

    def __str__(self):
        return '<Log: %r>' % self.id
