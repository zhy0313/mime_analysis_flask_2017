import json
from flask_login import login_required
from . import blueprint_region
from ..models import RegionCount
from ..models import Region
from ..models import Doctor
from ..models import DoctorTitle
from ..models import DoctorDisease
from ..models import HospitalOffice
from ..models import Hospital
from ..models import HospitalLevel
from ..models import Disease
from ..models import AgeGroup
from ..models import AuthenticatedDoctor
from sqlalchemy import func
from ..models import db
from flask import render_template
import datetime


@blueprint_region.route('/index/<string:province>', methods=['GET', 'POST'])
# @login_required
def index(province='湖北'):
    regions_ret = []
    r = db.session.query(Region.province, Region.longitude, Region.latitude, func.sum(RegionCount.register_count),
                         func.sum(RegionCount.authorize_count),
                         func.sum(RegionCount.trade_count), func.sum(RegionCount.video_count),
                         func.sum(RegionCount.group_count)).filter(Region.province == province,
                                                                   RegionCount.region_id == Region.id).first()
    index_ret = {'province': r[0], 'longitude': str(r[1]), 'latitude': str(r[2]), 'register_count': str(r[3]),
                 'authorize_count': str(r[4]),
                 'trade_count': str(r[5]), 'video_count': str(r[6]), 'group_count': str(r[7])}
    print(index_ret)
    return render_template('home.html', statistic_info=index_ret)


@blueprint_region.route('/titles/<string:province>', methods=['GET', 'POST'])
# @login_required
def titles(province='湖北'):
    titles_ret = []
    ret = db.session.query(Doctor.doctor_title_id, DoctorTitle.title,
                           func.count(Doctor.id)).filter(Region.province == province,
                                                         Doctor.region_id == Region.id).group_by(
        Doctor.doctor_title_id).join(DoctorTitle,
                                     Doctor.doctor_title_id == DoctorTitle.id).all()
    for r in ret:
        json_ret = {'doctor_title': r[1], 'count': str(r[2])}
        titles_ret.append(json_ret)
    print(json.dumps(titles_ret))
    return json.dumps(titles_ret)


@blueprint_region.route('/offices/<string:province>', methods=['GET', 'POST'])
# @login_required
def offices(province='湖北'):
    offices_ret = []
    ret = db.session.query(Doctor.hospital_office_id, HospitalOffice.office,
                           func.count(Doctor.id)).filter(Region.province == province,
                                                         Doctor.region_id == Region.id).group_by(
        Doctor.hospital_office_id).join(HospitalOffice,
                                        Doctor.hospital_office_id == HospitalOffice.id).all()
    for r in ret:
        json_ret = {'doctor_office': r[1], 'count': str(r[2])}
        offices_ret.append(json_ret)
    print(json.dumps(offices_ret))
    return json.dumps(offices_ret)


@blueprint_region.route('/hospital_levels/<string:province>', methods=['GET', 'POST'])
# @login_required
def hospital_levels(province='湖北'):
    hospital_levels_ret = []
    ret = db.session.query(Doctor.hospital_level_id, HospitalLevel.level,
                           func.count(Doctor.id)).filter(Region.province == province,
                                                         Doctor.region_id == Region.id).group_by(
        Doctor.hospital_level_id).join(HospitalLevel,
                                       Doctor.hospital_level_id == HospitalLevel.id).all()
    for r in ret:
        json_ret = {'hospital_level': str(r[1]), 'count': str(r[2])}
        hospital_levels_ret.append(json_ret)
    print(json.dumps(hospital_levels_ret))
    return json.dumps(hospital_levels_ret)


# TODO
@blueprint_region.route('/diseases/<string:province>', methods=['GET', 'POST'])
# @login_required
def diseases(province='湖北'):
    diseases_set = []
    ret = db.session.query(DoctorDisease.disease_id, Doctor.hospital_level_id, Disease.name_ch, HospitalLevel.level,
                           func.count(DoctorDisease.doctor_id)).filter(Region.province == province,
                                                                       Doctor.region_id == Region.id, DoctorDisease.doctor_id==Doctor.id, Doctor.hospital_level_id == HospitalLevel.id).group_by(
        DoctorDisease.disease_id, Doctor.hospital_level_id).join(Disease, DoctorDisease.disease_id == Disease.id).all()
    for r in ret:
        json_ret = {'hospital_level': str(r[3]),'disease':str(r[2]), 'count': str(r[4])}
        diseases_set.append(json_ret)
    print(json.dumps(diseases_set))
    return json.dumps(diseases_set)


@blueprint_region.route('/months/<string:province>/<int:year>', methods=['GET', 'POST'])
# @login_required
def months(province='湖北', year=datetime.datetime.now().year):
    months_ret = []
    ret = db.session.query(RegionCount.month, func.sum(RegionCount.register_count),
                           func.sum(RegionCount.authorize_count),
                           func.sum(RegionCount.trade_count)).filter(Region.province == province,
                                                                     RegionCount.region_id == Region.id,
                                                                     RegionCount.year == year).group_by(
        RegionCount.month).all()
    for r in ret:
        json_ret = {'month': r[0], 'register_count': str(r[1]), 'authorize_count': str(r[2]), 'trade_count': str(r[3])}
        months_ret.append(json_ret)
    # print(json.dumps(months_ret))
    return json.dumps(months_ret)


@blueprint_region.route('/days/<string:province>/<int:year>/<int:month>', methods=['GET', 'POST'])
# @login_required
def days(province='湖北', year=datetime.datetime.now().year, month=datetime.datetime.now().month):
    days_ret = []
    ret = db.session.query(RegionCount.day, func.sum(RegionCount.register_count), func.sum(RegionCount.authorize_count),
                           func.sum(RegionCount.trade_count)).filter(Region.province == province,
                                                                     RegionCount.region_id == Region.id,
                                                                     RegionCount.year == year,
                                                                     RegionCount.month == month).group_by(
        RegionCount.day).all()
    for r in ret:
        json_ret = {'day': r[0], 'register_count': str(r[1]), 'authorize_count': str(r[2]), 'trade_count': str(r[3])}
        days_ret.append(json_ret)
    # print(json.dumps(days_ret))
    return json.dumps(days_ret)
