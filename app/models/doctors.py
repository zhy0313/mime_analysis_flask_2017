from . import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer(), primary_key=True)

    year = db.Column('year', db.Integer(), nullable=False)