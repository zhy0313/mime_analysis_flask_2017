from . import db


class TimeCount(db.Model):
    __tablename__ = 'time_count'
    id = db.Column(db.Integer(), primary_key=True)

    year = db.Column('year', db.Integer(), nullable=False)
    month = db.Column('month', db.Integer(), nullable=False)
    day = db.Column('day', db.Integer(), nullable=False)

    visit_count = db.Column('visit_count', db.Integer(), nullable=False)
    register_count = db.Column('register_count', db.Integer(), nullable=False)
    authorize_count = db.Column('authorize_count', db.Integer(), nullable=False)
    trade_count = db.Column('trade_count', db.Integer(), nullable=False)

