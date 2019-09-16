from flask import Blueprint, jsonify, request, current_app

from spd_core.data.models import db, SpeedLog

log = Blueprint('log', __name__)

@log.route('/', methods=['GET'])
def get_logs():

    return jsonify({ "hello": "log" })

@log.route('/<int:id>', methods=['GET'])
def logs(log_id):

    return jsonify({ "id": log_id })

