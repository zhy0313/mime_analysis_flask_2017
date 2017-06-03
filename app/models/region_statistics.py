from . import db


class RegionCount(db.Model):
    __tablename__ = 'region_count'
    id = db.Column(db.Integer(), primary_key=True)
    region_id = db.Column(db.Integer(), db.ForeignKey('region.id'))

    year = db.Column('year', db.Integer(), nullable=False)
    month = db.Column('month', db.Integer(), nullable=False)
    day = db.Column('day', db.Integer(), nullable=False)

    register_count = db.Column('register_count', db.Integer(), nullable=False)
    authorize_count = db.Column('authorize_count', db.Integer(), nullable=False)
    trade_count = db.Column('trade_count', db.Integer(), nullable=False)
    video_count = db.Column('video_count', db.Integer(), nullable=False)
    group_count = db.Column('group_count', db.Integer(), nullable=False)

