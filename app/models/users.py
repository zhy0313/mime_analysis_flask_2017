from . import db
from ..vendors import bcrypt
from ..vendors import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column('phone', db.String(11), unique=True, nullable=False)
    sms_code = db.Column('sms_code', db.String(4), nullable=True)
    password = db.Column('password', db.String(120), nullable=True)
    updated_at = db.Column('updated_at', db.DateTime(), nullable=True)

    def __str__(self):
        return 'phone is {phone}'.format(phone=self.phone)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        ret = bcrypt.check_password_hash(self.password, password)
        return ret


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
