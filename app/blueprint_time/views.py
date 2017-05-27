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
    pass


@blueprint_time.route('/titles/', methods=['GET', 'POST'])
@login_required
def titles():
    pass


@blueprint_time.route('/offices/', methods=['GET', 'POST'])
@login_required
def offices():
    pass


@blueprint_time.route('/hospital_levels/', methods=['GET', 'POST'])
@login_required
def hospital_levels():
    pass


@blueprint_time.route('/age_groups/', methods=['GET', 'POST'])
@login_required
def age_groups():
    pass


@blueprint_time.route('/months/<int:year>', methods=['GET', 'POST'])
@login_required
def months(year):
    pass


@blueprint_time.route('/days/<int:year>/<int:month>', methods=['GET', 'POST'])
@login_required
def days(year, month):
    pass


@blueprint_time.route('/rates/<int:year>/<int:month>', methods=['GET', 'POST'])
@login_required
def rates(year, month):
    pass


