from . import db
from ..vendors import bcrypt
from ..vendors import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(30))
    phone = db.Column('phone', db.String(11), unique=True)
    password = db.Column('password', db.String(120))

    def __str__(self):
        return 'name is {name}, phone is {phone}'.format(name=self.username, phone=self.phone)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        ret = bcrypt.check_password_hash(self.password, password)
        return ret


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
