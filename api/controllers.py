from flask import Blueprint, jsonify, request

from speed_tst.data.models import db, SpeedLog

log = Blueprint('speed_log', __name__)

@log.route('/', methods=['GET'])
def get_logs():

    return jsonify({ "message": "Hi user :)"})

@log.route('/<int:id>', methods=['GET'])
def logs(id):

    return jsonify({ "id": id })