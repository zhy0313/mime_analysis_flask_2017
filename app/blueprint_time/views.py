import json
from flask import render_template
from flask_login import login_required
from . import blueprint_time
from ..models import TimeCount
from ..models import RegionCount
from sqlalchemy import func
from ..models import db


@blueprint_time.route('/')
@blueprint_time.route('/index/')
@login_required
def index():
    register_count = db.session.query(func.sum(TimeCount.register_count)).first()[0]
    authorize_count = db.session.query(func.sum(TimeCount.authorize_count)).first()[0]
    visit_count = db.session.query(func.sum(TimeCount.visit_count)).first()[0]
    trade_count = db.session.query(func.sum(TimeCount.trade_count)).first()[0]
    ret = {'register_count': register_count, 'authorize_count': authorize_count, 'visit_count': visit_count, 'trade_count': trade_count}
    return render_template('home.html', statistic_info=ret)


@blueprint_time.route('/time_count/')
@login_required
def time_count():
    pass

