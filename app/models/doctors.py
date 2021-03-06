from . import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column('name', db.String(30), nullable=True)
    real_name = db.Column('real_name', db.String(30), nullable=True)
    phone = db.Column('phone', db.String(11), nullable=False, unique=True)

    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))
    age_group_id = db.Column(db.Integer(), db.ForeignKey('age_group.id'))
    doctor_title_id = db.Column(db.Integer(), db.ForeignKey('doctor_title.id'))
    hospital_id = db.Column(db.Integer(), db.ForeignKey('hospital.id'))
    hospital_level_id = db.Column(db.Integer(), db.ForeignKey('hospital_level.id'))
    hospital_office_id = db.Column(db.Integer(), db.ForeignKey('hospital_office.id'))
    register_year = db.Column('register_year', db.String(30), nullable=True)
    register_month = db.Column('register_month', db.String(30), nullable=True)
    register_day = db.Column('register_day', db.String(30), nullable=True)


class AuthenticatedDoctor(db.Model):
    __tablename__ = 'authenticated_doctor'
    id = db.Column(db.Integer(), primary_key=True)
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    real_name = db.Column('real_name', db.String(30), nullable=False)
    register_year = db.Column('register_year', db.String(30), nullable=False)
    id_number = db.Column('id_number', db.String(30), nullable=False)
    pqc_number = db.Column('pqc_number', db.String(30), nullable=False)
    ppqc_number = db.Column('pqc_number', db.String(30), nullable=False)


class DoctorDisease(db.Model):
    __tablename__ = 'doctor_disease'
    id = db.Column(db.Integer(), primary_key=True)
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'))
    disease_id = db.Column(db.Integer(), db.ForeignKey('disease.id'))
