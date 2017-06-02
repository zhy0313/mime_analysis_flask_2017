import json
from flask import render_template
from flask_login import login_required
from . import blueprint_time
from ..models import TimeCount
from ..models import RegionCount
from ..models import Region
from ..models import Doctor
from ..models import DoctorTitle
from ..models import HospitalOffice
from ..models import Hospital
from ..models import HospitalLevel
from ..models import AgeGroup
from ..models import AuthenticatedDoctor
from sqlalchemy import func
from ..models import db
import datetime


@blueprint_time.route('/')
@blueprint_time.route('/index/')
# @login_required
def index():
    ret = db.session.query(func.sum(TimeCount.register_count), func.sum(TimeCount.authorize_count),
                           func.sum(TimeCount.trade_count)).first()
    register_count = ret[0]
    authorize_count = ret[1]
    trade_count = ret[2]
    index_ret = {'register_count': register_count, 'authorize_count': authorize_count, 'trade_count': trade_count}
    return render_template('home.html', statistic_info=index_ret)


@blueprint_time.route('/regions/', methods=['GET', 'POST'])
# @login_required
def regions():
    regions_ret = []
    ret = db.session.query(RegionCount.region_id, Region.province, Region.city,
                           func.sum(RegionCount.register_count), func.sum(RegionCount.authorize_count),
                           func.sum(RegionCount.trade_count), Region.longitude, Region.latitude).group_by(
        RegionCount.region_id).join(Region,
                                    Region.id == RegionCount.region_id).all()
    for r in ret:
        json_ret = {'province': r[1], 'city': r[2], 'register_count': str(r[3]), 'authorize_count': str(r[4]),
                    'trade_count': str(r[5]), 'longitude': str(r[6]), 'latitude': str(r[7])}
        regions_ret.append(json_ret)
    #print(json.dumps(regions_ret))
    return json.dumps(regions_ret)


@blueprint_time.route('/titles/', methods=['GET', 'POST'])
#@login_required
def titles():
    titles_ret = []
    ret = db.session.query(Doctor.doctor_title_id, DoctorTitle.title,
                           func.count(Doctor.id)).group_by(Doctor.doctor_title_id).join(DoctorTitle,
                                     Doctor.doctor_title_id == DoctorTitle.id).all()
    for r in ret:
        json_ret = {'doctor_title': r[1], 'count': str(r[2])}
        titles_ret.append(json_ret)
    #print(json.dumps(titles_ret))
    return json.dumps(titles_ret)


@blueprint_time.route('/offices/', methods=['GET', 'POST'])
#@login_required
def offices():
    offices_ret = []
    ret = db.session.query(Doctor.hospital_office_id, HospitalOffice.office,
                           func.count(Doctor.id)).group_by(Doctor.hospital_office_id).join(HospitalOffice,
                                     Doctor.hospital_office_id == HospitalOffice.id).all()
    for r in ret:
        json_ret = {'doctor_office': r[1], 'count': str(r[2])}
        offices_ret.append(json_ret)
    #print(json.dumps(offices_ret))
    return json.dumps(offices_ret)


@blueprint_time.route('/hospital_levels/', methods=['GET', 'POST'])
#@login_required
def hospital_levels():
    hospital_levels_ret = []
    ret = db.session.query(Doctor.hospital_level_id, HospitalLevel.level,
                           func.count(Doctor.id)).group_by(Doctor.hospital_level_id).join(HospitalLevel,
                                     Doctor.hospital_level_id == HospitalLevel.id).all()
    for r in ret:
        json_ret = {'hospital_level': r[1], 'count': str(r[2])}
        hospital_levels_ret.append(json_ret)
    #print(json.dumps(hospital_levels_ret))
    return json.dumps(hospital_levels_ret)


@blueprint_time.route('/age_groups/', methods=['GET', 'POST'])
#@login_required
def age_groups():
    age_groups_ret = []
    ret = db.session.query(Doctor.age_group_id, AgeGroup.range,
                           func.count(Doctor.id)).group_by(Doctor.age_group_id).join(AgeGroup,
                                     Doctor.age_group_id == AgeGroup.id).all()
    for r in ret:
        json_ret = {'age_group': r[1], 'count': str(r[2])}
        age_groups_ret.append(json_ret)
    #print(json.dumps(age_groups_ret))
    return json.dumps(age_groups_ret)


@blueprint_time.route('/months/<int:year>', methods=['GET', 'POST'])
# @login_required
def months(year=datetime.datetime.now().year):
    months_ret = []
    ret = db.session.query(TimeCount.month, func.sum(TimeCount.register_count), func.sum(TimeCount.authorize_count),
                           func.sum(TimeCount.trade_count)).filter(TimeCount.year == year).group_by(
        TimeCount.month).all()
    for r in ret:
        json_ret = {'month': r[0], 'register_count': str(r[1]), 'authorize_count': str(r[2]), 'trade_count': str(r[3])}
        months_ret.append(json_ret)
    #print(json.dumps(months_ret))
    return json.dumps(months_ret)


@blueprint_time.route('/days/<int:year>/<int:month>', methods=['GET', 'POST'])
# @login_required
def days(year=datetime.datetime.now().year, month=datetime.datetime.now().month):
    days_ret = []
    ret = db.session.query(TimeCount.day, func.sum(TimeCount.register_count), func.sum(TimeCount.authorize_count),
                           func.sum(TimeCount.trade_count)).filter(TimeCount.year == year,
                                                                   TimeCount.month == month).group_by(
        TimeCount.day).all()
    for r in ret:
        json_ret = {'day': r[0], 'register_count': str(r[1]), 'authorize_count': str(r[2]), 'trade_count': str(r[3])}
        days_ret.append(json_ret)
    #print(json.dumps(days_ret))
    return json.dumps(days_ret)


@blueprint_time.route('/rates/<int:year>/<int:month>', methods=['GET', 'POST'])
#@login_required
def rates(year=datetime.datetime.now().year, month=datetime.datetime.now().month):
    year_ret = db.session.query(func.sum(TimeCount.register_count), func.sum(TimeCount.authorize_count),
                                func.sum(TimeCount.trade_count)).filter(TimeCount.year == year).first()
    year_register_count = year_ret[0]
    year_authorize_count = year_ret[1]
    year_trade_count = year_ret[2]
    month_ret = db.session.query(func.sum(TimeCount.register_count), func.sum(TimeCount.authorize_count),
                                 func.sum(TimeCount.trade_count)).filter(TimeCount.year == year,
                                                                         TimeCount.month == month).first()
    month_register_count = month_ret[0]
    month_authorize_count = month_ret[1]
    month_trade_count = month_ret[2]
    rates_ret = {'register_rate': float(month_register_count / year_register_count),
                 'authorize_rate': float(month_authorize_count / year_authorize_count),
                 'trade_rate': float(month_trade_count / year_trade_count)}
    return json.dumps(rates_ret)
