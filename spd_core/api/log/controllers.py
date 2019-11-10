from flask import Blueprint, jsonify
from flask import abort, request
from sqlalchemy import func

from spd_core import db
from spd_core.data.models import SpeedLog

log = Blueprint('log', __name__)


@log.route('/', methods=['GET'])
def get_logs():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        logs = db.session.query(SpeedLog).filter(func.date(SpeedLog.time) >= start_date, func.date(SpeedLog.time) <= end_date).order_by(SpeedLog.time)

        return jsonify([row.serialize for row in logs.order_by(SpeedLog.time)])

    return abort(400, 'Error: End date or start date not supplied')



