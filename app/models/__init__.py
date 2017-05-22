from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import your models here,
# otherwise, your models won't be detected by migrate.
from .users import User
