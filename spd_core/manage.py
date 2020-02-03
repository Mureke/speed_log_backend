import speedtest
from flask import Blueprint
from spd_core.data.models import SpeedLog
from spd_core import db
from spd_core import app
from spd_core.network_tools.network_tools import get_devices

commands = Blueprint('commands', __name__)


@commands.cli.command('test')
def init_db():
    print('Test command')
    print(app.config.get('PORT'))
    print(app.config.get('SQLALCHEMY_DATABASE_URI'))


@commands.cli.command('speed-test')
def test_speed():
    print('Starting speed test!')
    print(get_devices())
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    print(f"""
Speed test results:
    Down : {res['download']}
    Up   : {res['upload']}
    Ping : {res['ping']}
    """)
    log_result = SpeedLog(download=res['download'], upload=res['upload'], ping=res['ping'])

    db.session.add(log_result)
    db.session.commit()


@commands.cli.command('get-logs')
def test_get_speed():
    logs = db.session.query(SpeedLog).limit(3)
    for log in logs:
        print("Ping: " + str(log.ping))
        print("down: " + str(log.download))
        print("up: " + str(log.upload))

