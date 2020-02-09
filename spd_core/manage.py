import speedtest
from flask import Blueprint
from spd_core.data.models import SpeedLog
from spd_core import db
from spd_core import app
from spd_core.network_tools.network_tools import check_if_scan_available

commands = Blueprint('commands', __name__)


@commands.cli.command('test')
def init_db():
    print('Test command')
    print(app.config.get('PORT'))
    print(app.config.get('SQLALCHEMY_DATABASE_URI'))


@commands.cli.command('speed-test')
def test_speed():
    print('Starting speed test!')
    if check_if_scan_available(app.config.get('BLOCKING_DEVICES')):
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
    else:
        print("Skipping scan")


