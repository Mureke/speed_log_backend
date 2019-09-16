from flask import Blueprint, jsonify, request, current_app

from spd_core.data.models import db, SpeedLog

user = Blueprint('log', __name__)

@user.route('/', methods=['GET'])
def get_logs():

    return jsonify({ "hello": "log" })

@user.route('/<int:id>', methods=['GET'])
def logs(id):

    return jsonify({ "id": id })

