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
    trade_count = db.session.query(func.sum(TimeCount.trade_count)).first()[0]
    ret = {'register_count': register_count, 'authorize_count': authorize_count, 'trade_count': trade_count}
    return render_template('home.html', statistic_info=ret)


@blueprint_time.route('/regions/', methods=['GET', 'POST'])
@login_required
def regions():
    regions_ret = {}
    return json.dumps(regions_ret)


@blueprint_time.route('/titles/', methods=['GET', 'POST'])
@login_required
def titles():
    titles_ret = {}
    return json.dumps(titles_ret)


@blueprint_time.route('/offices/', methods=['GET', 'POST'])
@login_required
def offices():
    offices_ret = {}
    return json.dumps(offices_ret)


@blueprint_time.route('/hospital_levels/', methods=['GET', 'POST'])
@login_required
def hospital_levels():
    hospital_levels_ret = {}
    return json.dumps(hospital_levels_ret)


@blueprint_time.route('/age_groups/', methods=['GET', 'POST'])
@login_required
def age_groups():
    age_groups_ret = {}
    return json.dumps(age_groups_ret)


@blueprint_time.route('/months/<int:year>', methods=['GET', 'POST'])
@login_required
def months(year):
    months_ret = {}
    return json.dumps(months_ret)


@blueprint_time.route('/days/<int:year>/<int:month>', methods=['GET', 'POST'])
@login_required
def days(year, month):
    days_ret = {}
    return json.dumps(days_ret)


@blueprint_time.route('/rates/<int:year>/<int:month>', methods=['GET', 'POST'])
@login_required
def rates(year, month):
    rates_ret = {}
    return json.dumps(rates_ret)


