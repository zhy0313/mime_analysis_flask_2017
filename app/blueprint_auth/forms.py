import datetime
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import EqualTo

from ..models import User


class LoginForm(FlaskForm):
    phone = StringField('Phone', [DataRequired(), Length(max=11)])
    password = PasswordField('Password', [DataRequired()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False
        # if the user not exist
        user = User.query.filter_by(phone=self.phone.data).first()
        if not user:
            return False
        # if the passwords not match
        if not user.check_password(self.password.data):
            return False

        return True


class RegisterForm(FlaskForm):
    phone = StringField('Phone', [DataRequired(), Length(max=11)])
    code = StringField('Code', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    def validate(self):
        check_validate = super(RegisterForm, self).validate()
        if not check_validate:
            return False
        # If the phone is allowed.
        user = User.query.filter_by(phone=self.phone.data).first()
        if not user:
            return False
        # If the code match.
        time_diff = datetime.datetime.now() - user.updated_at
        if (user.sms_code != self.code.data) or (time_diff.seconds > 300):
            return False
        return True

