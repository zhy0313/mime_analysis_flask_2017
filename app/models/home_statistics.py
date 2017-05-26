from . import db


class DailyCount(db.Model):
    __tablename__ = 'daily_count'
    id = db.Column(db.Integer(), primary_key=True)

    year = db.Column('year', db.Integer(), nullable=False)
    month = db.Column('month', db.Integer(), nullable=False)
    day = db.Column('day', db.Integer(), nullable=False)

    visit_count = db.Column('visit_count', db.Integer(), nullable=False)
    register_count = db.Column('register_count', db.Integer(), nullable=False)
    authorize_count = db.Column('authorize_count', db.Integer(), nullable=False)
    authorize_count = db.Column('trade_count', db.Integer(), nullable=False)


class RegionCount(db.Model):
    __tablename__ = 'region_count'
    id = db.Column(db.Integer(), primary_key=True)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))

    year = db.Column('year', db.Integer(), nullable=False)
    month = db.Column('month', db.Integer(), nullable=False)
    day = db.Column('day', db.Integer(), nullable=False)

    visit_count = db.Column('visit_count', db.Integer(), nullable=False)
    register_count = db.Column('register_count', db.Integer(), nullable=False)
    authorize_count = db.Column('authorize_count', db.Integer(), nullable=False)
    authorize_count = db.Column('trade_count', db.Integer(), nullable=False)

