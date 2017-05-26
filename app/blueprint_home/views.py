import json
from flask import render_template
from flask_login import login_required
from . import blueprint_home
from ..models import DailyCount
from ..models import RegionCount
from sqlalchemy import func
from ..models import db


@blueprint_home.route('/')
@blueprint_home.route('/index/')
#@login_required
def index():
    register_count = db.session.query(func.sum(DailyCount.register_count)).first()[0]
    authorize_count = db.session.query(func.sum(DailyCount.authorize_count)).first()[0]
    visit_count = db.session.query(func.sum(DailyCount.visit_count)).first()[0]
    trade_count = db.session.query(func.sum(DailyCount.trade_count)).first()[0]
    ret = {'register_count': register_count, 'authorize_count': authorize_count, 'visit_count': visit_count, 'trade_count': trade_count}
    return render_template('home.html', statistic_info=ret)


@blueprint_home.route('/daily_count/')
@login_required
def daily_count():
    pass


@blueprint_home.route('/region_count/')
@login_required
def region_count():
    pass
