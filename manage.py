import speedtest
from flask import Flask, Blueprint

app = Flask(__name__)

commands = Blueprint('commands', __name__)


@commands.cli.command('test')
def init_db():
    print('Test command')


@commands.cli.command('speed-test')
def test_speed():
    print('Starting speed test!')
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
