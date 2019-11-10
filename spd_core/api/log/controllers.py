from flask import Blueprint, jsonify
from spd_core import app

log = Blueprint('log', __name__)

@log.route('/', methods=['GET'])
def get_logs():

    return jsonify({ "hello": f"{app.config.get('APPNAME')}" })

@log.route('/<int:log_id>', methods=['GET'])
def logs(log_id):

    return jsonify({ "id": log_id })

