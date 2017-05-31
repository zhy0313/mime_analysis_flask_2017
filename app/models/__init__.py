from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .users import User
from .commons import Disease
from .commons import Region
from .commons import AgeGroup
from .commons import Hospital
from .commons import HospitalLevel
from .commons import HospitalOffice
from .commons import DoctorTitle
from .doctors import Doctor
from .doctors import AuthenticatedDoctor
from .time_statistics import TimeCount
from .region_statistics import RegionCount

