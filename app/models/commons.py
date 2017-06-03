from . import db


class Disease(db.Model):
    __tablename__ = 'disease'
    id = db.Column(db.Integer(), primary_key=True)
    name_ch = db.Column('name_ch', db.String(30), nullable=False)


class Region(db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer(), primary_key=True)
    province = db.Column('province', db.String(30), nullable=False)
    city = db.Column('city', db.String(30), nullable=False)
    longitude = db.Column('longitude', db.Numeric(12, 6), nullable=True)
    latitude = db.Column('latitude', db.Numeric(12, 6), nullable=True)
    province_id = db.Column(db.Integer(), db.ForeignKey('province.id'))


class Province(db.Model):
    __tablename__ = 'province'
    id = db.Column(db.Integer(), primary_key=True)
    province = db.Column('province', db.String(30), nullable=False)


class AgeGroup(db.Model):
    __tablename__ = 'age_group'
    id = db.Column(db.Integer(), primary_key=True)
    range = db.Column('range', db.String(30), nullable=False)
    range_description = db.Column('range_description', db.String(30), nullable=False)
    age_index = db.Column('age_index', db.Integer(), nullable=False)


class HospitalLevel(db.Model):
    __tablename__ = 'hospital_level'
    id = db.Column(db.Integer(), primary_key=True)
    level = db.Column('level', db.String(30), nullable=False)
    level_description = db.Column('level_description', db.String(30), nullable=False)


class HospitalOffice(db.Model):
    __tablename__ = 'hospital_office'
    id = db.Column(db.Integer(), primary_key=True)
    office = db.Column('office', db.String(30), nullable=False)
    office_description = db.Column('office_description', db.String(30), nullable=False)


class DoctorTitle(db.Model):
    __tablename__ = 'doctor_title'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column('title', db.String(30), nullable=False)
    title_description = db.Column('title_description', db.String(30), nullable=False)


class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column('hospital_name', db.String(50), nullable=False)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))
    hospital_level_id = db.Column(db.Integer(), db.ForeignKey('hospital_level.id'))
