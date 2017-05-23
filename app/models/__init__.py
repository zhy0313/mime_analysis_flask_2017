from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .users import User
from .essentials import Disease
from .essentials import Region
from .essentials import AgeGroup
from .essentials import HospitalLevel
from .essentials import HospitalOffice
from .essentials import DoctorTitle
from .home_statistics import DailyCount
from .home_statistics import RegionCount

